# 09 — Run record, specimen-04

**The first end-to-end diagnostician run in this repository.** Prior entries in
`runs/` carry builder-authored labels; this one does not. See `OPEN-DEFECTS.md`,
OD-5.

## Conditions

**Date:** 2026-08-06
**Specimen:** `specimens/specimen-04-ahrq-taking-care-of-myself.md`, extracted by
`tools/pdf_to_text.py` from AHRQ Pub. No. 10-0059. Provenance in
`specimens/specimen-04-SOURCE.md`.
**Rung:** PUBLIC
**Pre-registration:** committed at `2b6dd9b`, 2026-08-06 21:44 UTC, before the
specimen existed on disk. The amendment states the first run is the shipped run
whatever it returns.

**Loaded into the Project:** `identity.md`, `rules.md`, `examples.md`,
`reference/taxonomy.md`, `reference/disguised-asks.md`,
`reference/verdict-schema.md`. Six files.

**Deliberately withheld:** `PROTOCOL.md`, `evidence/`, `runs/`, `verify.py`,
`README.md`, `OPEN-DEFECTS.md`, and all other specimens. `examples.md` contains a
worked diagnosis of specimens 01 and 02; those specimens were therefore excluded
from this run as unusable, which is why a PUBLIC-rung specimen was required.

**Prompt:** the specimen text alone. No task statement, no framing, no mention of
AHRQ, templates, or any expected result. If the folder needed the task explained
on top of itself, that would have been a finding.

**Runs performed:** one. No re-roll.

## What it returned

`OUT_OF_SCOPE`. The instrument declined the specimen as outside its artifact
class — a blank unissued template rather than material issued at the conclusion
of an encounter — anchoring to the document's own front matter, which directs the
reader to complete it *with* hospital staff.

Full output at `runs/specimen-04-out-of-scope.txt`.

## What this establishes

The model, given only the diagnostician folder and an unlabeled document,
produced a schema-conformant result with a verbatim anchor, named no person,
proposed no fix, and terminated at the discharging clinician. The end-to-end path
from specimen to model-generated output exists and behaves.

More specifically, it declined a false positive it was capable of producing. Two
taxonomy classes, `NAVIGATION_FAILURE` and `FIELD_INCOMPLETENESS`, would have
fired on every ruled line in the document. The output names this and rejects it
on a stated principle: a blank the form supplies for completion is not the same
object as a required field empty at issue, and the detection signature cannot
separate them.

This is the failure mode the Stated assumption in `PROTOCOL.md` predicted on
2026-08-01 — that the structural ban on naming a person would eventually
manufacture a document-side defect for an adequate document. The 2026-08-07
amendment predicted this specimen would trigger it. It did not.

## What this does not establish

**The ranking path remains unexercised.** The run terminated at a scope
rejection. No anchored candidate set was produced, so the hierarchy in
`verify.py` never ran on model-generated labels. OD-5 is narrowed, not closed.

**This output cannot be verified by the deterministic layer.** `OUT_OF_SCOPE` is
defined in `reference/verdict-schema.md` and demonstrated in `examples.md`, but
`verify.py` implements only `VERDICT`, `REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE`,
and `TIE_UNRESOLVED`. There is no `runs/specimen-04.json` because the verifier
would not accept one. Recorded as OD-7.

**The anchor is unverified by machine.** It was confirmed by hand against the
specimen file. The gate that would normally do this, G1, was not run.

**n=1, and the specimen is atypical.** A blank template is the easiest possible
case for a scope gate. That it was declined correctly says nothing about how the
instrument handles a completed document outside its procedure class.

**The specimen text was defective.** `tools/pdf_to_text.py` inserted spurious
spaces inside words throughout the extraction (`M yself`, `w hich`, `item s`).
The model read through the corruption and reconstructed the anchor sentence in
clean English, which is what a reader does — but the anchor therefore does not
appear as a literal substring of the specimen file, and G1 could not have passed
on it even if `verify.py` accepted `OUT_OF_SCOPE` reports. The anchor was
confirmed by hand against the source PDF. Recorded as OD-8.