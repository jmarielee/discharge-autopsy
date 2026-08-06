# 10 — Run record, specimen-01 (open book)

**This run is contaminated and is published as contaminated.** `examples.md`
contains a worked diagnosis of specimen-01 by name, including its anchors. That
file was loaded in the Project. The model had the answer sheet in the room. No
claim of blindness is made here and none can be.

It is filed anyway because of what it did with the answer it was given.

## Conditions

**Date:** 2026-08-06
**Specimen:** `specimens/specimen-01-post-op-visit-summary.md`, alone. Not the
01+02 pair.
**Rung:** AUTHOR
**Pre-registration:** none. This run was not planned. It was performed by
mistake, in a Project opened for a different specimen. Recorded as accidental
rather than presented as designed.
**Loaded:** `identity.md`, `rules.md`, `examples.md`, `reference/taxonomy.md`,
`reference/disguised-asks.md`, `reference/verdict-schema.md`.
**Runs performed:** one. No re-roll.

Output at `runs/specimen-01-threshold-absence-OPEN-BOOK.txt`.

## What it returned

`THRESHOLD_ABSENCE` at P2, locus `observability`, anchored to two instructions to
act whose governing criteria the document never quantifies.

## Why a contaminated run is worth publishing

`examples.md` primes `ACTION_DIVERGENCE` at P1 for this specimen and files
`THRESHOLD_ABSENCE` as a **demoted symptom**, quoting the same anchor this run
promoted to primary. The open-book answer was available verbatim.

The model did not give it. Fed specimen-01 without its companion document, it
ruled out `ACTION_DIVERGENCE` on the ground that the divergence requires a second
document — "eliminated on set contents, not on strength" — and promoted the P2
that `examples.md` had demoted.

Contamination normally shows as recitation of the primed answer. This is the
model declining the primed answer and stating a structural reason tied to the set
actually in front of it. That is evidence about the ranking, not proof, and it is
the strongest signal available from a run that cannot be blind.

Two further behaviours were unprompted:

- It flagged `CONTACT_ABSENCE` as possibly an artifact of the builder's own
  redaction rather than a property of the original document, and declined to
  assert it. The Redaction rule in `PROTOCOL.md` anticipates this case; nothing in
  the loaded folder instructs the model to apply it.
- Its `WOULD FLIP THIS` field names the arrival of a second document as a
  condition that would overturn its own verdict.

## Anchor verification

All eight quoted spans were checked against
`specimens/specimen-01-post-op-visit-summary.md` and match on whitespace-normalised
comparison. None fabricated. G1 did not run: the output is rendered text, not the
JSON `verify.py` ingests.

## What this does not establish

**Not a blind run, and never can be.** Any future run against specimens 01 or 02
carries the same contamination for as long as `examples.md` contains their worked
diagnosis.

**Not machine-verified.** No `runs/specimen-01.json` exists; the anchors were
confirmed by script outside the gate table.

**Not pre-registered.** Every other run in this repository was pre-registered
before execution. This one was an accident, and the record says so rather than
retrofitting an intention.
