# Operating manual for coding agents (Codex, Claude Code, etc.)

This repo is the brain of a self-directed Spanish program. The voice tutor
(GPT-Live-1 in ChatGPT) is stateless; all curriculum state lives here. Your job
as the desktop agent is to run the loop around each session: generate headers,
analyze transcripts, update state, commit.

## The three workflows

### 1. "Start a session" / "dame el header"

Run `python3 tools/session.py start` and show the output for the user to paste
into a fresh GPT-Live-1 voice chat. Optional: `--task "..."` to override the
rotation, `--goal "..."` for a custom session goal.

### 2. "Log this session" (user pastes or points you at a transcript)

You do the analysis yourself — no separate ChatGPT step needed:

1. Read `prompts/debrief.md`. Perform that exact analysis on the transcript,
   as the severe error analyst it describes (Mexican Spanish is the target).
   Fill `{ACTIVE_TARGETS}` from `state/error-ledger.json` (status `active`,
   falling back to `watch`).
2. Ask the user for the `fun` rating (1-5) and minutes if not stated; if you
   can't ask, default minutes to 60 and fun to null.
3. Write the JSON (schema at the bottom of `prompts/debrief.md`) to a temp file
   and run `python3 tools/session.py log <file> --commit`.
4. Report back: hours total, streak state, top recurring error, and the
   `next_focus` line.

Studio work (writing scorecards, monologue ratings, assessments) logs the same
way — those prompts also end in loggable JSON; `type` must be one of
`conversation | studio | anki | listening | reading | assessment`. Weekly Anki
time gets logged as one entry (`{"type": "anki", "minutes": 70}` or whatever
the week's total was).

### 3. Periodic maintenance (monthly/quarterly, or when asked)

- Monthly: help run the benchmark (prompts/monologue-rating.md), triage the
  error ledger (promote `watch`→`active` when confirmed, `active`→`retired`
  when spontaneous accuracy stays high, reclassify `unclassified` features),
  and prune `state/vocab/anki-import.tsv` rows the user has imported.
- Quarterly: simulated OPI (prompts/opi-simulation.md), refill 1 repair token
  in `state/state.json` (max 2) as part of the review, re-run the canary tests
  (prompts/canary-tests.md), rotate `task_rotation`/`fluency_topics` in
  `state/state.json` to match the current phase in `docs/PLAN.md`.
- Phase transitions: update `state/state.json` (`phase`, `form_focus`,
  rotations, `level_anchor`/`level_example` as the level rises) AND
  `state/curriculum-state.md` together.

### 4. "Author the next lesson unit"

Lessons are fully scripted in `lessons/` — ChatGPT executes them, it never
designs them. When `session.py start` warns that ≤2 scripted lessons remain
(or the user asks):

1. Read `lessons/README.md` (format), the next unit's spec in
   `lessons/p1/unit-maps.md` (or the next phase's outline in `docs/PLAN.md`),
   `state/error-ledger.json`, and the last few session logs.
2. Write the unit's 6 lesson files following the existing files' anatomy
   exactly (verbatim drill questions, task beats with a complication and a
   concrete outcome, 6-9 Mexican vocab items the tutor uses naturally, warm-up
   quizzing the PREVIOUS lesson's vocab). Weight drills toward ledger features
   that are actually failing; reuse personas and their state.
3. Append the new ids to `lessons/SEQUENCE`, update persona state if the unit
   advances their story, commit.

## Rules

- **Never fabricate transcript content.** Analyze only what's actually there;
  flag suspected ASR mishearings (`suspect_asr`) instead of guessing.
- **Be severe in analysis, honest in reporting.** No unearned praise; error
  counts are lower bounds (ASR normalizes learner errors).
- `state/state.json` and `state/error-ledger.json` are owned by
  `tools/session.py` during logging — edit them directly only for curation
  (triage, phase changes, token refills), not to record sessions.
- `prompts/` and `docs/` are stable artifacts — change them only when the user
  asks or a canary test result demands it (record why in the commit message).
- Commit after every logging or curation action; GitHub is the only reporting
  channel. `--commit` on the log command handles the routine case.
- The research base lives in `docs/research/`; when the user asks "why is the
  program like this," answer from there, not from vibes.

## Map

| Path | What |
|---|---|
| `docs/PLAN.md` | The 500-hour plan: phases, weekly rhythm, task menus, assessment calendar |
| `docs/BRAINSTORM.md` | Design rationale + research synthesis |
| `docs/research/` | Nine sourced research streams + adversarial critique |
| `prompts/` | Session header template, debrief, OPI sim, monologue rating, writing workshop, canary tests |
| `state/` | All curriculum state (see files' own headers) |
| `tools/session.py` | start / log / stats |
| `PROGRESS.md` | Auto-generated dashboard (`session.py stats`) |
