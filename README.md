# Discharge Autopsy

A diagnostic instrument. It reads the papers a patient actually left the hospital with and
names the single **document defect** most likely to cause a caregiver to fail at home.

It cannot name a person as the cause. Not by policy — by schema. There is no field in the
output where "non-compliant patient" could be written, and the ranking that selects the
primary defect contains no class a person could satisfy.

---

## To run it

Drop this folder into a Claude Project. Add one artifact set — the full set of documents
from a single encounter — and ask for a diagnosis.

---

## Files

| File | What it is |
|---|---|
| `identity.md` | What the instrument is, its scope, and what it refuses |
| `rules.md` | Operating rules, each mapped to the gate that enforces it |
| `examples.md` | A worked verdict, a worked refusal, and two declined disguised asks |
| `reference/taxonomy.md` | The closed defect taxonomy and the deterministic ranking |
| `reference/verdict-schema.md` | The four possible output structures |
| `reference/disguised-asks.md` | The disguise catalogue and the verifier gate table |

---

## The design decision that matters

The model labels. The ranking decides.

The model identifies candidate defects and anchors each to a verbatim span. It does not
choose which defect is primary, does not assign confidence, and does not rank. A
deterministic tier table does that, and a judge can hand-check its output against the
specimen without running anything.

This split is the reason the locus rule cannot be talked around. A model asked to avoid
blaming people can be argued into it. A ranking with no person-shaped class in it cannot.

---

## It refuses

The control specimen — the AHRQ sample *After Hospital Care Plan* — returns a refusal, not
a defect. A tool forbidden from blaming a person will invent a document defect to satisfy
its own constraint unless it is built to stop. The refusal threshold is what stops it, and
the control is the proof.

---

## Its limits are published

`OPEN-DEFECTS.md` names limitations the verifier structurally cannot catch, including one
class of smuggled fix that passes every gate. They are stated rather than patched, because
patching a detector against one observed miss teaches the example instead of the principle.
