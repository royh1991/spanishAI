# Quickstart: one session, end to end

## What you need open

1. A terminal in this repo (or Codex/Claude Code opened in it — recommended)
2. ChatGPT (the "Spanish" Project)
3. A timer

## The session (≈75 min total)

### 1. Get the briefing (1 min)

```
python3 tools/session.py start
```

Copy everything it prints. It's today's lesson: the tutor's rules + the full
script (warm-up quiz on what you missed last time, today's roleplay, drills).

### 2. Do the lesson (45 min)

- ChatGPT → new **voice** chat inside the Spanish Project → paste (or read)
  the briefing.
- Start your timer. The lesson has 5 timed blocks; when a block's time is up,
  say **"siguiente bloque"**. At minute ~40 say **"cierre"**.
- Rules the tutor is following: Spanish only (escape hatch: "¿Puedo decirlo en
  inglés?"), it makes you self-correct on your target errors, it won't invent
  content beyond the script. If it drifts to English: **"En español, por
  favor."**

### 3. Get your feedback (10-15 min)

When the voice chat ends, ChatGPT keeps the **transcript** in that chat's
history. Copy it. Then either:

- **Agent route (recommended):** in Codex/Claude Code say *"log this
  session"* and paste the transcript. It analyzes the transcript, shows you
  your feedback report (errors + fixes, target-grammar score, vocab worth
  keeping, "you said X → a native says Y"), and logs everything.
- **Manual route:** new **text** chat → paste `prompts/debrief.md` + the
  transcript. Its reply is your feedback report. Save the JSON block at the
  end to a file and run:
  ```
  python3 tools/session.py log debrief.json --commit
  ```

Either way, logging is what closes the loop: errors → ledger, vocab → Anki
queue (`state/vocab/anki-import.tsv` — import into Anki), minutes → your 500,
and the NEXT session's warm-up will quiz exactly what you missed today.

### 4. Check progress (any time)

```
python3 tools/session.py stats     # regenerates PROGRESS.md
```

## The week

- 2 × the loop above (conversation sessions — the lesson sequence advances
  automatically)
- 1 × studio hour: open `lessons/studio/rotation.md`, find the current week
  type (1-4), follow the steps
- Daily: ~10 min Anki

## First week ever?

Do `state/curriculum-state.md`'s P0 checklist first — ChatGPT Project setup,
the canary tests in `prompts/canary-tests.md`, baseline recordings, book the
OPIc. The first two lessons in the sequence are diagnostics designed for this.
