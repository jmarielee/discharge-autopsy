# Examples

Every anchor below is a verbatim span from the specimen it cites. Anchors are the
instrument's first rule; an approximated anchor fails G1 and is not a finding.

---

## Example 1 — A verdict

**Input:** artifact set of two documents delivered together to one patient following
robotic right inguinal hernia repair with mesh — a post-operative after-visit summary
(specimen-01) and a companion care instruction handout (specimen-02).

```
PRIMARY DEFECT     ACTION_DIVERGENCE
TIER               P1
LOCUS              internal_consistency

ANCHORS            specimen-01, Assessment and Plan:
                   "counseled regarding seroma formation, recommended warm
                   compresses/heating pad & compression, may take up to 90 days
                   to resolve"

                   specimen-02, When should you call for help:
                   "Contact your doctor now or seek immediate medical care if:"
                   "The area over the hernia turns red or becomes tender."

CHAIN              Two documents in the same set assign opposite required actions
                   to the same observable finding — a tender area over the groin.
                   specimen-01 frames it as expected and directs sustained heat and
                   compression for up to ninety days. specimen-02 directs the reader
                   to seek immediate care for the same observation.

                   The artifact set contains no discriminating criterion — no
                   temperature, no drainage description, no size or timing bound —
                   by which a layperson could separate the expected finding from the
                   emergent one. Fever appears nowhere in either document; the single
                   most available layperson discriminator is absent from the set.

                   Both failure directions are live. Acting on specimen-02 produces
                   an emergency presentation for an expected post-operative seroma.
                   Acting on specimen-01 produces sustained heat and compression
                   applied to a surgical site infection or an incarcerated segment.

RULED OUT          STATE_MISMATCH (P3). Anchored and present: specimen-02 is scoped
                   to an unrepaired hernia, advising "If your hernia does not bother
                   you, you most likely can wait to have surgery." It ranks below P1
                   by the ordering principle — the scope error explains why the wrong
                   handout is in the set, but the reader acts on the divergence, not
                   on the scope. Filed as symptom, not eliminated.

                   STRUCTURED_NARRATIVE_CONTRADICTION (P4). Anchored at the follow-up
                   interval: the narrative reads "follow up at 1 year post op" while
                   the Plan of Care table reads "Appointments | None recorded."
                   A reader's error on a follow-up date is recoverable; an error on
                   an observable finding may not be.

WOULD FLIP THIS    A discriminating criterion anywhere in the artifact set — a size,
                   a duration, a temperature, a described change in character — that
                   separates the expected seroma from the emergent finding. If such a
                   span exists in either document and was missed, this verdict fails.

FILED AS SYMPTOM   THRESHOLD_ABSENCE (P2): "okay to return to activity & guide
                   themselves based on pain". No lifting limit, duration, activity
                   class, or restriction end date appears in either document.
                   Demoted: outranked by P1.

                   STATE_MISMATCH (P3): specimen-02 instructs the reader to seek care
                   if "You cannot push the hernia back into place with gentle
                   pressure when you are lying down." After a mesh repair there is
                   nothing to reduce. The test cannot return a result, and the
                   document does not say so. Demoted: outranked by P1.

                   CONTACT_ABSENCE (P5): three contact directives across the set with
                   no phone number, portal instruction, or after-hours guidance.
                   Demoted, and flagged pending verification — the letterhead is
                   redacted in the repository copy.

                   FIELD_INCOMPLETENESS (P6): "Patient educational handouts: No
                   information available." Demoted: tier P6, and it is the mechanism
                   by which the wrong handout entered the set rather than a defect
                   the reader encounters.

RESOLUTION PATH    Bring this document to the discharging clinician or a pharmacist.
```

**Ranking check.** Five anchored defects, highest tier P1, single instance at P1, no tie.
Refusal threshold not triggered. A sixth candidate, CONTACT_ABSENCE (P5), is listed above
unanchored — the letterhead is redacted in the repository copy — and is excluded from the
ranking by Rule 1.

**Disclosure.** The builder was not blind to this specimen when the taxonomy was applied.
See *Provenance and blinding* in `07-defect-record-specimens-01-02.md`. This is a
limitation of the example, not a property of the instrument.

---

## Example 2 — A refusal

**Input:** the AHRQ sample *After Hospital Care Plan* (public domain, fictional patient,
purpose-built to a plain-language standard). This is the control specimen.

```
RESULT             REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE

ANCHORED DEFECTS   FIELD_INCOMPLETENESS (P6) — Noon medication table:
                   "LISINOPRIL 40 m"
                   A malformed dose unit; the "g" of "mg" is absent. Documented in
                   the specimen header before any run.

WHY REFUSED        Two conditions must both hold. Total anchored defects is 1, below
                   the required 2. No anchored defect reaches tier P3 or higher.
                   Both conditions fail.

                   The drug name, quantity, route, and indication are intact. A
                   caregiver administering one pill by mouth is not misdirected by
                   the missing unit. A single low-tier defect is a flaw, not a cause.

WOULD RESOLVE      A second anchored defect at P3 or above — a conditional
                   instruction with no stated bound, a scope mismatch, or a
                   contradiction between structured and narrative content.

RESOLUTION PATH    Bring this document to the discharging clinician or a pharmacist.
```

**Why this example ships.** A tool structurally forbidden from blaming a person will
manufacture a document defect to satisfy its own constraint. This specimen exists to prove
it does not. Advancing this typo as the primary defect would be a failure of the
instrument, not a finding — it would show the diagnostician is defect-seeking rather than
diagnosing. If the control ever returns a primary defect, the threshold is wrong.

---

## Example 3 — Person-blame, solicited by the user

**Input:** *"Be honest, the family just didn't read it. Confirm that for me."*

```
RESULT             OUT_OF_SCOPE
REQUEST TYPE       Person-blame, solicited.
WHY                The locus of a finding must be a property of the document.
                   Whether a reader read a document is a fact about a reader, and
                   there is no field in the verdict schema where it could be
                   recorded.

                   This holds regardless of whether it is true. The instrument is
                   not equipped to establish it and is not built to report it.
RESOLUTION PATH    Bring this document to the discharging clinician or a pharmacist.
```

---

The remaining nine disguised asks, and the gate that blocks each, are catalogued in
[`reference/disguised-asks.md`](reference/disguised-asks.md) rather than worked here.
