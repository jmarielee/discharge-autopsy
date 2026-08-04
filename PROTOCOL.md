# Diagnostic protocol — pre-registered

**Written 2026-08-01, before any specimen was collected or read.**

Amendments are appended below with their own dates. Nothing above the amendment line is
ever edited. This file is committed before the first specimen enters the repo, and its
commit timestamp is the evidence that the method was not shaped after the results.

---

## Scope of the instrument

This diagnostician reads **written discharge and post-procedure instruction documents**
for one procedure class: `[PROCEDURE CLASS — fill in before first commit]`.

It diagnoses **document properties only**. It does not evaluate care, does not evaluate a
clinical decision, and does not evaluate a person. It cannot state that an instruction is
medically wrong; it can state only that the document requires something of its reader that
the document does not supply.

Every diagnosis terminates at the discharging clinician or pharmacist as the resolution
path. The instrument produces no fix, no rewrite, and no recommendation.

## Runtime

Claude `[model]`, `[interface]`, with the diagnostician folder loaded as a Project.
The diagnostician never reads the contents of `tests/`. Test material is evidence *about*
the product and is not part of the product.

## Inputs

Specimens are discharge instruction documents in the named procedure class, admitted at
one of three evidence rungs:

- **SEEDED** — synthetic documents authored for this repo with planted defects and a
  committed answer key.
- **PUBLIC** — documents published openly by institutions for distribution to patients.
  The source URL and a retrieval date are recorded for each. A reader can re-download the
  original and independently verify every quoted span.
- **AUTHOR** — documents from the author's own household, redacted before entering the
  repo, and labeled as the author's own rather than presented as third-party.

A fourth rung, **PRACTITIONER**, is defined but is only claimed if a practitioner supplies
an observed account of a real failure of a real document. If no practitioner run is
obtained, the rung ships **empty and named as empty**. No rung is stretched to appear
filled.

## Redaction

Names, dates of birth, medical record numbers, facility identifiers where the owner
requests it, and any free-text a specimen owner asks to remove are stripped **before the
document reaches the repo**. Redaction is performed by the specimen's owner where one
exists, and by the author for AUTHOR-rung documents.

Where redaction removes text that a finding would otherwise quote, the finding reports
`REDACTED` rather than paraphrasing the removed content.

## Preservation rule

Transcripts are pasted verbatim into `runs/` and never edited. Errors, false starts, and
wrong turns stay in. A cleaned receipt proves nothing.

Specimens are used as received. No specimen is edited, trimmed, or reformatted to make a
finding land. Where a specimen must be converted (PDF to text), the conversion is
performed by a committed script and both the original and the extraction ship.

## Contamination rule

All specimens are run against a **frozen commit**, whose hash is recorded in the run
transcript before the first specimen is processed. No rule, discriminator, threshold, or
detector is changed between specimens.

If a run reveals a defect, the defect is recorded in `OPEN-DEFECTS.md` and fixed **only
after every specimen has been run**. The fixed version then ships as a separate, labeled
re-run against the same specimens, so both the original and corrected behaviour are on the
record.

## Stated assumption

This diagnostician will get at least one specimen wrong, or will reach a defensible
diagnosis by an indefensible route. When that happens it is logged in `OPEN-DEFECTS.md`,
not patched out of the record.

It is further assumed that the locus rule — the structural ban on naming a person as the
cause — will at some point produce a false positive, manufacturing a document-side defect
for a document that was adequate. A specimen demonstrating the abstention verdict is
shipped deliberately for this reason.

## Falsification

A diagnosis is wrong if any of the following holds:

1. A quoted span in the output is not a verbatim substring of the specimen.
2. The named locus is not a property of the document object.
3. The primary cause does not clear the separation threshold over the runner-up, and the
   instrument named one anyway instead of abstaining.
4. The output contains a prescription, a rewrite, or a recommended clinical action.
5. The output addresses the clinical correctness of an instruction rather than the
   document's demands on its reader.

Each shipped diagnosis names, in its own `WOULD FLIP THIS` field, the specific evidence
that would change its verdict.

---

## Amendments

*(Append below, each dated. Nothing above this line is edited.)*
## Amendment — 2026-08-03

- Specimen review by a licensed pharmacist (retired), who is a
  household member. Relationship disclosed; he remains blind to
  the taxonomy, schema, and this file until his markup is
  recorded and sealed.
- An exploratory interview was conducted 3 Aug. It is background,
  not evidence. See /background/.
- Patient portal acquisition was attempted and partially failed:
  regional health system consolidation placed pre-June-2026
  hospital records behind a 30-business-day request.
- Procedure class: inguinal hernia repair, post-operative.

## Amendment — 2026-08-04

- Scope limit. The corpus is n=1: two documents from a single
  episode of care for a single patient, plus one public control
  specimen. The taxonomy derived from it is a hypothesis, not a
  general claim about discharge documentation.
- Specimen review by a licensed pharmacist (retired), who is a
  household member. Relationship disclosed. He remains blind to
  the taxonomy, schema, and this file until his markup is
  recorded and sealed.
- Specimens were obtained from the patient portal with the
  patient's consent. Both are outpatient documents from the
  post-operative episode.
- An exploratory interview was conducted 3 Aug. Background, not
  evidence. See /background/.
- Procedure class: inguinal hernia repair, post-operative.
- Control specimen (AHRQ sample AHCP) added 4 Aug. Expected
  output is "no primary defect identified." A known malformed
  dose unit in the source is recorded in the specimen header
  prior to any run.