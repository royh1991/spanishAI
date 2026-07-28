# The 500-Hour Plan (v1)

Locked decisions (2026-07-28):

| Decision | Choice |
|---|---|
| Target variety | **Mexican Spanish** (materials, AI persona instructions, Azure es-MX) |
| Weekly budget | **3 scheduled hours/week** + one recommended micro-habit (Anki ~10 min/day) |
| ChatGPT tier | **Plus** (~1 hr GPT-Live-1 per rolling 24 h — enough, since no day needs >1 voice hour) |
| Human hours | **None** (see §8 Risk register — this has consequences) |
| External stakes | **Official ACTFL OPIc at hours ~0 / ~250 / ~500** (decided for you, §1.2). No deposit contract. |
| Reporting | None — GitHub is the system of record |
| Tooling | **Automated session logs** (`tools/session.py`) |
| Goal | **ACTFL Advanced Mid speaking (≈ B2+) at 500 hours**, verified by the final OPIc; maintenance mode after |

## 1. The honest math

### 1.1 Timeline

- 3 scheduled hr/week → 500 hours ≈ **3.2 years**.
- With the Anki micro-habit (~10 min/day ≈ 1.1 hr/week, logged) → ~4.1 hr/week ≈ **2.4 years**.
- Realistic planning number, allowing lapses and deload weeks: **~2.5–3 years.**

Two blunt research notes, so the plan's own evidence base isn't ignored:

1. **3 hr/week is below the ~4–5 hr/week density floor** associated with consistent
   gains in adult programs. The plan compensates by (a) never letting conversation
   frequency drop below 2 sessions/week (proceduralization needs short lags — this
   is the one non-negotiable), (b) keeping hours concentrated in 1-hour blocks
   rather than scattered, and (c) the Anki micro-habit, which is the cheapest way
   to get back over the floor. If progress stalls, **the first lever is one more
   weekly hour, not a method change.**
2. The main threat over 2.5–3 years is not learning rate — it's **attrition**.
   That's why the headline metric is cumulative hours (unbreakable), the streak is
   weekly with repair tokens, and the lapse-restart script exists before it's
   needed (`state/adherence.md`).

### 1.2 Why the OPIc is booked anyway (decision #5, made for you)

"External stakes" = paying for a real, human-rated proficiency test on a fixed
date. FSI/DLI deliberately use high-stakes testing as a motivation and washback
engine, and it's the only rater-drift-proof calibration for the home-grown
assessments. With **zero human conversation hours**, the OPIc is also the *only
time a human ever hears your Spanish* — it becomes the transfer test for the
whole AI-only bet. Three tests (~$75–100 each via Language Testing International,
purchasable by individuals): baseline in month 1, midpoint at ~hour 250, final at
~hour 500. The deposit-contract idea (staking money on Beeminder/stickK) is
skipped: evidence says it works for people who self-select into it, and "idk what
this is" is not self-selection.

## 2. The weekly rhythm

Three 1-hour blocks + one micro-habit. Default slots get written into
`state/adherence.md` as if-then plans, with fallbacks.

| Block | What | Composition |
|---|---|---|
| **Session A** (e.g., Tue) | AI conversation | 45 min GPT-Live-1 voice + 15 min transcript debrief in text mode (`prompts/debrief.md`) |
| **Session B** (e.g., Sat) | AI conversation | Same structure, different task type |
| **Studio** (e.g., Sun) | Everything else | Rotates on a 4-week cycle (below) |
| **Micro-habit** (daily) | Anki, 10 min | FSRS on, retention 0.85–0.90, ~5–7 new cards/day from mined vocab |

Studio 4-week rotation:

- **Week 1 — Writing workshop:** 30 min writing on the current grammar targets +
  staged LLM feedback (`prompts/writing-feedback.md`); 20 min listening decode
  (micro-dictation of 30–60 s native Mexican audio); 10 min ledger/plan review.
- **Week 2 — Ear training:** 30 min micro-dictations + connected-speech work
  (resyllabification, 'pa'/'ps' reductions); 20 min grammar mini-cycle on one
  ledger family; 10 min review.
- **Week 3 — Writing workshop** (as week 1, other error family) + 20 min solo
  4/3/2 re-recording of a monologue; 10 min review.
- **Week 4 — Monthly benchmark:** 2 recorded timed monologues from the fixed
  prompt bank → rated later in a separate text session (`prompts/monologue-rating.md`);
  Can-Do spot-check; ledger triage (promote/retire targets); log everything.

Bonus hours (podcast on a commute, graded reader on a flight, extra session)
always count — log them. They only ever shorten the calendar.

### The conversation session template (45 min voice)

Generated per-session by `tools/session.py start` from the state files:

1. **Warm-up + retrieval quiz** (5–8 min) — AI cold-quizzes recent mined vocab and
   one prior error target, in Spanish.
2. **Task block** (~20 min) — one communicative task with an outcome (rotation in
   §4 per phase): teach-a-topic, roleplay-with-complication, narration,
   negotiation, interview, multiparty simulation. Never open-ended chat.
3. **Fluency block** (~8 min) — 4/3/2: same mini-monologue three times with
   shrinking time; feedback on accuracy between retellings.
4. **Focus-on-form** (~8 min) — communicative drills on 1–2 active ledger targets;
   AI must *prompt self-repair*, not supply the form.
5. **Wrap** (min ~40) — spoken self-eval against the session goal; end before the
   cap kills the session.

Correction protocol (in every header): prompt-first on ledger targets; salient
explicit recast ("Ojo: se dice…") for new errors; let flow-critical moments go and
catch them in the debrief; minimum-correction quota; no unearned praise; Mexican
variety pinned; Spanish-only with the single escape phrase *"¿Puedo decirlo en
inglés?"*; reset command *"En español, por favor"* for English drift; re-anchor
level and protocol at every block transition (counters level drift).

## 3. Phases (by cumulative logged hours)

### P0 — Baseline & shakedown (hours 0–8, ~2–3 weeks)

- **Canary-test GPT-Live-1** (`prompts/canary-tests.md`): does the Project reach
  voice? does the correction protocol actually fire? planted mispronunciations?
  drift timing? Adjust the header template based on results.
- **Baseline battery** (`state/assessments/`): Spanish EIT (Ortega 30-item),
  simulated OPI (`prompts/opi-simulation.md`), 2 recorded monologues, writing
  sample, Can-Do inventory, vocab diagnostic sweep over Davies top-3k (batch
  yes/no + translation spot-checks) → partition known / dormant / unknown.
- **Error census:** first conversation sessions are diagnostic; every error into
  the ledger with a feature tag and acquisition class (treatable / late-variable /
  interface-persistent).
- **Book OPIc #1.**
- Exit: state files populated, header template tuned, working level estimate
  replaces the B1+ guess.

### P1 — Reactivation (hours 8–75, ~5–7 months)

The savings-effect phase: force production of what's dormant, don't re-teach.

- Session A tasks: narrations of your own history/life in past tenses; teach-a-topic
  on familiar subjects; travel-Mexico roleplays *with complications* (the thing
  travel never gave you).
- Session B tasks: personalized functional scripts built, varied, and outgrown
  (MTC-style: self-intro, your Spanish history, opinions frame, past-narration
  frame — `state/scripts.md`).
- Grammar campaign (focused cycles, 2–4 weeks each, writing workshop + form block
  aligned): **ser/estar** (kill ser-overuse), **preterite/imperfect forms**,
  gender/number agreement, clitic placement. Log everything; drill nothing that
  isn't in the ledger.
- Anki: dormant-word blitz from the P0 diagnostic (reactivations are cheap wins),
  then steady mined-vocab flow.
- Listening: Dreaming Spanish intermediate/advanced + No Hay Tos with transcript
  support; decode training starts immediately (it's the weakest skill vs. need).
- Exit criteria: comfortable 3-minute spontaneous past-tense narration; ser/estar
  and agreement error rates halved from baseline in spontaneous speech; EIT retest
  bump; conversation feels like *retrieval*, not translation.

### P2 — Systematic rebuild (hours 75–250, ~1–1.3 years)

The grammar-heavy middle. Also where the **plateau will hit** (subjective stall
likely in the months around hours 120–200) — the counter-plan is pre-scheduled:
metrics switch emphasis to per-error trends and speech-rate numbers
(`PROGRESS.md` makes small gains visible), plus a program refresh at ~hour 150
(new task types, new materials, framed as a checkpoint).

- Grammar campaign continues: **imperfect discourse use front-loaded**
  (foreground/background narrative contrast — the hard half of pret/imp);
  clitic combinations (se lo); subordinate-clause fluency (que-clauses,
  connectors) as the **gate for the subjunctive strand**, which opens mid-phase:
  volition + high-frequency triggers first, processing-instruction style
  ("you tend to ignore the mood ending"), expectations set for a multi-month grind.
- Session tasks: information-gap and negotiation tasks; AI feigns
  non-understanding (engineered breakdowns); topic rotation begins (work, tech,
  food, family, news).
- Listening: No Hay Tos without transcript first-pass; Mexican Netflix with ES
  captions + caption-free second passes; 0.8x scaffold on new material only.
- Writing: weekly workshop cycles locked to the active grammar family; error
  rates per 100 words tracked on *new* texts.
- Midpoint battery at ~hour 250: **OPIc #2** + EIT + full benchmark. This is the
  **go/no-go gate**: if OPIc shows Intermediate High or better, the AI-only
  approach is working; if it shows a big gap between AI-session comfort and rated
  proficiency, revisit the no-human-hours decision (§8).
- Exit criteria: paragraph-length discourse with connected past narration;
  subjunctive appearing (imperfectly) in spontaneous speech; Intermediate
  High / Advanced Low on OPIc #2.

### P3 — Expansion (hours 250–400, ~1 year)

- Domain rotation is the point (the anti-"mission Spanish" move): politics,
  health, humor, opinion, service complaints, storytelling for laughs. New
  domains keep sessions fun — which the adherence research says is load-bearing.
- Multiparty simulation: AI runs 2–3 distinct characters with interruptions and
  topic shifts (FSI's "hardest skill" — and with no human hours, the only
  available approximation).
- Native-rate everything: Radio Ambulante, Mexican TV without captions, YouTube.
- Grammar: subjunctive expansion (emotion/doubt/adjectival/adverbial), si-clause
  hypotheticals, imperfect subjunctive; ledger triage retires mastered targets
  and accepts variability on interface features (por/para nuance, subject
  pragmatics) per the defossilization evidence.
- Monthly Spanish-only half-days (DLI-style immersion punctuation, solo:
  media + self-talk + journaling + session).
- Exit criteria: sustained Advanced-level performance in simulated OPIs (narrate
  across time frames, handle complications, paragraph discourse).

### P4 — Polish & push (hours 400–500, ~7–9 months)

- Superior-function *probes* (supported opinion, hypothesis, abstraction) as
  stretch material — not the target, but they pull Advanced Mid upward.
- Accent comprehensibility block: Azure PA (es-MX) benchmarks, shadowing sprints,
  the four problem areas (tap/trill, [β ð ɣ], unaspirated /p t k/, unreduced
  vowels).
- Timed-pressure tasks, fast topic-switching, long-form storytelling.
- **OPIc #3 at ~hour 500 = the verdict.**
- Build the maintenance design before finishing (§7).

## 4. Task-type rotation (Session A/B menus)

Teach-a-topic · roleplay-with-complication · past narration (foreground/background)
· information gap · negotiation/persuasion · interview (you interview the AI, then
reversed) · picture/scene description · multiparty simulation (P3+) · debate (P3+)
· "explain like I'm five" register-shifting (P3+) · simulated OPI (quarterly).

Each task ends with an outcome the AI checks (a decision, a summary, a ranked
list) — tasks without outcomes degrade into chat.

## 5. Materials ladder (Mexican-first)

- **Listening:** Dreaming Spanish (int/adv) → No Hay Tos (Mexican, transcripts)
  → How to Spanish (Mexican) → Radio Ambulante (pan-LatAm) → Mexican Netflix
  (Club de Cuervos, Control Z, etc.) → unassisted native media/YouTube.
- **Reading (bonus strand):** Paco Ardit LatAm graded readers (B1→B2) / Olly
  Richards Short Stories → Mexican news (El Universal, Animal Político) →
  fiction. ~98% known-word coverage rule for comfort.
- **Vocab spine:** Davies frequency list (top 5k lemmas), free download —
  the diagnostic and tracking backbone in `state/vocab/`.
- **Pronunciation:** Azure Speech Studio Pronunciation Assessment (es-MX);
  native audio for shadowing from the podcast ladder.

## 6. Assessment calendar

| Cadence | Instrument | Where it lands |
|---|---|---|
| Every session | Debrief JSON: errors by feature, target hit-rates, mined vocab, fun rating | `state/session-logs/` via `tools/session.py log` |
| Monthly (studio wk 4) | 2 recorded monologues (fixed prompt bank), rated in a *separate* text session against pasted ACTFL descriptors + calibration exemplars; writing sample error counts | `state/assessments/` |
| Quarterly | Simulated OPI; Azure PA benchmark; blind re-rate of one old recording (drift check); Can-Do inventory | `state/assessments/` |
| Hours ~0 / 250 / 500 | **Official OPIc** + Spanish EIT (parallel forms) | ground truth |

Rules: the conversation model never rates its own conversation; transcripts are
ground truth over live impressions (and even transcripts get spot-checked against
audio for ASR normalization); single ratings are ±1 sublevel noise; per-error
prompted vs. spontaneous accuracy tracked separately (spontaneous is the real
test; backsliding under load is expected, not failure).

## 7. After hour 500: maintenance

Advanced Mid is **below** FSI's self-maintaining threshold — parked skills at
this level decay. Standing design: 1 conversation session + ~1 hr native input
per week, Anki maintenance load (no new cards required), and Spanish media
defaulting into normal leisure. Revisit a Superior push only if OPIc #3 lands at
Advanced High and life allows a density increase.

## 8. Risk register

| Risk | Mitigation |
|---|---|
| **Attrition** (the big one at 3 hr/wk × 3 yrs) | Cumulative-hours headline metric; weekly streak w/ repair tokens; lapse-restart script pre-written; fun tracked as KPI; plateau counter-plan at P2; automation reduces friction |
| Below-density-floor progress | ≥2 conversation sessions/wk non-negotiable; Anki micro-habit; "add an hour" is the first lever |
| **No human hours** → transfer to real speakers unknown | OPIc #2 at hour 250 is an explicit go/no-go gate on the AI-only bet; multiparty simulation + native-rate media partially compensate; decision revisited on evidence, not dogma |
| AI under-correction (sycophancy) | Prompt-first protocol w/ correction quota; planted-error audits monthly; transcript mining catches what live sessions miss |
| ASR blindness / false corrections | Writing workshop is the accuracy channel; suspicious corrections flagged in debrief; audio spot-checks |
| Level/language drift in voice | Block-transition re-anchoring; reset phrase; header restated each session |
| GPT-Live-1 caps/behavior change | Only 1 voice hr/day needed (Plus suffices); fallbacks: GPT-Live-1 mini for low-stakes blocks, Gemini Live as alternate partner; re-run canary tests quarterly |
| Fossilized-error stubbornness | Ledger triage: reallocate to targets that move, accept variability on interface features |
| Motivation loss at plateau | Pre-scheduled refresh ~hour 150; fine-grained metrics keep progress visible |

## 9. Operating the system

```
# before a session
python3 tools/session.py start            # prints the session header to paste/read

# after a session: run prompts/debrief.md in text mode on the transcript,
# save the JSON block it outputs, then
python3 tools/session.py log debrief.json # appends log, updates hours/streak/ledger/vocab

# any time
python3 tools/session.py stats            # regenerates PROGRESS.md
```

Everything the tools maintain lives in `state/`. Commit after logging — GitHub
is the system of record and the only reporting channel.
