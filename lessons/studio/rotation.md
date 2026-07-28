# Studio hour — 4-week rotation, fully scripted

The third weekly hour. No decisions to make: find the week type, do the steps.
Log each studio hour with `type: "studio"` (the writing/rating prompts already
emit loggable JSON; for the rest, log a minimal entry with minutes + notes).

## Week 1 — Taller de escritura I

1. (25 min) Write 150–250 words on the CURRENT unit's prompt (table below).
   No dictionary while drafting; mark words you wanted with [?].
2. (25 min) Run `prompts/writing-feedback.md` in ChatGPT text mode with
   `{FOCUS_FAMILIES}` = the current unit's family + one ledger `active`
   feature. Do all four stages honestly — self-correct before reveals.
3. (10 min) Add [?] words + corrections to Anki; log the scorecard JSON.

| Unit | Writing prompt |
|---|---|
| U1 | Describe tu ciudad a un amigo mexicano que nunca ha ido: cómo es, qué hay, dónde queda lo bueno. |
| U2 | Narra la historia completa de un viaje que salió mal: escena, eventos, desenlace. |
| U3 | Retrata a tres personas de tu familia: físico, carácter, y cómo están últimamente. |
| U4 | Cuenta la historia de un regalo importante: quién te lo dio, por qué, qué hiciste con él. |
| U5 | Explica tu proyecto de español: por qué lo haces, para qué, para cuándo, y qué has hecho por él. |

## Week 2 — Entrenamiento de oído

1. (30 min) Three micro-dictations, native Mexican audio (No Hay Tos episode,
   or a Mexican YouTube/Netflix clip):
   - Pick a 30–45 second stretch. Listen ONCE at 1.0x, write what you catch.
   - Listen twice more at 1.0x, filling gaps. One pass at 0.8x ONLY if stuck.
   - Check against the transcript/captions. Copy the stretches you misheard
     and mark WHY: linking (mi.sa.mi.gos), reduction (pa'/ps), speed, unknown
     word. Unknown words → Anki.
2. (20 min) Oral grammar mini-cycle in ChatGPT text-with-voice-dictation or
   text: ask it to fire 15 rapid transformation items on the current unit's
   family (e.g., U2: "yo digo una frase en presente, tú la pones en la forma
   pasada correcta y yo te digo si el porqué"). It confirms/corrects each.
3. (10 min) Ledger review: update `state/curriculum-state.md` notes; queue
   anything alarming for the next session's warm-up.

## Week 3 — Taller de escritura II + fluidez sola

1. (30 min) Writing workshop as Week 1, second prompt of the unit (invent a
   variation on the same theme) or re-write Week 1's text from scratch without
   looking — then diff against the corrected version.
2. (20 min) Solo 4/3/2 with recording: this unit's fluency topic, recorded on
   your phone in 4-, 3-, and 2-minute versions. Listen to the 2-minute one
   against the earliest recording of the same topic. Note: faster? fewer
   English islands? same errors?
3. (10 min) Anki housekeeping: suspend leeches, import mined TSV rows.

## Week 4 — Benchmark mensual

1. (35 min) Record 2 timed monologues per `prompts/monologue-rating.md`
   (one repeated from last month, one fresh). Transcribe them.
2. (20 min) Run the rating prompt in a separate text session; log its JSON.
3. (5 min) Triage: in `state/error-ledger.json` promote watch→active features
   that keep appearing, retire actives with high spontaneous accuracy; spend/
   check streak tokens; glance at PROGRESS.md pace vs. the 500-hour ETA.

Quarterly (every 3rd Week-4): swap step 2's monologue rating for the full
simulated OPI (`prompts/opi-simulation.md`) and refill 1 repair token (max 2).
