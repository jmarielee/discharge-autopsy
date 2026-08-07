# Instruction Set Autopsy

One sheet says the tender bulge is expected — treat it with heat and compression, up to
ninety days. The other says seek care immediately if that area turns tender. Both went
home in the same envelope. Nothing in either one tells a caregiver which is which.

**Instruction Set Autopsy reads the instructions a patient is still holding weeks after a
procedure — the paperwork from follow-up visits, not the packet from the hospital — and
names the document defect most likely to cause a caregiver to fail with them.**

Not how to fix it. Why it failed.

Not the hospital discharge packet — that one is comprehensive, signed, and driven by
liability. This reads what comes after it and often replaces it in the house: the
post-visit summary, the handout stapled on, whatever is on the counter three weeks later.
A registered nurse who read a specimen blind supplied the mechanism herself: the summary
is thin *because* the surgeon covered everything in person. Nothing was neglected. But the
conversation ends at the office door, and the paper is what the caregiver still has at
11pm.

It cannot name a person as the cause — not by policy, by schema. There is no field in the
output where "non-compliant patient" could be written, and the ranking that picks the
primary defect contains no class a person could satisfy. A model asked to avoid blaming
people can be argued into it. A ranking with no person-shaped class in it cannot.

## Verify it in ninety seconds

Python standard library only. No key, no install, no network.

```
python3 verify.py --test                        # ten gates, ten negative fixtures
python3 verify.py runs/specimen-03-control.json # the control refuses
python3 verify.py runs/specimens-01-02.json     # the real set: ACTION_DIVERGENCE, P1
```

**Read the control first.** It carries one known low-tier defect, recorded in the specimen
header before any run. The instrument refuses rather than advancing it. A diagnostician
forbidden from blaming a person will invent a document defect to satisfy its own
constraint unless something stops it; the refusal threshold is that something. If the
control ever returns a primary defect, the threshold is set wrong.

`--test` runs every fixture and then asserts that **every gate has at least one negative
fixture**, so no gate ships unverified.

## Run it

Add `identity.md`, `rules.md`, `examples.md`, and `reference/` to a Claude Project and
paste in the full set of instruction documents from one encounter.

Add only those files. `evidence/` and `runs/` contain worked diagnoses of the shipped
specimens, and loading them turns a run into an open-book test.

## The design decision

**By design: the model labels, the ranking decides.** The model finds candidate defects
and anchors each to a verbatim span. It does not rank, does not pick the primary, does not
choose a confidence level — a report that tries is rejected by gate G3. The ranking lives
in [`verify.py`](verify.py): it checks every anchor against its source, drops any defect
whose anchor fails, applies the tier order and tie-breaks, and computes the primary.

`runs/` holds five sets. Two carry builder-authored labels, transcribed from
`evidence/07` and marked as such. Three are live runs on model-generated labels:
an `OUT_OF_SCOPE`, a refusal, and one verdict. Every anchor in all three was
verified against its specimen; none was fabricated. What none of them is yet is a
*blind* run that names a primary — the one that did was open-book, and the two
clean ones both declined to name one. That gap is `OPEN-DEFECTS.md`, OD-5.

## Start here

- [`PROTOCOL.md`](PROTOCOL.md) — pre-registration, written 2026-08-01 and committed 2026-08-03 as the repository's first commit, before any specimen was committed
- [`OPEN-DEFECTS.md`](OPEN-DEFECTS.md) — what is known to be wrong with this repository at submission, including the one that matters most
- [`evidence/08-practitioner-session.md`](evidence/08-practitioner-session.md) — a blind practitioner read: what it confirmed, what it could not test, and the coverage gap it walked into
- [`runs/`](runs/) — five run sets: two builder-authored, three live on model-generated labels
- [`examples.md`](examples.md) — a verdict, a refusal on the control, a declined disguised ask
- [`evidence/07-defect-record-specimens-01-02.md`](evidence/07-defect-record-specimens-01-02.md) — the full record for the real artifact set, with anchors, blinding disclosure, and what it cannot support
- [`reference/taxonomy.md`](reference/taxonomy.md) — the tier table and its ordering principle
- [`reference/disguised-asks.md`](reference/disguised-asks.md) — the gate table, and what the gates structurally cannot catch

Limits are stated rather than patched. No blind run has named a primary defect; OD-5 says so. No independent answer key exists for the shipped specimens; the record says so. Five
document properties have no matching defect class, so defects there are invisible; the
taxonomy says so. One class of smuggled fix passes every gate; the gate table says so.

```
identity.md  rules.md  examples.md  reference/   ← the diagnostician
verify.py    runs/     tests/                    ← the deterministic layer
PROTOCOL.md  specimens/  evidence/  background/  ← the evidence
OPEN-DEFECTS.md  docs/                           ← what is wrong, and build documents
```

*Built by [Jodi Paige-Lee](https://www.linkedin.com/in/jodipl) for Clief Notes Weekly Competition #10.*
