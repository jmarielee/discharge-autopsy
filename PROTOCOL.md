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
## Amendment — 2026-08-04 (evening)

- **Artifact class.** Specimen-01 is an after-visit summary generated
  for a post-operative office visit, not a packet issued at the point
  of hospital discharge. The scope in "Scope of the instrument" is
  therefore read as: the patient-facing written instruction set issued
  at a care transition and carried home. This covers discharge
  packets, after-visit summaries, and their companion handouts. The
  widening is recorded here rather than applied silently, and was
  made after specimen acquisition revealed the failure mechanism to
  be a property of the artifact *set* rather than of a single
  document.
- **Portal inventory.** Specimen-02 is the only instruction document
  filed under the surgical encounter in the patient portal. The
  absence of post-operative instruction is documented at source, not
  inferred solely from the empty educational-handouts field in
  specimen-01.
- **Bound on that claim.** Portal inventory records what was *filed*.
  Paper materials handed over at discharge and never entered into the
  record would not appear. The specimen set is what is retrievable
  from the record and is not asserted to be the complete set of what
  was physically given to the patient.
- **Specimen-02 licensing.** Specimen-02 is third-party licensed
  patient-education content (© Ignite Healthwise, LLC; adapted under
  license by the health system). It is reproduced unaltered as a
  research specimen, with attribution recorded in
  `specimens/specimen-02-SOURCE.md`. It is not authored by the
  builder and all rights remain with the copyright holder. It is
  preserved in its retrieved HTML form, markup included, so that
  quoted anchors can be verified against the source.
- **Builder blinding — disclosure.** The builder produced a
  structured defect analysis of specimens 01 and 02 (recorded in
  `07-defect-record-specimens-01-02.md`) in conversation with an
  assistant, prior to writing an independent answer key. The
  builder's own key is therefore not blind, and this cannot be
  corrected after the fact. The independent key for this specimen set
  is the PRACTITIONER-rung session, conducted with a clinician who
  receives the specimens without the taxonomy, the schema, or any
  statement of the hypothesis, and whose unprompted account is
  recorded before any specific question is asked.
- **PRACTITIONER rung status.** Pending as of this amendment. If no
  session is obtained, the rung ships empty and named as empty, per
  the Inputs section above.
- **Ranking authority.** `06-defect-priority-hierarchy.md` was
  written and committed before its application to any specimen. It
  removes primary-defect selection from the model: the model labels
  anchored candidates, the hierarchy and its tiebreak rules select
  the primary, and an unresolved tie returns `TIE_UNRESOLVED` rather
  than a choice.

## Amendment — 2026-08-06

- **Correction to the timestamp claim above.** The section "Written
  2026-08-01" states that this file's commit timestamp is the evidence
  that the method was not shaped after the results. That is stronger
  than the repository supports, and the original sentence is left
  unedited above rather than quietly corrected. What the history
  actually shows: this file is commit `71f473d`, the first commit in
  the repository, dated 2026-08-03 15:35:50 UTC. The specimens commit
  `25f5bc5` carries the same timestamp to the second — both were
  pushed together. The history therefore establishes commit ordering
  within this repository and nothing more. It does not establish a
  gap, and it does not independently corroborate the 2026-08-01
  writing date, which rests on the author's word. The defensible
  claim is the narrow one: the protocol is the repository's first
  commit, and no specimen appears before it.

- **No diagnostician run exists.** The JSON files in `runs/` carry
  builder-authored labels transcribed from `evidence/07`, which states
  on its own face that it was produced before any diagnostician run.
  `runs/README.md` described them as model-produced; that description
  was wrong and is corrected as of this date. The end-to-end path from
  specimen to model-generated labels was never exercised. Recorded in
  `OPEN-DEFECTS.md` as OD-5, including why running it now against
  specimens 01 and 02 would be an open-book test: `examples.md`
  contains a worked diagnosis of those specimens by name.

- **Runtime fields.** The `Runtime` section above was committed with
  `[model]` and `[interface]` unfilled and is not edited. They remain
  unfilled because no diagnostician run was performed. No model or
  interface is recorded because none was used to produce the shipped
  labels.

- **Pharmacist markup attempted, not obtained.** The 2026-08-03 and
  2026-08-04 amendments pre-registered a sealed specimen markup by a
  licensed pharmacist (retired), a household member. A session was
  conducted 2026-08-04 with both specimens in hand and the blind ask
  stated unchanged. It did not produce a markup against the artifact,
  and no finding in this repository is drawn from it. The session
  transcript is withheld: it is not de-identified and the subject is
  a household member. Recorded here so the rung's status is not
  inferred from silence — no result was obtained, and none was
  withheld for being unwelcome.

- **PRACTITIONER rung filled by a different clinician.** The rung was
  filled on 2026-08-06 by a registered nurse, not by the
  pre-registered pharmacist. Full session record in
  `evidence/08-practitioner-session.md`.

- **Relationship disclosed.** The practitioner is a relative by
  marriage of the builder (the builder's sister-in-law's niece),
  outside the builder's household, with infrequent contact, contacted
  for this project specifically. She is not an independent recruit;
  she is a convenience sample obtained through a family network, and
  is recorded as such.

- **Scope narrowed after specimens were read.** The 2026-08-04
  (evening) amendment read the scope as covering discharge packets,
  after-visit summaries, and companion handouts. As of commit
  `40bd876` the instrument excludes the hospital discharge packet and
  addresses post-visit instruction sets only. This narrowing was made
  after the specimens were read and after the practitioner session,
  and is recorded here rather than applied silently.

- **`OPEN-DEFECTS.md` created.** The "Contamination rule" and "Stated
  assumption" sections above reference this file. It did not exist
  until this date. It now exists and is populated with the defects
  known at submission.

- No rule, threshold, taxonomy class, gate, or tie-break was altered
  in response to the practitioner session.

## Amendment — 2026-08-07

- **PUBLIC-rung specimen admitted, procedure class widened.** Specimens
  04 and 05 are MedlinePlus patient instruction pages for laparoscopic
  cholecystectomy, a procedure class outside the one named on
  2026-08-03. The widening is recorded here before the run, not after
  it. Source URLs and retrieval date are in the specimen headers.
  Rationale: OD-5 records that no end-to-end run exists, and specimens
  01–02 cannot supply one because `examples.md` contains a worked
  diagnosis of them by name. A specimen absent from `examples.md` is
  required.
- **Result is binding.** The first run is the shipped run, whatever it
  returns, including a refusal or a class the builder disagrees with.
  Per the Stated assumption above, an unwanted result is logged, not
  re-rolled.
- **PUBLIC-rung specimen withdrawn before use.** The MedlinePlus pages
  named above were not used and no run was performed on them. Their
  content is licensed from A.D.A.M./Ebix, not public domain, and the
  license bars reproduction and use in evaluating AI systems. The
  cholecystectomy class widening is void.

- **PUBLIC-rung specimen admitted.** Specimen-04 is "Taking Care of
  Myself: A Guide for When I Leave the Hospital," AHRQ Publication
  No. 10-0059, a U.S. Government work in the public domain. It is a
  fillable discharge template rather than a completed instruction set,
  and is admitted knowing that: an instrument that flags its blank
  fields as `FIELD_INCOMPLETENESS` has produced a false positive of
  the kind named in the Stated assumption above. Procedure class is
  widened to unspecified inpatient discharge for this specimen only.

## Amendment — 2026-08-06 (evening)

- **Second run pre-registered.** Specimen-05 is the same source document as
  specimen-04, re-extracted with a corrected converter. The specimen-04 run
  stands as the first and binding run; nothing from it is discarded or
  superseded. Specimen-05 exists because the specimen-04 extraction was
  defective in a way that made its anchors unverifiable — see OD-8 — not
  because its result was unwelcome.
- **What the second run tests.** Whether the `OUT_OF_SCOPE` result was a
  property of the document or an artifact of a corrupted reading of it. A
  differing result is the more interesting outcome and is recorded as such.
- **Result is binding**, on the same terms as the 2026-08-07 entry. First run
  on specimen-05 is the shipped run.

## Amendment — 2026-08-07

- **Amendment dating error.** The block above headed `## Amendment — 2026-08-07`
  was committed in `f29debc` at 2026-08-06T16:11:30-04:00. Its heading date is
  one day ahead of its commit. It was also appended to after it was written, so
  one dated entry records three sequential decisions: the MedlinePlus admission,
  its withdrawal, and the AHRQ admission. It stands unedited above, and appears
  out of sequence relative to the 2026-08-06 (evening) entry, which is also left
  as committed. In a file whose value is dating discipline this is the error that
  matters most, and it is corrected here rather than tidied above.

- **G11 added; Contamination rule satisfied, not excepted.** The locus rule was
  unenforced in prose (OD-9). The Contamination rule permits a fix once every
  specimen has been run, shipped as a labeled re-run with both behaviours on the
  record. Specimens 01-05 are all run and no sixth was admitted, so that
  condition holds. The re-run is deterministic — `verify.py` against two report
  files and twelve fixtures, no model call, no new specimen. No shipped result
  changed. The defect was found by external review, not by a run.

- **OD-3 superseded.** Display-layer only; not a rule, discriminator, threshold,
  or detector, so the Contamination rule never barred it.

- No taxonomy class, tier, threshold, or tie-break was altered.
