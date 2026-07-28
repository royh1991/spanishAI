# spanishAI

A self-directed, evidence-based **500-hour** Spanish program targeting **ACTFL
Advanced Mid speaking in Mexican Spanish**, built around 2 weekly ~1-hour
conversation sessions with ChatGPT's GPT-Live-1 voice model plus 1 studio hour
and a daily Anki micro-habit (~3-4 h/week ≈ 2.5-3 years).

GPT-Live-1 has no API and every voice session starts fresh, so **this repo is
the brain**: curriculum state, error ledger, vocab pipeline, assessments, and
progress tracking all live here. A desktop coding agent (Codex / Claude Code)
opened in this repo runs the loop around each session — see `AGENTS.md`.

## The loop

```
python3 tools/session.py start     # 1. generate today's session header
                                   # 2. paste into a fresh GPT-Live-1 voice chat,
                                   #    do the 45-min session (you drive block
                                   #    transitions: "siguiente bloque")
                                   # 3. copy the transcript, tell your agent:
                                   #    "log this session"  (or run
                                   #    prompts/debrief.md in ChatGPT text mode
                                   #    yourself and:)
python3 tools/session.py log debrief.json --commit
python3 tools/session.py stats     # regenerate PROGRESS.md any time
```

## Getting started (P0 checklist)

`state/curriculum-state.md` has the full checklist: create the ChatGPT Project,
run the canary tests (`prompts/canary-tests.md`), do the baseline battery, book
OPIc #1, set up Anki+FSRS, fill in the if-then slots in `state/adherence.md`.

## Layout

- `docs/PLAN.md` — the plan: honest timeline math, weekly rhythm, phases P0-P4,
  task menus, materials ladder (Mexican-first), assessment calendar, risk register
- `docs/BRAINSTORM.md` — research synthesis and design rationale
- `docs/research/` — nine sourced research streams (SLA evidence, FSI/DLI, the
  Mormon MTC, vocab/SRS, assessment, AI architecture, adherence, listening/
  reading/writing, defossilization) + an adversarial critique
- `prompts/` — the artifacts that run inside ChatGPT: session header template,
  post-session debrief, simulated OPI, monologue benchmark, staged writing
  feedback, week-1 canary tests
- `state/` — learner profile, curriculum state, error ledger, personas, scripts,
  adherence system, vocab pipeline, session logs, assessments
- `tools/session.py` — header generation, debrief ingestion (hours, streak,
  ledger, vocab, dashboard), stats
- `PROGRESS.md` — auto-generated dashboard
- `AGENTS.md` — operating manual for coding agents
