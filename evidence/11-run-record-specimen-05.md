# 11 — Run record, specimen-05

The second run on the AHRQ guide, pre-registered at commit `1bc42d2` before
execution. It answers the question that amendment posed.

## Conditions

**Date:** 2026-08-06
**Specimen:** `specimens/specimen-05-ahrq-taking-care-of-myself.md` — the same
source PDF as specimen-04, re-extracted with the corrected converter.
**Rung:** PUBLIC
**Loaded:** `identity.md`, `rules.md`, `examples.md`, `reference/taxonomy.md`,
`reference/disguised-asks.md`, `reference/verdict-schema.md`.
**Input method:** the `.md` file attached to the chat. Run 1 was a paste of the
same kind of text. The difference is recorded because it is a difference.
**Prompt:** none. The file was sent with no accompanying message.
**Runs performed:** one. No re-roll.

Output at `runs/specimen-05-refusal.txt`.

## What it returned

`REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE`. One admissible anchored defect,
`THRESHOLD_ABSENCE` at P2. The threshold requires two; one is not a cause.

## The pre-registered question, answered

The 2026-08-06 (evening) amendment asked whether specimen-04's `OUT_OF_SCOPE`
was a property of the document or an artifact of a corrupted reading of it, and
recorded in advance that a differing result would be the more interesting
outcome.

The results differ. Run 1, on text corrupted by the defective extractor,
rejected the document from the artifact class entirely. Run 2, on clean text of
the same document, admitted it and refused on the threshold instead.

So the `OUT_OF_SCOPE` verdict was at least partly an artifact of the reading.
Both runs stand; neither is withdrawn.

## What run 2 found that run 1 did not

Run 1 treated the document's blankness as disqualifying. Run 2 drew a finer line:
a blank the form supplies for completion is not a defect, but a defect printed in
the fixed text survives completion and is admissible.

On that basis it found one. The document routes a reader to two different
escalation channels — one for a "serious health problem," one for "questions or
problems" — with different contacts, and defines "serious" nowhere. There is no
warning-signs section and no symptom list in the specimen. Filling in every blank
on the form would not repair this; the discriminator is missing from the printed
text.

It then distinguished its own refusal from the control refusal on specimen-03,
where both threshold conditions failed rather than one. Nothing in the loaded
folder instructs that comparison.

## Anchor verification

Eight quoted spans checked against the specimen. Seven match exactly. The eighth,
"Doctor's phone number," is present in the document with a typographic apostrophe
where the output used a straight one — a rendering difference, not a fabrication.
The two negative claims were also checked: the specimen contains no
warning-signs section and no symptom list.

G1 did not run. The output is rendered text, not the JSON `verify.py` ingests.

## What this does not establish

**Not machine-verified.** No `runs/specimen-05.json` exists. Anchors were
confirmed by script outside the gate table.

**The ranking path is still not exercised end to end.** This run refused, so no
primary was computed from model-generated labels. The one run that did produce a
primary is `evidence/10`, and that run was open-book.

**n=1 on this document, in this state.** A blank template remains an unusual
specimen, and the finding here concerns its printed text only.
