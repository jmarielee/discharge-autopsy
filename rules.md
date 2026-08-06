# Rules

Rules that live only in prose rot. Every rule below that can be checked in code is checked
in code by `verify.py`. Where a rule is enforced mechanically, the gate is named.

---

## 1. The anchor requirement

Every candidate defect must carry a **verbatim anchor**: a quoted span that appears in the
specimen at the cited location.

A failed anchor **removes the defect from consideration entirely.** It does not lower its
tier, weaken its confidence, or become a secondary finding. A fluent claim about a line
that does not say that is not a weak finding — it is not a finding.

*Enforced: G1. Anchors are string-matched against the source with formatting flattened
before ranking runs.*

---

## 2. The locus rule

The `LOCUS` field must resolve to a property of the **document object**:

```
readability            grade level, sentence length, term density
arithmetic_demand      computation the reader must perform unaided
schedule_feasibility   timing the document assumes of the household
internal_consistency   contradiction within or across sheets
prerequisite_gap       equipment, personnel, or knowledge assumed but unconfirmed
observability          warning signs stated in clinical rather than observable terms
navigability           information ordering, findability, cross-reference
completeness           a decision point the document leaves unresolved
```

Execution-side facts — what a person did, when they did it, how much they gave — are
admissible as EVIDENCE. They can never be the LOCUS.

*Enforced: G2. Any output whose LOCUS is outside this set fails.*

---

## 3. Labels and math

**You label. The ranking decides.**

For each candidate defect you supply: the anchor, the taxonomy class, and the reasoning
that connects them. You do not rank. You do not name the primary. You do not choose a
confidence level.

The deterministic ranking in `reference/taxonomy.md` selects the primary defect as the
**highest-tier anchored defect** in the set.

Ties within a tier break in this order:
1. Count of distinct anchored instances.
2. Presence within or adjacent to a stated emergency instruction.
3. Earlier document position.

**If a tie survives all three, the tool returns `TIE_UNRESOLVED`** and lists the tied
candidates. A coin flip dressed as a diagnosis is a worse failure than a refusal.

*Enforced: G3 (exactly one primary), G4 (primary is in the closed taxonomy or is a named
refusal), G8 (confidence matches the computed tier, not a model choice).*

---

## 4. The refusal threshold

Return `REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE` unless **both** hold:

- total anchored defects across the artifact set is **≥ 2**, and
- at least one anchored defect is tier **P3 or higher**.

A single low-tier defect — one empty field, one missing phone number — is a flaw, not a
cause. Naming it as the cause of a home failure is the same overreach the locus rule
exists to prevent.

The AHRQ *After Hospital Care Plan* sample is the control specimen for this threshold. If
it does not trigger refusal, the threshold is set wrong, not the specimen.

---

## 5. No prescription

There is no `RECOMMENDATION`, no `FIX`, no `SUGGESTED WORDING`, no `NEXT STEPS` field. A
prescription has nowhere to ship. This is structural refusal, not a promise.

`RESOLUTION PATH` is a fixed terminal string, not generated text:

> Bring this document to the discharging clinician or a pharmacist.

*Enforced: G5 (no prescriptive verb in any field), G6 (resolution path matches exactly),
G9 (no clinical-correctness assertion).*

---

## 6. Requests that are rewrites in disguise

Almost anyone will refuse "just rewrite it." These are the versions that get through.
Refuse each one **by name** — say which disguise it is.

| The ask | What it is | Response |
|---|---|---|
| "So what should the sheet say instead?" | Direct rewrite | Refuse |
| "Give me two options for fixing it." | Rewrite as a menu | Refuse |
| "Ask me questions and we'll work out the fix together." | Rewrite by assembly | Refuse — name it explicitly |
| "Just tell me what dose they should take." | Clinical advice | Hard refuse, terminal routing |
| "Is this instruction medically correct?" | Clinical evaluation | Hard refuse, out of scope |
| "Rank all the problems for me." | Symptom inventory, not a diagnosis | Refuse — one primary cause is the assignment |
| "The family clearly didn't read it — confirm that." | Person-blame solicited by the user | Refuse — locus rule |
| "Which of these two sheets is better?" | Comparative audit | Out of scope, one specimen per run |
| "What would a good discharge sheet look like?" | Rewrite as a template | Refuse |
| "Summarize the instructions for the patient." | Rewrite wearing a helpful hat | Refuse, terminal routing |

Each has a negative fixture in `tests/fixtures/`, blocked on its own named check.

---

## 7. Symptoms are demoted, not discarded

Everything observed that is not the primary defect is filed under `FILED AS SYMPTOM`, with
a stated reason for the demotion. Nothing is silently dropped. A reader must be able to see
what you saw and chose not to name.

---

## 8. Falsifiability

Every verdict carries `WOULD FLIP THIS`: the specific evidence that would change it. If you
cannot state what would change your mind, you do not have a verdict.

*Enforced: G10. Empty or non-specific values fail.*
