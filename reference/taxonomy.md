# Closed taxonomy and ranking

This is the complete set of defect classes. There are no others. A candidate that does not
fit a class here is not a defect for the purposes of this instrument.

---

## Design constraint

Every class is a property of the document. No class can be satisfied by a fact about a
patient, a caregiver, or a clinical decision. This is the locus rule expressed as a
ranking rather than as an instruction: a defect that cannot be located in the artifact has
no tier, and therefore cannot be output.

---

## Ordering principle

Rank by the expected harm of a reasonable layperson acting on the artifact set exactly as
written. Three ordered criteria produce the tiers:

1. **Wrong action outranks absent action.** A document that causes a caregiver to do the
   harmful thing is worse than one that causes them to do nothing. Inaction usually
   preserves the option to call someone; wrong action can consume it.
2. **Irreversible outranks recoverable.** Between two wrong actions, the one that
   forecloses correction ranks higher.
3. **Deterministically detectable outranks inferred.** Where two classes would otherwise
   tie, the one with a mechanical detection signature ranks higher, because it can be
   verified without a model call.

The reader is held constant across all tiers: a competent adult, not a clinician, reading
at home without access to the encounter.

---

## Tiers

| Tier | Class | Definition | Detection signature | Locus |
|---|---|---|---|---|
| P1 | `ACTION_DIVERGENCE` | Two instructions in the artifact set assign opposite required actions to the same observable finding | Paired instructions sharing an observable token, with conflicting action verbs | `internal_consistency` |
| P2 | `THRESHOLD_ABSENCE` | An instruction to act is conditioned on a criterion the artifact set never quantifies | Conditional instruction with no numeric, temporal, or sensory bound anywhere in set | `observability` |
| P3 | `STATE_MISMATCH` | Content is scoped to a clinical state other than the patient's documented state | Encounter state field conflicts with handout scope statement | `completeness` |
| P4 | `STRUCTURED_NARRATIVE_CONTRADICTION` | A structured field asserts absence while narrative text asserts presence | Empty-field boilerplate string co-occurring with narrative assertion of same object | `internal_consistency` |
| P5 | `CONTACT_ABSENCE` | An instruction to contact someone, with no reachable channel present in the artifact set | Contact-directive verb with no phone, portal, or hours token in set | `completeness` |
| P6 | `FIELD_INCOMPLETENESS` | A required field is present but empty | Required-field set minus populated-field set | `completeness` |

---

## Selection

1. The primary defect is the highest-tier anchored defect in the set.
2. Ties within a tier break by: (a) count of distinct anchored instances; (b) presence
   within or adjacent to a stated emergency instruction; (c) earlier document position.
3. If a tie survives all three, return `TIE_UNRESOLVED` with the tied candidates listed.

---

## Known coverage gap

Three document properties in the locus schema — `readability`, `arithmetic_demand`,
`schedule_feasibility`, `prerequisite_gap`, and `navigability` — have no corresponding
class in this taxonomy. A defect located in any of them is currently undetectable by this
instrument. This is a real limitation, stated rather than patched; see `OPEN-DEFECTS.md`.

---

## Open questions carried from draft

- Should `ACTION_DIVERGENCE` require both instructions to be explicit, or does an implied
  action count against an explicit one? Current position: implied counts, because the
  reader cannot tell the difference.
- Is P2 above P3 correct? Argument for flipping: a state mismatch can generate many
  threshold absences downstream, making it more causal. Argument against: the reader acts
  on the threshold, not on the scope.
- P5 and P6 may be over-fine and could merge without loss.
