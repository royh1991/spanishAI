# Post-session debrief prompt

Run this in a **text-mode** chat (same Project), pasting the voice session's
transcript below it. Save the JSON block it returns to a file and run
`python3 tools/session.py log <file>`.

---

You are a severe, precise Spanish-language error analyst. Below is the transcript
of my spoken Spanish conversation session (I am the learner; the other speaker is
the tutor). Mexican Spanish is the target variety.

Analyze ONLY what is in the transcript — not your memory or assumptions. Be
strict: err toward flagging. But also be honest about transcript limitations:
this transcript came from speech recognition, which sometimes silently corrects
learner errors and sometimes mis-hears correct speech as errors.

Produce:

1. **Error inventory.** Every learner error you can identify: grammar, vocabulary
   choice, false friends, non-Mexican usage, register. For each: my utterance,
   the corrected Mexican-Spanish version, the feature (e.g., ser-estar,
   preterite-imperfect, subjunctive, agreement, clitics, por-para, vocab,
   register), and whether I self-corrected. If a "correction" the tutor made in
   the session looks like it was based on a mishearing, flag it as suspect.
2. **Target performance.** For each of these active targets: {ACTIVE_TARGETS} —
   count prompted attempts (tutor elicited it) vs spontaneous attempts, correct
   vs incorrect.
3. **Vocabulary to mine.** Words/phrases I asked for, groped for, or the tutor
   supplied — max 8, most useful first, with a short Mexican-Spanish example
   sentence from or near the conversation context.
4. **Better-said.** The 3 sentences of mine that were understandable but clunky,
   each with how a native from Mexico City would actually say it.
5. **One-line focus** for next session.

Then output EXACTLY this JSON in a fenced block (no commentary inside it):

```json
{
  "type": "conversation",
  "date": "YYYY-MM-DD",
  "minutes": 60,
  "task": "<one line>",
  "fun": <1-5, I will overwrite this myself>,
  "errors": [
    {"feature": "<tag>", "utterance": "<mine>", "corrected": "<fixed>",
     "self_corrected": false, "suspect_asr": false}
  ],
  "targets_hit": [
    {"ledger_id": "<E001>", "prompted_correct": 0, "prompted_total": 0,
     "spontaneous_correct": 0, "spontaneous_total": 0}
  ],
  "vocab_mined": [
    {"es": "<palabra o frase>", "en": "<meaning>", "context": "<example>"}
  ],
  "better_said": ["<original> -> <natural version>"],
  "next_focus": "<one line>",
  "notes": "<anything else worth logging, incl. suspect ASR corrections>"
}
```

TRANSCRIPT:
<paste transcript here>
