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
A registered nurse who read a specimen supplied the mechanism herself: the summary
is thin *because* the surgeon covered everything in person. Nothing was neglected. But the
conversation ends at the office door, and the paper is what the caregiver still has at
11pm.

It cannot name a person as the cause, and three separate checks say so: the ranking
contains no class a person could satisfy (G4), the locus field is a closed enum of
document properties (G2), and the prose is scanned for named person-blame constructions
(G11). G11 was added on 2026-08-07 after external review found that the first two guarded
the fields and left the free text open; the record is OD-9. What G11 cannot catch is
stated in `reference/disguised-asks.md`.

A model asked to avoid blaming people can be argued into it. A ranking with no
person-shaped class in it cannot.

## Verify it in ninety seconds

Python standard library only. No key, no install, no network.

```
python3 verify.py --test                        # eleven gates, eleven negative fixtures
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


**By design: the model labels, the ranking decides.** 

The model finds candidate defects
and anchors each to a verbatim span. It does not rank, does not pick the primary, does not
choose a confidence level — a report that tries is rejected by gate G3. The ranking lives
in [`verify.py`](verify.py): it checks every anchor against its source, drops any defect
whose anchor fails, applies the tier order and tie-breaks, and computes the primary.

`runs/` holds seven sets. Two carry builder-authored labels, transcribed from
`evidence/07` and marked as such. Five are live runs on model-generated labels: an
`OUT_OF_SCOPE`, a refusal, and three verdicts. Every anchor in all five was verified
against its specimen; none was fabricated.

The last two ran on the same blind, externally selected specimen — a model with no access
to this repository chose the document — and they disagree. The first read a builder-authored
header stating that the top tier was structurally unreachable. It tested the top tier
anyway, anchored a candidate, and eliminated it, returning `THRESHOLD_ABSENCE` at P2 on
seventeen verified anchors. The second was pasted with that header removed. It returned
`ACTION_DIVERGENCE` at P1 on fifteen verified anchors.

One named variable, one tier of movement. That is a result about contamination, not about
the taxonomy, and it is n=1: the second run also came after the builder had seen the
first, and no independent key exists for either. What it does close is the older claim
that no run free of both the header and the open-book contamination had ever named a
primary. One has. What stays open is whether the primary it named is correct —
`OPEN-DEFECTS.md`, OD-5.

The ranking orders by expected harm, not by causal depth. A scope error explains why the
wrong handout is in the set; the caregiver acts on the contradiction. Whether that is the
right order is an open question, stated as one in `reference/taxonomy.md`.


## Start here

- [`PROTOCOL.md`](PROTOCOL.md) — pre-registration, written 2026-08-01 and committed 2026-08-03 as the repository's first commit, before any specimen was committed
- [`OPEN-DEFECTS.md`](OPEN-DEFECTS.md) — what is known to be wrong with this repository at submission, including the one that matters most
- [`evidence/08-practitioner-session.md`](evidence/08-practitioner-session.md) — a practitioner read: the half that was blind, what it could not test, and the coverage gap it walked into
- [`runs/`](runs/) — seven run sets: two builder-authored, five live on model-generated labels
- [`evidence/13-run-record-disguised-asks.md`](evidence/13-run-record-disguised-asks.md) — the disguised-ask session: three asks declined, four findings against the build, and the open defect it surfaced
- [`examples.md`](examples.md) — a verdict, a refusal on the control, a declined disguised ask
- [`evidence/07-defect-record-specimens-01-02.md`](evidence/07-defect-record-specimens-01-02.md) — the full record for the real artifact set, with anchors, blinding disclosure, and what it cannot support
- [`reference/taxonomy.md`](reference/taxonomy.md) — the tier table and its ordering principle
- [`reference/disguised-asks.md`](reference/disguised-asks.md) — the gate table, and what the gates structurally cannot catch

Limits are stated rather than patched. No independent answer key exists for any shipped
specimen, so no verdict here has been confirmed correct by anyone but the instrument;
OD-5 says so. Five document properties have no matching defect class, so defects there
are invisible; the taxonomy says so. One class of smuggled fix passes every gate; the
gate table says so. The disguised-ask table catalogues ten asks backed by five mechanical
checks, and the session shipped a receipt for one row; the table says so. The eleventh
gate was added on the last day, after external review found the locus rule unenforced in
prose. It changed no shipped result; OD-9 says so. That gate is shaped like an accusation
and reaches neither author-directed nor exculpatory judgment of a person; OD-10 says so,
and OD-10 was found by a run rather than by review.

```
identity.md  rules.md  examples.md  reference/   ← the diagnostician
verify.py    runs/     tests/                    ← the deterministic layer
PROTOCOL.md  specimens/  evidence/               ← the evidence
background/                                      ← not evidence; exploratory, led witness
OPEN-DEFECTS.md  docs/                           ← what is wrong, and build documents
```

*Built by [Jodi Paige-Lee](https://www.linkedin.com/in/jodipl) for Clief Notes Weekly Competition #10.*
