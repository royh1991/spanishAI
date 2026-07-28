# Lessons

Fully-scripted session content. The principle: **ChatGPT executes, it never
designs.** Every conversation session runs a lesson file from this directory;
the tutor's creativity is confined to playing its role inside the script.

## How it works

- `SEQUENCE` lists lesson ids in order. `tools/session.py start` prints the
  protocol rules + the next lesson; logging a conversation session advances the
  pointer (`lesson_index` in `state/state.json`).
- Lesson files are written TO the tutor (Spanish, imperative): exact warm-up
  items, exact task beats and complications, exact drill questions to ask
  verbatim, exact closing questions.
- `{VOCAB_RECIENTE}` in a lesson is filled by the tool with recently mined
  vocabulary; `{TARGET_FEATURES}` with active error-ledger targets.

## Anatomy of a lesson

1. Title + session goal (+ any rule overrides, e.g. diagnostics disable the
   correction quota)
2. Calentamiento — scripted retrieval quiz (prior vocab + error targets)
3. Tarea — scenario script: tutor's role, opening line, ordered beats, the
   complication, the required concrete outcome
4. Fluidez 4/3/2 — fixed topic
5. Foco gramatical — 8–10 verbatim communicative drill questions (answers must
   *require* the target structure)
6. Cierre — 2 scripted self-evaluation questions
7. Vocabulario nuevo — the lesson's 6–8 items (Mexican usage), which the NEXT
   lesson's warm-up quizzes

## Authoring the next unit (desktop agent job, never ChatGPT's)

When `SEQUENCE` has ≤2 unplayed lessons: write the next unit (6 lessons) from
`p1/unit-maps.md` (or the next phase's map in `docs/PLAN.md`), consulting
`state/error-ledger.json` and recent session logs to weight the drills toward
what's actually failing. Follow the existing files' format exactly. Append ids
to `SEQUENCE`. Commit. See AGENTS.md workflow 4.

## Current inventory

- `p0/` — 2 diagnostic sessions (correction quota off; they exist to fill the
  error ledger)
- `p1/` — Unit 1 fully scripted (ser/estar, 6 lessons); Units 2–5 specified
  lesson-by-lesson in `p1/unit-maps.md` (preterite/imperfect → agreement →
  clitics → por/para + exit exam)
- `studio/rotation.md` — the 4-week studio hour, fully scripted
