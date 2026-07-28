# Vocabulary system

## Spine

Davies' Spanish frequency list (top 20k lemmas, free):
https://www.wordfrequency.info/files/spanish/spanish_lemmas20k.txt
Download it here as `davies-20k.txt` (not committed by default — large).

Targets: full command (recognition + production) of the top ~3,000 lemmas
(≈94-95% of spoken Spanish); recognition of 3,000–5,000; personal/domain vocab
on top.

## P0 diagnostic sweep

Batch self-test the top 3,000 in chunks (e.g., 100/day inside Anki or on paper):
for each word — (a) recognize meaning? (b) produce it EN→ES cold? Partition:

- **known** — skip, no cards
- **dormant** — recognized but couldn't produce → production cards, these
  relearn fast (savings effect) and are the cheap early wins
- **unknown** — recognition cards first; promote to production if they show up
  in conversation

## Anki policy (from the research)

- FSRS on, desired retention 0.85–0.90. ~5–7 new cards/day sustained.
- Card format: simple L1↔L2 pairs + one short Mexican-Spanish example sentence.
  Production (EN→ES) for top-3k and conversation-mined items; recognition
  (ES→EN) for breadth. Mnemonics only for repeatedly-failed cards.
- Cognates: no reading cards needed, but DO make listening/pronunciation cards
  for high-value cognates (they're transparent on paper, not by ear).
- Maintain a small false-friend deck (actual, embarazada, realizar, asistir,
  carpeta, éxito, recordar…).

## Files

- `inbox.md` — human-readable log of mined vocabulary (appended by the session
  tool)
- `anki-import.tsv` — appended by the session tool; import into Anki
  (File → Import, tab-separated: front, back, example, tag), then archive the
  imported rows by hand or leave them (Anki dedupes on first field)
