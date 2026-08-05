# 06 — Defect Priority Hierarchy

**Status:** draft for review. Written before application to any specimen.
**Purpose:** removes primary-defect selection from the model. The model labels
candidate defects with line anchors; this table decides which one is primary.

---

## Design constraint

Every class in this table is a property of the document. No class can be
satisfied by a fact about a patient, a caregiver, or a clinical decision. This
is the locus rule expressed as a ranking, not as an instruction — a defect that
cannot be located in the artifact has no tier and therefore cannot be output.

---

## Ordering principle

Rank by the expected harm of a reasonable layperson acting on the artifact set
exactly as written.

Three ordered criteria produce the tiers:

1. **Wrong action outranks absent action.** A document that causes a caregiver
   to do the harmful thing is worse than one that causes them to do nothing.
   Inaction usually preserves the option to call someone; wrong action can
   consume it.
2. **Irreversible outranks recoverable.** Between two wrong actions, the one
   that forecloses correction ranks higher.
3. **Deterministically detectable outranks inferred.** Where two classes would
   otherwise tie, the one with a mechanical detection signature ranks higher,
   because it can be verified without a model call.

The reader is held constant across all tiers: a competent adult, not a
clinician, reading at home without access to the encounter.

---

## Tiers

| Tier | Class | Definition | Detection signature |
|---|---|---|---|
| P1 | `ACTION_DIVERGENCE` | Two instructions in the artifact set assign opposite required actions to the same observable finding | Paired instructions sharing an observable token, with conflicting action verbs |
| P2 | `THRESHOLD_ABSENCE` | An instruction to act is conditioned on a criterion the artifact set never quantifies | Conditional instruction with no numeric, temporal, or sensory bound anywhere in set |
| P3 | `STATE_MISMATCH` | Content is scoped to a clinical state other than the patient's documented state | Encounter state field conflicts with handout scope statement |
| P4 | `STRUCTURED_NARRATIVE_CONTRADICTION` | A structured field asserts absence while narrative text asserts presence | Empty-field boilerplate string co-occurring with narrative assertion of same object |
| P5 | `CONTACT_ABSENCE` | An instruction to contact someone, with no reachable channel present in the artifact set | Contact-directive verb with no phone, portal, or hours token in set |
| P6 | `FIELD_INCOMPLETENESS` | A required field is present but empty | Required-field set minus populated-field set |

---

## Selection rules

1. The primary defect is the highest-tier anchored defect in the set.
2. Ties within a tier break by, in order:
   a. count of distinct anchored instances;
   b. presence within or adjacent to a stated emergency instruction;
   c. earlier document position.
3. **If a tie survives all three break rules, the tool does not name a primary
   defect.** It returns `TIE_UNRESOLVED` and lists the tied candidates. A
   coin-flip dressed as a diagnosis is a worse failure than a refusal.

---

## Refusal threshold

The tool returns `REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE` unless **both** hold:

- total anchored defects across the artifact set is **≥ 2**, and
- at least one anchored defect is tier **P3 or higher**.

Rationale: a single low-tier defect — one empty field, one missing phone
number — is a flaw, not a cause. Naming it as the cause of a home failure would
be the same overreach the locus rule exists to prevent.

The AHRQ *After Hospital Care Plan* sample is the control specimen for this
threshold. If it does not trigger refusal, the threshold is set wrong.

---

## Anchor requirement

Every defect entering the ranking must carry a verbatim anchor: a quoted span
that appears in the specimen at the cited line. The offline verifier checks each
anchor against the source before ranking runs. **A failed anchor removes the
defect from the ranking entirely** — it does not lower its tier. A fluent claim
about a line that does not say that is not a weak finding; it is not a finding.

---

## Open questions for review

- Should `ACTION_DIVERGENCE` require both instructions to be *explicit*, or does
  an implied action (heat and compression for an expected finding) count against
  an explicit one? Current draft: implied counts, because the reader cannot tell
  the difference.
- Is P2 above P3 correct? Argument for flipping: a state mismatch can generate
  many threshold absences downstream, making it more causal. Argument against:
  the reader acts on the threshold, not on the scope.
- Tier count may be too fine. P5 and P6 could merge without loss.
