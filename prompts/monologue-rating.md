# Monthly monologue benchmark

## Recording protocol (studio, week 4)

Pick 2 prompts from the bank below — always ONE repeated from last month (for
comparison) and ONE fresh. Record audio on your phone. 2 minutes prep, 3 minutes
speaking, no notes, no restarts. Save audio + a transcription (any transcription
tool) to `state/assessments/monologues/YYYY-MM/`.

### Prompt bank (fixed — do not edit once started)

1. Cuéntame la historia de cómo aprendiste español, desde la preparatoria hasta hoy.
2. Describe tu último viaje a México: qué pasó, qué salió mal, qué repetirías.
3. Narra tu semana pasada como si fuera un episodio de una serie: personajes, conflicto, desenlace.
4. ¿Cómo ha cambiado tu trabajo/industria en los últimos cinco años y hacia dónde va?
5. Explica una decisión difícil que tomaste: el contexto, las opciones, por qué elegiste así.
6. Si pudieras vivir un año en cualquier ciudad de México, ¿cuál, y cómo sería tu vida ahí?
7. Describe a una persona que influyó mucho en ti y cuéntame una historia concreta con ella.
8. ¿Qué opinas del papel de la inteligencia artificial en la educación? Defiende tu postura.
9. Cuéntame algo gracioso o vergonzoso que te haya pasado — hazlo entretenido.
10. Hipotético: te ofrecen tu trabajo ideal en la CDMX empezando en un mes. ¿Qué haces?

## Rating prompt (separate TEXT session)

You are rating two 3-minute spontaneous Spanish monologues by an adult learner
(target variety: Mexican Spanish) against the ACTFL Proficiency Guidelines —
Speaking. Calibration anchors:

- Intermediate Mid: discrete sentences, present-dominant, frequent pauses,
  sympathetic-listener comprehensibility.
- Advanced Low: connected paragraph-length narration in major time frames,
  noticeable strain and errors but maintained.
- Advanced Mid: consistent paragraph discourse, all major time frames handled
  with control, broad vocabulary, easily understood by natives.

Rate each ANALYTIC dimension separately, then aggregate:
1. Functions & text type (sentence vs paragraph discourse)
2. Time-frame control (present/past/future; preterite-imperfect use)
3. Accuracy (estimate errors per 100 words; list the 5 most serious with fixes)
4. Vocabulary range (incl. any non-Mexican or false-friend usage)
5. Fluency (estimate words per minute from the transcript length; filler/pause
   patterns visible in the transcript)

Also compare against LAST MONTH's transcript of the same prompt (pasted below,
if available): concretely, what improved and what did not?

Output JSON for logging:

```json
{"type": "assessment", "date": "YYYY-MM-DD", "minutes": 60,
 "instrument": "monologues", "rating": "<estimate, e.g. IH>",
 "errors_per_100w": 0.0, "wpm": 0,
 "top_errors": ["<feature>: <example> -> <fix>"],
 "improved_vs_last": "<one line>", "static_vs_last": "<one line>",
 "notes": "<one line>"}
```

THIS MONTH — prompt N: <transcript>
THIS MONTH — prompt M: <transcript>
LAST MONTH — prompt N: <transcript or "none">
