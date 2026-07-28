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

## Why 45 minutes fits (timing budget)

A lesson file looks short because it is only the tutor's half — the learner's
speech is the content, and by design the learner should hold most of the talk
time (tutor turns are capped at 30 s by protocol rule 4). The budget:

| Block | Min | Why it fills |
|---|---|---|
| Warm-up quiz | ~6 | 7-9 produce-on-demand vocab items + retrieval Qs ≈ 40 s each |
| Task | ~20 | 4-5 beats of multi-turn exchange ≈ 4 min each; rule 7 forbids filler and forces depth-probing instead |
| 4/3/2 | ~9 | mechanically timed: 4+3+2 min + transitions |
| Drills | ~9 | 10 questions × ~50 s (answer → prompt → self-repair) |
| Cierre | ~2-3 | scripted self-eval |

If a block runs dry anyway, the tutor goes to the lesson's scripted
**Extensión** — never invents content (protocol rule 7).

## Research map (why lessons are shaped this way)

| Lesson component | Evidence (see docs/research/) |
|---|---|
| Cold retrieval warm-up quizzing the PREVIOUS lesson's vocab | Testing effect g≈0.6 (Adesope 2017); day-plus delay before first retrieval improves durability; substitutes for the model's missing memory |
| Vocab introduced inside tasks, mined into Anki afterward | Involvement-load "need + evaluation" are the strongest retention levers (Yanagisawa & Webb 2021); pushed output beats input-only for productive vocab (de la Fuente 2002) |
| Tasks with beats, a complication, and a concrete checked outcome | Interaction/negotiation-of-meaning meta-analyses (Keck 2006; Mackey & Goo 2007); TBLT (Bryfonski & McKay 2019); engineered breakdowns because an accommodating AI under-supplies them |
| Tutor talk capped; learner min-output rule | Skill-specificity: production practice automatizes production (DeKeyser 1997); Swain's output hypothesis |
| 4/3/2 blocks, topics deliberately repeated across a unit | Repetition under time pressure proceduralizes and transfers (de Jong & Perfetti 2011); accuracy note between rounds patches the technique's known blind spot (Boers 2014) |
| Drill questions where MEANING forces the form (never mechanical substitution) | FSI retains only communicative pattern practice; mechanical drills condemned (Wong & VanPatten 2003); deliberate practice (DeKeyser) |
| Prompt-first correction; recasts only for new material; salient flagging | Prompts d≈0.83 vs recasts d≈0.53 (Lyster & Saito 2010); audio-only recasts go unnoticed |
| Unit exams scored silently in FREE production, with exit criteria | The explicit-instruction advantage is inflated by drill-aligned tests (Norris & Ortega artifact); measure in spontaneous speech |
| Delayed surprise retells (don Chucho returns in lesson 12) | Immediate performance overstates learning; delayed testing is the honest measure |
| Recurring personas with saved state | MTC "progressing investigator" role-plays; cumulative interlocutors without model memory |
| Spanish-only with a formal escape phrase + "words I lacked" harvest | MTC SYL protocol (all five rules) |
| Grammar sequence: ser/estar → pret/imp → agreement → clitics → por/para; subjunctive deferred to P2 | Acquisition-order research: VanPatten's ser/estar stages; forms-precede-use and the hard imperfect (Rothman et al.); subjunctive gated on subordinate-clause ability (Collentine); treatable-features-first triage from the defossilization literature |
| Diagnostics with correction OFF; exams with correction OFF | Separate measurement from treatment; error census seeds the ledger before targets are chosen |

## Current inventory

- `p0/` — 2 diagnostic sessions (correction quota off; they exist to fill the
  error ledger)
- `p1/` — Units 1–2 fully scripted (ser/estar 01–06, preterite/imperfect
  07–12); Units 3–5 specified lesson-by-lesson in `p1/unit-maps.md`
  (agreement → clitics → por/para + exit exam)
- `studio/rotation.md` — the 4-week studio hour, fully scripted
