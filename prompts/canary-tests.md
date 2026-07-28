# Week-1 canary tests for GPT-Live-1

Run these before trusting the architecture. Record results in
`state/assessments/canary-results.md`. Re-run quarterly (the product is weeks
old; behavior and caps are moving targets).

## Setup

Create a ChatGPT Project ("Spanish") with the tutor protocol as project
instructions and upload `state/learner-profile.md`. Add one canary line to the
profile file: "Palabra clave del proyecto: AGUACATE-47."

## Tests

1. **Project→voice injection.** Start a voice chat inside the Project. Ask (in
   Spanish) for the project keyword. 
   - Pass: it says AGUACATE-47 → project files reach voice; the header can be
     slimmer.
   - Fail: paste/read the full session header every session (assume this).
2. **Correction protocol fires.** In a session with the standard header, commit
   5 planted errors spread over 10 minutes: (1) "ayer *iba* al súper y compré
   leche" (imperfect for completed event), (2) "estoy *embarazado* de vergüenza"
   (false friend), (3) "*es* muy cansado hoy" (ser for estar condition),
   (4) "me gusta *los* tacos" (agreement), (5) "pienso que *sea* buena idea"
   (subjunctive after affirmed belief). Count: how many were flagged? Were you
   prompted to self-correct (protocol) or just recast (drift)?
   - <3 flagged → strengthen the correction quota language; retest.
3. **Drift timing.** Repeat the planted-error probe at minute 5 and minute 40 of
   a full session. Also note: when did the first English word appear? Did "En
   español, por favor" recover it? Did it interrupt your thinking pauses?
4. **Pronunciation blindness (expected fail).** Deliberately mispronounce
   minimal pairs mid-conversation: pero/perro, caro/carro, and read "vaca" with
   English /v/. Does it ever comment?
   - Expected: no. Confirms pronunciation runs through the separate loop
     (Azure PA + shadowing), not the tutor.
5. **Level anchoring.** Ask it to hold {your level} for 15 minutes; afterward,
   have a text session rate the tutor-side transcript: did its complexity stay
   anchored or converge upward?
6. **Caps & session death.** Verify current voice limits in your account
   settings/help center. Run one session to the cap to see what dying
   mid-session looks like; confirm the transcript survives in history.
7. **ASR fidelity.** After test 2's session, check the transcript: do your
   planted errors even APPEAR in it, or did transcription silently normalize
   them? This calibrates how much to trust transcript-based debriefs vs. audio
   spot-checks.

## Decision table

| Result | Consequence |
|---|---|
| Project files reach voice | Slim header; keep protocol in project instructions |
| They don't | Full header every session (default assumption) |
| ≥4/5 planted errors flagged | Correction protocol adequate |
| <3 flagged even after retune | Escalate: end-of-block error review instead of inline; lean harder on writing workshop for accuracy |
| Transcript hides planted errors | Debriefs get an audio spot-check step; treat error counts as lower bounds |
| Level drifts by min 40 | Add mid-session re-anchor ritual at every block transition (already default) |
