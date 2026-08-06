# Open defects

Defects known at submission, recorded rather than patched. Referenced by
`PROTOCOL.md` under "Contamination rule" and "Stated assumption."

Created 2026-08-06. The protocol named this file on 2026-08-01; it was not
created until this date, which is itself recorded in the 2026-08-06 amendment.

---

## OD-1 — `prerequisite_gap` has no defect class

**Status:** open, not patched.

Five document properties are named in `reference/taxonomy.md` as having no
corresponding tier. One of them, `prerequisite_gap` — equipment, personnel,
or knowledge assumed but unconfirmed — was walked into by a blind
practitioner on 2026-08-06, on a real specimen, with an anchor. See
`evidence/08-practitioner-session.md`.

**Not fixed, deliberately.** Adding a seventh tier against one observed miss
teaches the example rather than the principle. The gap was published before
the session that confirmed it and stands as published.

## OD-2 — one class of smuggled fix passes every gate

**Status:** open, documented.

Recorded in `reference/disguised-asks.md` as a stated limit of the gate
table rather than a discovered surprise. G5 catches proposed fixes; it does
not catch every form a fix can take.

## OD-3 — `--test` misreports the outcome of its own negative fixtures

**Status:** open, cosmetic, not yet fixed.

The self-test summary prints each negative fixture's `result` field:

    ok    negative-G2-execution-side-locus.json  ->  VERDICT

A reader can reasonably read that as the gate failing to block the fixture.
It did block it — the assertion logic checks that the named gate fired and
that no unrelated gate fired, and running the fixture directly prints
`REJECTED — failed G2` and exits 1. The defect is in the display line only.

Left unfixed at submission under the contamination rule: no change is made
to `verify.py` between the shipped runs and the submission.

## OD-4 — no full independent answer key

**Status:** open.

The builder's own defect record is not blind, disclosed in the 2026-08-04
(evening) amendment. The practitioner session partially fills this and does
not close it: a delivery failure meant the instrument's primary finding,
`ACTION_DIVERGENCE`, was never put to the practitioner under blind
conditions. It remains builder-only.

## OD-5 — no end-to-end diagnostician run exists

**Status:** open, disclosed, not resolved before submission.

The JSON files in `runs/` carry builder-authored labels and anchors,
transcribed from `evidence/07`, which states it was produced before any
diagnostician run. No run of the diagnostician folder against these specimens
was ever performed. `runs/README.md` previously described the JSON as
model-produced; that description was wrong and is corrected as of 2026-08-06.

**Why it cannot be resolved by running it now.** `examples.md` contains a
worked diagnosis of specimens 01 and 02 by name, including the primary class
and its anchors. Any run against these specimens with the diagnostician folder
loaded is an open-book test. A clean end-to-end run requires a specimen that
does not appear in `examples.md`.

**What is unaffected.** The deterministic layer. `verify.py` receives no tier,
no primary, and no refusal decision; it verifies anchors against source and
computes the result. That behaviour is reproducible offline and is what
`runs/` and `--test` demonstrate.