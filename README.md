# Discharge Autopsy

One sheet says the tender bulge is expected — treat it with heat and compression, up to
ninety days. The other says seek care immediately if that area turns tender. Both went
home in the same envelope. Nothing in either one tells a caregiver which is which.

**Discharge Autopsy reads the papers a patient left the hospital with and names the
document defect most likely to have caused a caregiver to fail at home.**

Not how to fix it. Why it failed.

It cannot name a person as the cause — not by policy, by schema. There is no field in the
output where "non-compliant patient" could be written, and the ranking that picks the
primary defect contains no class a person could satisfy. A model asked to avoid blaming
people can be argued into it. A ranking with no person-shaped class in it cannot.

## Run it

Add this repo to a Claude Project and paste in the full set of instruction documents from
one encounter. Three specimens ship in `specimens/`, including a control that is supposed
to return a refusal.

## The design decision

**The model labels. The ranking decides.** The model finds candidate defects and anchors
each to a verbatim span. It does not rank, does not pick the primary, does not choose a
confidence level. A six-tier table does that, and you can hand-check it against the
specimen without running anything.

## Start here

- [`PROTOCOL.md`](PROTOCOL.md) — pre-registration, committed 2026-08-01 before any specimen was collected
- [`examples.md`](examples.md) — a verdict, a refusal on the control, a declined disguised ask
- [`evidence/07-defect-record-specimens-01-02.md`](evidence/07-defect-record-specimens-01-02.md) — the full record for the real artifact set, with anchors, blinding disclosure, and what it cannot support
- [`reference/taxonomy.md`](reference/taxonomy.md) — the tier table and its ordering principle
- [`reference/disguised-asks.md`](reference/disguised-asks.md) — the gate table, and what the gates structurally cannot catch

Limits are stated rather than patched. No independent answer key exists for the shipped
specimens yet; the record says so. Five document properties have no matching defect class,
so defects there are invisible; the taxonomy says so. One class of smuggled fix passes
every gate; the gate table says so.

```
identity.md  rules.md  examples.md  reference/   ← the diagnostician
PROTOCOL.md  specimens/  evidence/  background/  ← the evidence
docs/                                            ← build documents
```

*Built by [Jodi Paige-Lee](https://www.linkedin.com/in/jodipl) for Clief Notes Weekly Competition #10.*
