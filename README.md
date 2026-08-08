# Instruction Set Autopsy

One sheet says a fluid collection at the surgical site is expected, and to treat
it with heat and compression for up to ninety days. The other says seek care
right away if that area becomes tender. Nothing in either one tells a caregiver
how to tell the two apart.

**Instruction Set Autopsy reads the paperwork a patient is still holding weeks after a
procedure, and names the one document defect most likely to make a caregiver fail at
home.**

Not how to fix it. Why it failed.

## It cannot blame a person

When home care goes wrong, the easy explanation is that the patient didn't follow the
directions. This tool cannot give that answer. Not "won't" — can't.

That constraint exists because the easy explanation is usually the wrong question. Look at
the two sheets above. A caregiver who follows one exactly is violating the other. Nobody
failed to follow directions. The directions disagreed.

So this tool asks a narrower question: what about the paper made the wrong action look
correct? Then it stops.

Three checks hold that line, and you can run all three:

- `G2` — the cause must be a document property, from a fixed list
- `G4` — the list of defect types contains nothing a person could be
- `G11` — the written explanation is scanned for blame aimed at a person

`G11` was added on the last day, after an outside reviewer found the first two guarded the
structured fields but left the prose open. It changed no shipped result. The record is
`OD-9`. What it still misses is in
[`reference/disguised-asks.md`](reference/disguised-asks.md).

## What it reads

Not the hospital discharge packet. That one is long and signed and written under legal
pressure, so it tends to be thorough.

This reads what comes after: the visit summary, the handout stapled to it, whatever is on
the counter three weeks later. Those are written under the opposite pressure. A registered
nurse who read one of these specimens supplied the mechanism herself — the summary is thin
*because* the surgeon covered everything in person. Nothing was skipped. But the
conversation ends at the office door, and the paper is what the caregiver has at 11pm.

She also read specimen-02 blind, not knowing what this tool looks for or that the patient
had already had the surgery, and concluded it couldn't work as go-home paperwork. She got
there from what was missing. The tool got there from a scope error. Same conclusion, two
directions. That was one nurse, one call, one of the two documents — it doesn't prove the
pattern generalizes, and this repository doesn't claim it does.

## How it works

The model finds candidate defects and quotes the exact words that show each one. It does
not rank them, pick the primary, or choose a confidence level.

[`verify.py`](verify.py) does that. It checks every quote against the source, drops any
defect whose quote fails, applies a fixed ranking, picks the primary, and runs eleven gates
on the result.

**The model labels. The ranking decides.**

## Verify it in ninety seconds

Python standard library only. No key, no install, no internet.

```bash
python3 verify.py --test
python3 verify.py runs/specimen-03-control.json
python3 verify.py runs/specimens-01-02.json
```

Every gate blocked by its own test case, the control refusing, and the real set returning
`ACTION_DIVERGENCE` at P1.

**Run the control first.** It holds one small known flaw, written into its header before
any run. A tool forbidden from blaming a person will invent a document defect instead, just
to have something to say. The minimum bar stops it: two anchored defects, one of them
serious. The control doesn't clear it, so the tool refuses. If it ever returns a defect
there, the bar is wrong.

## Run it

Add only these four to a Claude Project, then paste the complete set of instruction documents from one visit into the project.

```text
identity.md   rules.md   examples.md   reference/
```

Once the documents are in the project, ask Claude to diagnose the instruction set. It will identify candidate document defects; `verify.py` determines which one becomes the primary diagnosis.

Don't add `runs/` or `evidence/`. Those hold finished diagnoses, and loading them turns a fresh run into an open-book test.

## What the runs show

`runs/` holds seven sets. Two use builder-written labels and say so. Five are live runs on
model-written labels: one out-of-scope decline, one refusal, three verdicts. Every quote in
all five was checked against its source. None was invented.

The last two used the same document, picked by an outside model with no access to this
repo — and they disagreed. The first saw a builder-written note claiming the top tier was
impossible here. It tested that tier anyway, found a candidate, ruled it out, and returned
`THRESHOLD_ABSENCE` at P2. The second got the same document with the note deleted, and
returned `ACTION_DIVERGENCE` at P1.

One variable, one tier of movement. That's a finding about contamination, not about the
ranking. It's also a single case, and the second run came after the builder had seen the
first. It settles an older worry — that no clean run had ever named a primary. One has.
Whether that primary is *correct* is still open.

## What is wrong with it

Recorded, not patched. Full list in [`OPEN-DEFECTS.md`](OPEN-DEFECTS.md).

- **Nobody has confirmed these answers but the tool itself.** No independent answer key
  exists for any specimen. Biggest one — `OD-5`.
- **Five document properties have no matching defect type.** Defects there are invisible.
- **One kind of smuggled fix passes every gate.** The gate table says which.
- **`G11` only catches accusations.** It misses judgment aimed at the author, and misses a
  person being let off the hook — `OD-10`, found by a run, not a reviewer.
- **The ranking sorts by likely harm, not root cause.** A scope error explains how the
  wrong handout got in the envelope; the caregiver acts on the contradiction. Whether
  that's the right order is open, and `reference/taxonomy.md` says so.

## Start here

- [`OPEN-DEFECTS.md`](OPEN-DEFECTS.md) — what's known to be broken
- [`PROTOCOL.md`](PROTOCOL.md) — the plan, written 2026-08-01 and committed 2026-08-03 as
  the first commit, before any specimen was added
- [`examples.md`](examples.md) — a verdict, a refusal, a declined ask
- [`evidence/13-run-record-disguised-asks.md`](evidence/13-run-record-disguised-asks.md) —
  a session that tried to trick it: three asks declined, four problems found
- [`runs/`](runs/) — seven run sets, and what each proves

```text
identity.md  rules.md  examples.md  reference/   ← the diagnostician
verify.py    runs/     tests/                    ← the part that decides
PROTOCOL.md  specimens/  evidence/               ← the evidence
tools/                                           ← how specimen text and anchors were checked
background/                                      ← not evidence; a led witness
OPEN-DEFECTS.md  docs/                           ← what's wrong, and build notes
```

*Built by [Jodi Paige-Lee](https://www.linkedin.com/in/jodipl) for Clief Notes Weekly
Competition #10.*
