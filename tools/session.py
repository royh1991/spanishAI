#!/usr/bin/env python3
"""Session tooling: generate headers, ingest debriefs, track progress.

Commands:
  start [--task TEXT] [--goal TEXT]   print the session header for today
  log FILE [--commit]                 ingest a debrief JSON, update all state
  stats                               regenerate PROGRESS.md

State contract: state/state.json holds counters and rotations;
state/error-ledger.json holds per-error tracking. Debrief JSON schema is
defined in prompts/debrief.md.
"""

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state" / "state.json"
LEDGER = ROOT / "state" / "error-ledger.json"
LOGS = ROOT / "state" / "session-logs"
LESSONS = ROOT / "lessons"
INBOX = ROOT / "state" / "vocab" / "inbox.md"
TSV = ROOT / "state" / "vocab" / "anki-import.tsv"
TEMPLATE = ROOT / "prompts" / "session-header-template.md"
PROGRESS = ROOT / "PROGRESS.md"

TARGET_MINUTES = 500 * 60


def load(path):
    return json.loads(path.read_text())


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def iso_week(d):
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def week_index(week_key):
    y, w = week_key.split("-W")
    return int(y) * 53 + int(w)


# ---------------------------------------------------------------- start

def active_targets(ledger, n=3):
    pool = [e for e in ledger if e["status"] == "active"]
    if not pool:
        pool = [e for e in ledger if e["status"] == "watch"]
    pool.sort(key=lambda e: (e["last_targeted"] or "", e["id"]))
    return pool[:n]


def recent_vocab(n=8):
    if not TSV.exists():
        return []
    rows = [r.split("\t") for r in TSV.read_text().strip().splitlines() if r.strip()]
    return [r[0] for r in rows[-n:]]


def next_lesson(state):
    seq_file = LESSONS / "SEQUENCE"
    if not seq_file.exists():
        return None, None
    seq = seq_file.read_text().split()
    i = state.get("lesson_index", 0)
    if i >= len(seq):
        return None, None
    return seq[i], (LESSONS / (seq[i] + ".md")).read_text()


def cmd_start(args):
    state = load(STATE)
    ledger = load(LEDGER)
    targets = active_targets(ledger)
    vocab = recent_vocab()

    lesson_id, lesson_body = next_lesson(state)
    seq_len = len((LESSONS / "SEQUENCE").read_text().split()) if (LESSONS / "SEQUENCE").exists() else 0
    remaining = seq_len - state.get("lesson_index", 0)

    task = args.task or state["task_rotation"][state["task_index"] % len(state["task_rotation"])]
    fluency = state["fluency_topics"][state["fluency_index"] % len(state["fluency_topics"])]
    features = ", ".join(t["feature"] for t in targets) or "ninguno todavía (sesión de diagnóstico: anota todo)"

    text = TEMPLATE.read_text()
    parts = text.split("\n---\n")
    body = parts[1] if len(parts) > 1 else text
    if lesson_body and not args.task:
        rules = body.split("ESTRUCTURA DE LA SESIÓN")[0]
        body = rules + "\n" + lesson_body
    fills = {
        "{LEVEL_ANCHOR}": state["level_anchor"],
        "{LEVEL_EXAMPLE}": state["level_example"],
        "{TARGET_FEATURES}": features,
        "{TARGET_FEATURES_SHORT}": features,
        "{VOCAB_QUIZ}": ", ".join(vocab) or "(aún no hay vocabulario minado — omite esta parte)",
        "{VOCAB_RECIENTE}": ", ".join(vocab) or "(aún no hay vocabulario minado — omite esta parte)",
        "{VOCAB_SHORT}": ", ".join(vocab[:4]) or "(ninguno)",
        "{ERROR_RETRIEVAL}": features,
        "{TASK}": task,
        "{TASK_SHORT}": task.split(":")[0],
        "{FLUENCY_TOPIC}": fluency,
        "{FORM_FOCUS}": state["form_focus"],
        "{SESSION_GOAL}": args.goal or f"completar la tarea ({task.split(':')[0].lower()}) y cazar errores de {features}",
    }
    for k, v in fills.items():
        body = body.replace(k, v)

    hours = state["total_minutes"] / 60
    lesson_note = f" — lección {lesson_id}" if lesson_body and not args.task else " — (generic rotation)"
    print(f"# Session {state['session_counter'] + 1} — {dt.date.today()} — "
          f"phase {state['phase']}{lesson_note} — {hours:.1f}/500 h — week entries: {state['week_entries']}\n")
    print(body.strip())
    print("\n[after the session: run prompts/debrief.md on the transcript, then: "
          "python3 tools/session.py log <debrief.json>]")
    if 0 < remaining <= 2:
        print(f"[WARNING: only {remaining} scripted lesson(s) left — author the next "
              "unit from lessons/p1/unit-maps.md (AGENTS.md workflow 4)]")
    elif lesson_body is None and not args.task:
        print("[WARNING: lesson sequence exhausted — running generic rotation; "
              "author the next unit (AGENTS.md workflow 4)]")


# ---------------------------------------------------------------- log

def extract_json(raw):
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", raw, re.S)
    return json.loads(m.group(1) if m else raw)


def update_streak(state, entry_date):
    wk = iso_week(entry_date)
    last = state["last_logged_week"]
    if last is None:
        state["last_logged_week"] = wk
        state["week_entries"] = 1
        return
    if wk == last:
        state["week_entries"] += 1
        return
    gap = week_index(wk) - week_index(last)
    made_target = state["week_entries"] >= state["weekly_target"]
    missed_weeks = (0 if made_target else 1) + max(0, gap - 1)
    if made_target and gap == 1:
        state["streak_weeks"] += 1
    if missed_weeks:
        if state["repair_tokens"] >= missed_weeks:
            state["repair_tokens"] -= missed_weeks
            state["streak_weeks"] += 1 if made_target else 0
            print(f"  streak: spent {missed_weeks} repair token(s); streak preserved at {state['streak_weeks']}")
        else:
            state["streak_weeks"] = 0
            print("  streak: reset (out of repair tokens) — hours are unaffected, restart per adherence.md")
    state["last_logged_week"] = wk
    state["week_entries"] = 1


def update_ledger(ledger, entry, session_no, date):
    by_id = {e["id"]: e for e in ledger}
    features = {e["feature"]: e for e in ledger}
    for hit in entry.get("targets_hit", []):
        e = by_id.get(hit.get("ledger_id"))
        if not e:
            continue
        for k in ("prompted_correct", "prompted_total", "spontaneous_correct", "spontaneous_total"):
            e[k] += int(hit.get(k, 0))
        e["last_targeted"] = date
        e["history"].append({"date": date, "session": session_no,
                             **{k: int(hit.get(k, 0)) for k in
                                ("prompted_correct", "prompted_total",
                                 "spontaneous_correct", "spontaneous_total")}})
    next_id = max((int(e["id"][1:]) for e in ledger), default=0) + 1
    seen_new = set()
    for err in entry.get("errors", []):
        f = err.get("feature", "other")
        if f in features:
            e = features[f]
            if e["first_seen"] is None:
                e["first_seen"] = date
            if e["example"].startswith("(P0") and err.get("utterance"):
                e["example"] = f"{err['utterance']} -> {err.get('corrected', '?')}"
        elif f not in seen_new:
            seen_new.add(f)
            ledger.append({
                "id": f"E{next_id:03d}", "feature": f, "class": "unclassified",
                "example": f"{err.get('utterance', '')} -> {err.get('corrected', '')}",
                "status": "watch", "first_seen": date, "last_targeted": None,
                "prompted_correct": 0, "prompted_total": 0,
                "spontaneous_correct": 0, "spontaneous_total": 0, "history": [],
            })
            features[f] = ledger[-1]
            next_id += 1


def append_vocab(entry, date):
    rows = entry.get("vocab_mined", [])
    if not rows:
        return
    with INBOX.open("a") as f:
        for v in rows:
            f.write(f"| {date} | {v.get('es', '')} | {v.get('en', '')} | {v.get('context', '')} |\n")
    with TSV.open("a") as f:
        for v in rows:
            f.write(f"{v.get('es', '')}\t{v.get('en', '')}\t{v.get('context', '')}\tmined\n")


def cmd_log(args):
    raw = sys.stdin.read() if args.file == "-" else Path(args.file).read_text()
    entry = extract_json(raw)
    if "minutes" not in entry or "type" not in entry:
        sys.exit("debrief JSON needs at least 'type' and 'minutes'")
    state = load(STATE)
    ledger = load(LEDGER)

    date = entry.get("date") or str(dt.date.today())
    entry["date"] = date
    d = dt.date.fromisoformat(date)
    state["session_counter"] += 1
    n = state["session_counter"]
    entry["session"] = n
    if state["started_date"] is None:
        state["started_date"] = date

    state["total_minutes"] += int(entry["minutes"])
    t = entry["type"]
    state["minutes_by_type"][t] = state["minutes_by_type"].get(t, 0) + int(entry["minutes"])
    if t == "conversation":
        state["sessions_completed"] += 1
        state["task_index"] += 1
        state["fluency_index"] += 1
        state["lesson_index"] = state.get("lesson_index", 0) + 1
    update_streak(state, d)
    update_ledger(ledger, entry, n, date)
    append_vocab(entry, date)

    out = LOGS / f"{n:03d}-{date}.json"
    save(out, entry)
    save(STATE, state)
    save(LEDGER, ledger)
    write_progress(state, ledger)

    h = state["total_minutes"] / 60
    print(f"logged session {n}: {t}, {entry['minutes']} min -> {h:.1f}/500 h "
          f"({h / 5:.1f}%) | streak {state['streak_weeks']}w, tokens {state['repair_tokens']}")
    print(f"  {out.relative_to(ROOT)}")
    if args.commit:
        subprocess.run(["git", "-C", str(ROOT), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(ROOT), "commit", "-m",
                        f"Log session {n}: {t} {entry['minutes']}min ({h:.1f}h total)"], check=True)
        print("  committed")


# ---------------------------------------------------------------- stats

def acc(c, t):
    return f"{100 * c / t:.0f}%" if t else "—"


def write_progress(state, ledger):
    h = state["total_minutes"] / 60
    lines = [
        "# Progress",
        "",
        f"**{h:.1f} / 500 hours** ({h / 5:.1f}%) · {state['sessions_completed']} conversation sessions · "
        f"phase {state['phase']} · streak {state['streak_weeks']}w (tokens: {state['repair_tokens']})",
        "",
    ]
    logs = sorted(LOGS.glob("*.json"))
    if logs:
        recent = [load(p) for p in logs[-10:]]
        cutoff = dt.date.today() - dt.timedelta(days=56)
        recent_min = sum(int(load(p)["minutes"]) for p in logs
                         if dt.date.fromisoformat(load(p)["date"]) >= cutoff)
        pace = recent_min / 60 / 8
        lines.append(f"Trailing 8-week pace: **{pace:.1f} h/week**")
        if pace > 0:
            weeks_left = (500 - h) / pace
            eta = dt.date.today() + dt.timedelta(weeks=weeks_left)
            lines.append(f" · projected finish at this pace: **{eta.strftime('%b %Y')}**")
        lines.append("")
        funs = [e["fun"] for e in recent if isinstance(e.get("fun"), (int, float))]
        if funs:
            lines.append(f"Fun (last {len(funs)} logged): {sum(funs) / len(funs):.1f}/5")
            lines.append("")
    lines += ["## Hours by type", ""]
    for t, m in sorted(state["minutes_by_type"].items(), key=lambda kv: -kv[1]):
        lines.append(f"- {t}: {m / 60:.1f} h")
    lines += ["", "## Error ledger", "",
              "| id | feature | class | status | prompted | spontaneous | last targeted |",
              "|---|---|---|---|---|---|---|"]
    for e in ledger:
        lines.append(f"| {e['id']} | {e['feature']} | {e['class']} | {e['status']} | "
                     f"{acc(e['prompted_correct'], e['prompted_total'])} "
                     f"({e['prompted_total']}) | "
                     f"{acc(e['spontaneous_correct'], e['spontaneous_total'])} "
                     f"({e['spontaneous_total']}) | {e['last_targeted'] or '—'} |")
    if logs:
        lines += ["", "## Errors by feature (last 10 logs)", ""]
        counts = {}
        for e in recent:
            for err in e.get("errors", []):
                counts[err.get("feature", "other")] = counts.get(err.get("feature", "other"), 0) + 1
        for f, c in sorted(counts.items(), key=lambda kv: -kv[1]):
            lines.append(f"- {f}: {c}")
    PROGRESS.write_text("\n".join(lines) + "\n")


def cmd_stats(args):
    write_progress(load(STATE), load(LEDGER))
    print(PROGRESS.read_text())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("start")
    s.add_argument("--task")
    s.add_argument("--goal")
    s.set_defaults(fn=cmd_start)
    l = sub.add_parser("log")
    l.add_argument("file", help="debrief JSON file, or - for stdin")
    l.add_argument("--commit", action="store_true")
    l.set_defaults(fn=cmd_log)
    st = sub.add_parser("stats")
    st.set_defaults(fn=cmd_stats)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
