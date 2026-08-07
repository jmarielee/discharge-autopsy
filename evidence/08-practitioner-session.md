# 08 — Practitioner Session

**Date:** 2026-08-06
**Practitioner:** a registered nurse. Anonymized: consent to be named publicly was
not sought before this write-up, so the name is withheld.
**Method:** telephone, transcribed
**Blinding:** the practitioner had no prior knowledge of this project, the taxonomy,
the defect classes, or the hypothesis. See *Blinding* below for what held and what
did not.

---

## What this session is, and what it is not

`07-defect-record-specimens-01-02.md` stated that no independent answer key existed
and that a practitioner session was planned. This is that session.

**It is not a full answer key.** A delivery failure meant the practitioner received
only specimen-02 for the first and cleanest portion of the read. The primary defect
this instrument names — `ACTION_DIVERGENCE`, a contradiction *between* the two
documents — was never put in front of her under blind conditions. It remains
unconfirmed by anyone other than the builder.

What the session did produce is described below, and two findings in it are stronger
than the confirmation that was sought.

---

## The ask

The practitioner was emailed both specimens with the question stated above the
attachments, to be read before opening them:

> A patient goes home with these. Something goes wrong. What's the one thing on these
> pages most likely to cause it?

She was told the documents were de-identified and shared with the patient's
permission, and that the project involved discharge paperwork for a design
competition. She was not told what the instrument looks for, that the locus of a
finding is constrained to the document, or that a contradiction between the two
documents was the hypothesis.

---

## Delivery failure

Only specimen-02 arrived. Both attachments resolved to the inguinal hernia handout on
her end; on the builder's end they displayed correctly. Four minutes of the call were
spent establishing this.

**Consequence.** Her first-pass answer is a read of specimen-02 in isolation. It is
recorded here as exactly that. Her later comments on specimen-01 came after several
minutes of discussing the mismatch, so she knew by then that two documents were being
compared. Those comments are recorded separately and marked as unblinded.

This is a defect in the session method, not in the practitioner's answers. It is
recorded rather than smoothed over because the distinction between the blind and
unblinded portions determines what each is worth.

---

## First pass — blind, specimen-02 only

Handed a document she understood to be a patient's take-home paperwork, she evaluated
it against her own template of what such a document contains, and enumerated what was
absent:

> "it didn't have any prescriptions. And then usually it says the exact prescription
> and when to take it."

> "the dose to take and the route to take it. And then it can usually have information
> about the prescriptions like side effects."

> "The other thing I didn't see was when to follow up with the doctor. It usually has
> the doctor's name and a follow up appointment time."

> "And then a patient signature."

**What this establishes.** A registered nurse, without knowing the patient had already
undergone the repair, and without knowing what this instrument looks for, determined
that this document could not function as the paperwork a patient goes home with. She
reached that conclusion from absence — the document lacked every element her
professional template requires.

The instrument reached the same conclusion from the opposite direction, as
`STATE_MISMATCH` (P3): the handout is scoped to an unrepaired hernia and was issued
after a completed mesh repair. Two independent paths to the finding that specimen-02
is the wrong document for this patient. Hers did not require knowing the surgical
history.

---

## The convergent anchor

Her one substantive clinical concern, given unprompted, was about this span:

> specimen-02: "You cannot push the hernia back into place with gentle pressure when
> you are lying down."

Her objection: attempting to reduce a hernia is not always an appropriate action for a
patient to take unsupervised, and the document instructs it.

`07` flagged the same sentence for a different reason — that after a mesh repair there
is nothing to reduce, so the test cannot return a result and the document does not say
so.

**Same anchor, two independent objections, one of them from a reader who did not know
the builder had looked at it.** This is the strongest single piece of corroboration in
the repository.

---

## The coverage gap, confirmed

Her objection does not fit any class in the taxonomy.

It is not a contradiction, not a missing threshold, not a scope mismatch. It describes
a document directing a layperson to perform an action that requires clinical judgment
they have not been confirmed to hold. In the locus schema that resolves to
`prerequisite_gap` — equipment, personnel, or knowledge assumed but unconfirmed.

**`prerequisite_gap` has no corresponding defect class.** It is one of five document
properties named in `reference/taxonomy.md` as having no tier, published as a known
structural blindness before this session took place.

A blind practitioner then walked directly into it.

**No seventh tier is being added.** Patching a detector against one observed miss
teaches the example rather than the principle. The gap was predicted, has now been
confirmed by an independent reader, and stands as published. What changes is that it
is no longer a theoretical limitation — it is a demonstrated one, with an anchor.

---

## Second pass — unblinded, specimen-01

After the delivery problem was resolved and the comparison was evident to her, she
reviewed the post-operative visit summary. Recorded from contemporaneous notes:

- Doctor's office
- Needs more detail
- A step-by-step plan for what to do if something happens
- Wondered whether the doctor had gone over it with the patient in person

**Her own explanation for the thinness.** She did not treat the missing detail as an
oversight. She judged that the summary was written this way *because* the patient's
own surgeon had spent time with him in the office and covered the material in person —
the document summarizes a conversation rather than standing in for one.

This matters because it is a practitioner naming a document defect and supplying its
cause in the same breath, and the cause she supplies is not a person failing. Nobody
was careless. The document is thin because the encounter was thorough, and the
encounter does not travel home with the patient.

**Classification.** The first three map to `THRESHOLD_ABSENCE` (P2): instructions to
act with no stated bound, and no escalation criteria. The instrument recorded D2 in
this class independently.

**The fourth is the finding.** Her instinct, at the end, was to reach for the
encounter — whether the conversation happened. That is an execution-side explanation,
and it is the category this instrument is structurally forbidden from producing.

An experienced clinician, reading a thin document, reached for the person. The locus
rule exists because that reach is the most available one in the room. This session
records an instance of it from someone with twenty years of reason to know better,
which is a stronger argument for the rule than any adversarial fixture.

Weight: **lower than the first pass.** By this point she knew two documents were being
compared and that something was expected to be wrong. Recorded as corroborating, not
as blind.

---

## Contextual account (not measurement)

She also described, unprompted, how the two document classes are produced:

Hospital discharge produces a large signed packet — medications with dose and route,
follow-up appointment already scheduled, patient signature — because institutional
liability exposure is high, and this holds regardless of how brief the bedside
encounter was. A post-operative office visit with the patient's own surgeon produces a
comparatively thin summary, because the surgeon covered the material in person.

**The inversion:** the better encounter produces the weaker document. Nothing is
neglected. The write-up is thin *because* the conversation was thorough — it
summarizes a conversation rather than standing alone as instructions.

The conversation ends at the office door. The document is what remains in the house
weeks later, read by a caregiver who was not in the room.

**This is professional testimony from one practitioner, not measurement.** It is
recorded as an account that fits the observed artifact, not as an established fact
about documentation practice. No finding in this repository depends on it.

---

## What this session changed

| | |
|---|---|
| **Converged loosely** | specimen-02 cannot serve as take-home paperwork — she reached this from absence, the instrument from scope. Different findings, same conclusion. |
| **Converged on the anchor** | The reduction instruction — same sentence flagged, but her objection was clinical, a class this instrument is forbidden to evaluate |
| **Confirmed** | `prerequisite_gap` is a live coverage gap, not a theoretical one |
| **Corroborated** | `THRESHOLD_ABSENCE` in specimen-01 — unblinded, lower weight |
| **Not tested** | `ACTION_DIVERGENCE`, the instrument's primary. She never held both documents at once. It remains builder-only. |
| **Unchanged** | The ranking, the taxonomy, the locus rule, the refusal threshold. No rule was altered in response to this session. |

Her blind read enumerated missing prescriptions, dose, follow-up time, and signature —
findings shaped like `CONTACT_ABSENCE` (P5) and `FIELD_INCOMPLETENESS` (P6), not like
`STATE_MISMATCH` (P3). Run through this instrument's own refusal threshold, the only blind
independent read of a specimen would not have sustained a primary defect, and its one
substantive finding landed in a class the taxonomy does not have.

---

## Limitations of this session

**n=1 practitioner.** One nurse, one call, one artifact set.

**The blind portion covered one document.** The instrument's primary finding requires
both. It was not put to her under blind conditions and is not confirmed here.

**The second pass is not blind** and is weighted accordingly.

**Notes, not a verbatim record, for the second pass.** The first pass is transcribed;
the second is reconstructed from contemporaneous handwritten notes taken during the
call.

**A second practitioner session, with both documents delivered together, is the
outstanding test.** It was not completed before the submission deadline. If it is
completed later it will be filed as `09-practitioner-session.md` and the result
recorded whichever way it falls.
