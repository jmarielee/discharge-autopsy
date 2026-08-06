# 07 — Defect Record: Specimens 01 + 02

**Artifact set:** post-operative after-visit summary (specimen-01) and companion
care instruction handout (specimen-02), delivered together to one patient
following robotic right inguinal hernia repair with mesh.

**Analysis date:** 2026-08-04
**Analyst:** builder, unblinded. See *Provenance and blinding* below.
**Ranking authority:** `06-defect-priority-hierarchy.md`

---

## Provenance and blinding

This record was produced by the builder in conversation with an assistant,
before any diagnostician run and before any practitioner session.

**The builder's own answer key is therefore not blind.** She read a structured
defect analysis prior to writing one. This is disclosed rather than corrected,
because it cannot be corrected after the fact.

No independent answer key exists for this specimen set as of this writing. An exploratory 
interview with a retired hospital pharmacist is filed at `background/exploratory-interview-2026-08-03-retired-pharmacist.md` 
and is labeled there as background rather than evidence; the subject discussed discharge practice in general 
and did not read these specimens. A practitioner session is planned: a registered nurse will receive the 
documents without the schema, the defect classes, or any statement of the hypothesis, and her unprompted 
answer will be recorded before any specific question is asked. If completed, it will be filed as 
`08-practitioner-session.md` and that becomes the answer key against which the diagnostician 
run is scored — not this record.

Until then, the findings below rest on a single unblinded reader. That is a real limit on what 
this record can support, and it is stated here rather than resolved.

---

## Defects

### D1 — `ACTION_DIVERGENCE` (P1)

The artifact set assigns opposite required actions to the same observable
finding: a tender bulge in the groin.

- **specimen-01**, Assessment and Plan: patient counseled regarding seroma
  formation; warm compresses/heating pad and compression recommended; may take
  up to 90 days to resolve.
- **specimen-02**, When should you call for help: directs the reader to seek
  immediate care if <q>the area over the hernia turns red or becomes tender</q>.

A caregiver observing a tender, swollen groin has two documents in hand
directing opposite responses. The artifact set contains no discriminating
criterion — no temperature, no drainage description, no size or timing bound —
by which a layperson could distinguish the expected finding from the emergent
one.

Both failure directions are live:

- Acting on specimen-02 → emergency presentation for an expected post-operative
  seroma.
- Acting on specimen-01 → sustained heat and compression applied to a surgical
  site infection or an incarcerated segment.

**Fever appears nowhere in the artifact set.** The single most available
layperson discriminator between expected and emergent is absent from both
documents.

### D2 — `THRESHOLD_ABSENCE` (P2)

specimen-01 directs the patient to return to activity and <q>guide themselves
based on pain</q>. No lifting limit, no duration, no activity class, no
restriction end date appears in either document.

specimen-02 separately advises avoiding heavy lifting — but as prevention for an
unrepaired hernia, not as a post-operative restriction, and likewise without a
bound.

### D3 — `STATE_MISMATCH` (P3)

specimen-02 is scoped to an unrepaired inguinal hernia. It advises that surgery
may be deferred, discusses whether repair will be needed, and offers prevention
guidance for a defect the patient no longer has. specimen-01 documents that the
repair was performed with mesh.

The handout contains no post-operative content: no incision care, no wound
appearance guidance, no infection criteria, no mesh-specific information.

One instruction in specimen-02 is not merely inapplicable but unexecutable
post-repair: the reader is told to seek care if the hernia cannot be pushed back
into place with gentle pressure while lying down. After a mesh repair there is
nothing to reduce. A reader attempting this test cannot obtain a result, and the
document does not say so.

**Suspected root:** specimen-01 carries the field `Patient educational handouts:
No information available`. No post-operative handout was attached. The
pre-operative disease handout appears to have been supplied in its place.

**Source confirmation:** portal inventory for the surgical encounter returns
specimen-02 as the only instruction document filed. The absence of
post-operative instruction is documented in the record, not inferred solely from
the empty handout field in specimen-01. See *Limitations* for the bound on this
claim.

### D4 — `STRUCTURED_NARRATIVE_CONTRADICTION` (P4)

specimen-01 narrative directs follow-up at one year and instructs the patient to
call with questions or issues. The structured Plan of Care table reads
`None recorded.` in every row, including Appointments. No appointment exists in
the record the patient was given.

### D5 — `CONTACT_ABSENCE` (P5)

Three separate contact directives appear across the set — contact our office,
call with any questions/issues, contact your doctor now — and no phone number,
portal instruction, or after-hours guidance appears anywhere in either document.

*Redaction caveat: the letterhead is redacted in the repository copy. Whether a
number was present in the original must be confirmed against the source before
D5 is asserted. Flagged pending verification.*

### D6 — `FIELD_INCOMPLETENESS` (P6)

Empty required fields in specimen-01: Patient educational handouts; Discussion
Note; all six Plan of Care rows; Medications Administered; Results. The Current
Medications table lists entries with Prescribed Date and Start Date columns
present and unpopulated.

*Redaction caveat: medication directions cannot be assessed from the repository
copy. The prior finding regarding absent analgesic directions and acetaminophen
stacking must be re-verified against the unredacted source.*

---

## Ranking

Highest tier present: **P1**. Single anchored instance at P1, no tie.

**Primary defect: D1 — `ACTION_DIVERGENCE`.**

Refusal threshold: not triggered. Six anchored defects, ≥1 at P3 or higher.

---

## Note on ordering

D1 and D3 describe related facts, and D3 is plausibly causal to D1 — the wrong
handout is why the divergence exists. The hierarchy nevertheless ranks by harm
of action, not by causal depth, so D1 is primary. If the practitioner session
names the state mismatch rather than the divergence, that is evidence the
ordering principle in `06` is wrong, and `06` changes — not this record.

---

## Limitations

**Filed is not the same as handed over.** Portal inventory documents the
instruction set filed under the surgical encounter. Paper materials issued at
the point of discharge and never entered into the record would not appear there.
The specimen set is what is retrievable from the record. It cannot be asserted
as the complete set of what was physically given to the patient.

The defects above are bounded accordingly:

- **D1 is unaffected.** The divergence exists between two documents in hand. A
  third document elsewhere would not resolve a contradiction a reader encounters
  in these two.
- **D3's root claim is bounded.** The empty handout field appears on the
  *post-operative office visit* summary, a separate encounter weeks after the
  procedure. That absence stands independently of what may have gone home on the
  surgery date.
- **D5 remains pending** verification against the unredacted letterhead.

**n=1.** One patient, one procedure, one institution. No claim is made that these
defects generalize. The specimen set demonstrates that the diagnostician detects
and ranks defects in an authentic artifact — not that these defects are common.

**Builder unblinded.** See *Provenance and blinding* above.

---

## Licensing flag — resolve before push

specimen-02 is licensed third-party content (Ignite Healthwise, LLC, adapted
under license by Henry Ford Health). Committing the full handout to a public
repository is a redistribution question independent of de-identification.

Recommended: commit short anchored excerpts and a structural description rather
than the full document, and state the substitution in `PROTOCOL.md`. Confirm
before pushing specimen-02 in full.
