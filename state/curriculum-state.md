# Curriculum state

**Phase: P0 — Baseline & shakedown** (hours 0–8)

Machine-readable counters live in `state.json`; this file is the human view of
where we are and what's next. The session tool reads `state.json`; agents should
update BOTH when the phase advances.

## P0 checklist

- [ ] Create ChatGPT Project "Spanish": tutor protocol as project instructions,
      upload `learner-profile.md`
- [ ] Run canary tests 1–7 (`prompts/canary-tests.md`) → record results in
      `assessments/canary-results.md`; tune the session header accordingly
- [ ] Book OPIc #1 (Language Testing International) for ~1 month out
- [ ] Baseline battery → `assessments/baseline/`:
  - [ ] 2 recorded monologues (prompts 1 and 2 from the bank)
  - [ ] Simulated OPI (`prompts/opi-simulation.md`), recorded
  - [ ] Writing sample (250 words, past narrative) + error counts
  - [ ] Spanish EIT if practical (Ortega et al. 30-item; else defer to hour 250)
  - [ ] Vocab diagnostic sweep over Davies top-3k (see `vocab/README.md`)
- [ ] First 2–3 conversation sessions are diagnostic: error census → confirm or
      amend the six seeded ledger entries; set `first_seen`, real examples, and
      promote confirmed ones from `watch` → `active`
- [ ] Set Anki up with FSRS (desired retention 0.85–0.90), seed with dormant
      words from the diagnostic
- [ ] Fill in the if-then plan slots in `adherence.md`
- [ ] Update `learner-profile.md` level table with measured results
- [ ] Advance phase → P1 (edit `state.json` "phase", refresh `task_rotation`
      toward P1 menus, set `form_focus` to first campaign target)

## Active grammar campaign

P0: none — census first. First P1 campaign: **ser/estar** (2–4 weeks), then
**preterite/imperfect forms**, then agreement, then clitic placement.

## Notes

- Subjunctive strand stays closed until subordinate-clause fluency is reliable
  (mid-P2 expected).
- The plateau counter-plan (metrics granularity + program refresh) is scheduled
  around hours 120–200; see `docs/PLAN.md` §3-P2.
