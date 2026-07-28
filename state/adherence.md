# Adherence system

The research is blunt: attrition, not method, is how 3-year self-directed plans
die. This file is the pre-commitment layer. The headline metric is **cumulative
hours toward 500** — it can never be "broken." The streak is weekly and
repairable. Lapses are expected events with a scripted restart.

## If-then plans (fill in real slots, keep the fallbacks)

- Session A: If it is ______ at ______, I start a conversation session.
  - Fallback: if I miss the slot, then a 30-minute session after dinner counts.
- Session B: If it is ______ at ______, I start a conversation session.
  - Fallback: same-day 30-minute fallback, or swap with Studio day.
- Studio: If it is ______ at ______, I do the studio hour.
  - Fallback: split into 2×30 min across the next two days.
- Anki: attached to an existing daily anchor: right after ______ (e.g., morning
  coffee), 10 minutes.
- If a session gets cut short, I log the minutes I actually did. Partial always
  beats zero, and it still counts toward the week.

## Weekly streak rules (enforced by tools/session.py)

- Target: 3 logged entries/week (any type — a 30-min fallback counts).
- Miss a week's target → a repair token is spent automatically (start with 2).
- No tokens left → streak resets to 0. Nothing else resets: hours are forever.
- Token refill: +1 token (max 2) at each quarterly benchmark, by hand, as part
  of the review — not before.

## Lapse restart script (read this instead of feeling guilty)

The most persistent adult learners pause MORE but restart FASTER. A lapse of
any length costs only the hours not logged — there is no make-up debt.

1. Restart on the next Monday (or the 1st), whichever comes first.
2. First week back is a comeback week: two 30-minute conversation sessions,
   nothing else required. Log them; they count.
3. Do not redesign the program during a comeback week. No new apps, no new
   methods. The system is fine; just re-enter it.
4. If the lapse was >6 weeks: rerun one monologue benchmark first — expect less
   decay than feared (that's what the savings literature says), and let the
   result, not the guilt, set the re-entry level.

## Deload

1 planned light week per quarter (one conversation session + Anki only), taken
BEFORE burnout argues for it. It is a checkpoint, not a fresh start, and it does
not spend a token (log ≥1 entry).

## Fun is a KPI

Every debrief logs `fun` 1–5. If any activity format averages ≤2.5 over a month,
kill or replace that format at the next monthly review. Boring-but-optimal loses
to fun-but-good-enough over a 3-year horizon.
