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

## OD-5 — the ranking path has never run on model-generated labels

**Status:** narrowed 2026-08-06, not closed.

The JSON files in `runs/` for specimens 01–03 carry builder-authored labels
transcribed from `evidence/07`, which states on its own face that it was produced
before any diagnostician run.

**What has since been exercised.** An end-to-end run was performed on specimen-04
on 2026-08-06 under pre-registered conditions. See
`evidence/09-run-record-specimen-04.md`. The model, given only the diagnostician
folder and an unlabeled document, produced a schema-conformant result.

**What remains unexercised.** That run returned `OUT_OF_SCOPE` and terminated
before producing anchored candidates. The path this defect names — model emits
labeled candidates, `verify.py` ranks them, a primary is computed — has still
never run on labels a model wrote.

**Why specimens 01–02 cannot supply it.** `examples.md` contains a worked
diagnosis of both by name. Any run against them with the folder loaded is an
open-book test.

## OD-6 — specimen-03 extraction not produced by a committed script

**Status:** open, disclosed.

The Preservation rule requires PDF-to-text conversion by a committed script. Both
files ship for specimen-03, but its extraction predates `tools/pdf_to_text.py`
and was produced manually. A reader can compare the two files but cannot
reproduce the conversion step.

## OD-7 — `verify.py` cannot process an `OUT_OF_SCOPE` report

**Status:** open, found by the specimen-04 run, not patched.

`reference/verdict-schema.md` defines `OUT_OF_SCOPE` as a legal result and
`examples.md` demonstrates one. `verify.py` implements only `VERDICT`,
`REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE`, and `TIE_UNRESOLVED`. A conforming
`OUT_OF_SCOPE` report cannot be verified by the deterministic layer, and no
`runs/specimen-04.json` exists. The anchor was confirmed by hand; G1 did not run.

The defect is a gap between the schema and the verifier, not a fault in either
alone. The instrument behaved correctly and produced a result its own checker
cannot read. Not fixed: the contamination rule bars changes to `verify.py`
between the shipped runs and submission.

## OD-8 — `tools/pdf_to_text.py` corrupts word spacing

**Status:** open, found during the specimen-04 run, specimen preserved as-is.

The extractor inserts spurious spaces inside words throughout its output —
`M yself`, `w hich`, `item s` — an artifact of the source PDF's font encoding.
Twenty-eight instances of three sample patterns appear in an 8.5 KB extraction.

**Consequence for the run.** The corrupted text is what was submitted to the
diagnostician. The model read through it and reconstructed its anchor sentence in
clean English, which is what a reader does — but that anchor is therefore not a
literal substring of the specimen file and could not pass G1 against it. The
anchor was confirmed by hand against the source PDF and is genuine.

**Specimen not corrected.** Per the Preservation rule, specimens are used as
received. Hand-cleaning it would mean the shipped specimen is not the text the
model actually read.
