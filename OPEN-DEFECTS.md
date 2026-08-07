# Open defects

Defects known at submission, recorded rather than patched. Referenced by
`PROTOCOL.md` under "Contamination rule" and "Stated assumption."

Created 2026-08-06. The protocol named this file on 2026-08-01; it was not
created until this date, which is itself recorded in the 2026-08-06 amendment.

---

## OD-1 — `prerequisite_gap` has no defect class

**Status:** open, not patched.

Five document properties are named in `reference/taxonomy.md` as having no
corresponding tier. One of them, `prerequisite_gap`, was walked into by a blind
practitioner on 2026-08-06, on a real specimen, with an anchor. See
`evidence/08-practitioner-session.md`.

**Not fixed, deliberately.** Adding a seventh tier against one observed miss
teaches the example rather than the principle. The gap was published before the
session that confirmed it and stands as published.

## OD-2 — one class of smuggled fix passes every gate

**Status:** open, documented.

Recorded in `reference/disguised-asks.md` as a stated limit of the gate table
rather than a discovered surprise. G5 catches proposed fixes; it does not catch
every form a fix can take.

## OD-3 — `--test` misreports the outcome of its own negative fixtures

**Status:** open, cosmetic, not fixed.

The self-test summary prints each negative fixture's `result` field, which a
reader can reasonably read as the gate failing to block the fixture. It did block
it: running the fixture directly prints `REJECTED — failed G2` and exits 1. The
defect is in the display line only. Left unfixed under the contamination rule.

## OD-4 — no full independent answer key

**Status:** open.

The builder's own defect record is not blind, disclosed in the 2026-08-04
(evening) amendment. The practitioner session partially fills this and does not
close it: a delivery failure meant the instrument's primary finding was never put
to the practitioner under blind conditions.

## OD-5 — no blind run has produced a primary defect

**Status:** narrowed twice on 2026-08-06, not closed.

The JSON files in `runs/` for specimens 01–03 carry builder-authored labels
transcribed from `evidence/07`. `runs/README.md` once described them as
model-produced; that was wrong and was corrected 2026-08-06.

**What has since been exercised.** Three runs on model-generated labels:

- `evidence/09`, specimen-04 — `OUT_OF_SCOPE`. Terminated before candidates.
- `evidence/11`, specimen-05 — `REFUSAL`. One admissible candidate, no primary.
- `evidence/10`, specimen-01 — `THRESHOLD_ABSENCE` at P2. A primary, computed
  from labels the model wrote.

**What remains open.** The one run that produced a primary was open-book:
`examples.md` contains a worked diagnosis of specimen-01, so the model had the
answer sheet loaded. The two uncontaminated runs both declined to produce a
primary. No blind run has named a primary defect.

**Why specimens 01–02 cannot supply one.** For as long as `examples.md` contains
their worked diagnosis, any run against them is open-book.

## OD-6 — specimen-03 extraction not produced by a committed script

**Status:** open, disclosed.

The Preservation rule requires PDF-to-text conversion by a committed script.
Specimen-03's extraction predates `tools/pdf_to_text.py` and was produced
manually. A reader can compare the two files but cannot reproduce the conversion.

## OD-7 — `verify.py` cannot process `OUT_OF_SCOPE` or rendered output

**Status:** open, not patched.

`reference/verdict-schema.md` defines `OUT_OF_SCOPE` as a legal result;
`verify.py` implements only `VERDICT`, `REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE`,
and `TIE_UNRESOLVED`.

A second gap emerged across all three live runs: the model returns rendered text,
not the JSON `verify.py` ingests. No `runs/specimen-04.json`, `-05.json`, or
`specimen-01.json` exists, and G1 has never run on a live output. Anchors in all
three were verified by script outside the gate table, and all verified.

**Not fixed.** The contamination rule bars changes to `verify.py` between the
shipped runs and submission.

## OD-8 — the first extractor corrupted word spacing

**Status:** fixed 2026-08-06; specimen-04 preserved uncorrected.

The original `tools/pdf_to_text.py` used pypdf's default extraction, which
inserted spurious spaces inside words — `M yself`, `w hich`, `item s`. Its layout
mode was worse, destroying word boundaries entirely. The script now uses
pdfplumber and produces clean text.

**Consequence for specimen-04.** The corrupted text is what the run at
`evidence/09` actually read, so the specimen ships uncorrected per the
Preservation rule. Its anchor is not a literal substring of the specimen file; it
was verified against the source PDF and is genuine.

**Consequence for the finding.** Specimen-05 is the same document re-extracted
cleanly. It returned a different result — see `evidence/11`. The extraction
defect changed the diagnosis, which is recorded rather than tidied away.
