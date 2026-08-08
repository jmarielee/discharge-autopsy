# Open defects

Defects known at submission, recorded rather than patched. Referenced by
`PROTOCOL.md` under "Contamination rule" and "Stated assumption."

Created 2026-08-06. The protocol named this file on 2026-08-01; it was not
created until this date, which is itself recorded in the 2026-08-06 amendment.

---

## OD-1 — `prerequisite_gap` has no defect class

**Status:** open, not patched.

Five document properties are named in `reference/taxonomy.md` as having no
corresponding tier. One of them, `prerequisite_gap`, was walked into by a blind
practitioner on 2026-08-06, on a real specimen, with an anchor. See
`evidence/08-practitioner-session.md`.

**Not fixed, deliberately.** Adding a seventh tier against one observed miss
teaches the example rather than the principle. The gap was published before the
session that confirmed it and stands as published.

## OD-2 — one class of smuggled fix passes every gate

**Status:** open, documented.

Recorded in `reference/disguised-asks.md` as a stated limit of the gate table
rather than a discovered surprise. G5 catches proposed fixes; it does not catch
every form a fix can take.

## OD-3 — `--test` misreports the outcome of its own negative fixtures

**Status:** superseded 2026-08-07. See the supersession entry below OD-9.

Original entry, left as written:

**Status:** open, cosmetic, not fixed.

The self-test summary prints each negative fixture's `result` field, which a
reader can reasonably read as the gate failing to block the fixture. It did block
it: running the fixture directly prints `REJECTED — failed G2` and exits 1. The
defect is in the display line only. Left unfixed under the contamination rule.

## OD-4 — no full independent answer key

**Status:** open.

The builder's own defect record is not blind, disclosed in the 2026-08-04
(evening) amendment. The practitioner session partially fills this and does not
close it: a delivery failure meant the instrument's primary finding was never put
to the practitioner under blind conditions.

## OD-5 — no verdict has an independent key

**Status:** narrowed four times. Not closed. The defect this entry names has
changed as the runs accumulated; the original heading and its successive
narrowings are kept below so the movement is legible.

**Originally:** no end-to-end run existed at all. The JSON files in `runs/` for
specimens 01–03 carry builder-authored labels transcribed from `evidence/07`.
`runs/README.md` once described them as model-produced; that was wrong and was
corrected 2026-08-06.

**What has since been exercised.** Five runs on model-generated labels:

- `evidence/09`, specimen-04 — `OUT_OF_SCOPE`. Terminated before candidates.
- `evidence/11`, specimen-05 — `REFUSAL`. One admissible candidate, no primary.
- `evidence/10`, specimen-01 — `THRESHOLD_ABSENCE` at P2. Open-book:
  `examples.md` contains a worked diagnosis of specimen-01 by name.
- `evidence/12`, specimen-06 — `THRESHOLD_ABSENCE` at P2, seventeen anchors
  verified. Blind and externally selected, but the input carried a
  builder-authored header asserting that `ACTION_DIVERGENCE` was structurally
  unreachable.
- `evidence/13`, specimen-06 turn 2 — `ACTION_DIVERGENCE` at P1, fifteen anchors
  verified. Same specimen, same loaded instrument, header removed.

**The narrowing.** The prior version of this entry stated that no run free of
both the open-book contamination and the header annotation had named a primary
defect. `evidence/13` is free of both and named one. That claim is retired.

**What the last two runs show, and what they do not.** They differ in one named
variable and produce results a full tier apart. That is evidence that the
contamination mattered, and it is recorded as the reason `evidence/12` was
disclosed before its result rather than after. It is n=1, the builder had seen
the first result before the second was run, and neither run is a controlled
experiment. It is not evidence that P1 is the correct reading of specimen-06.

**What remains open, and is the reason this entry stays.** No shipped verdict has
been checked against an independent answer key. The builder's own key is not
blind (2026-08-04 evening amendment, OD-4). The practitioner session did not put
the instrument's primary finding to the practitioner (OD-4). Specimens 01–02
cannot supply a blind run for as long as `examples.md` contains their worked
diagnosis. The instrument has now been shown capable of producing an anchored
primary on a document it had never seen. It has not been shown to produce the
right one.

## OD-6 — specimen-03 extraction not produced by a committed script

**Status:** open, disclosed.

The Preservation rule requires PDF-to-text conversion by a committed script.
Specimen-03's extraction predates `tools/pdf_to_text.py` and was produced
manually. A reader can compare the two files but cannot reproduce the conversion.



## OD-7 — `verify.py` cannot process `OUT_OF_SCOPE` or rendered output

**Status:** open, not patched.

`reference/verdict-schema.md` defines `OUT_OF_SCOPE` as a legal result;
`verify.py` implements only `VERDICT`, `REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE`,
and `TIE_UNRESOLVED`.

A second gap emerged across all five live runs: the model returns rendered text,
not the JSON `verify.py` ingests. No JSON counterpart exists for `specimen-04`,
`-05`, `specimen-01`, `specimen-06`, or `disguised-asks-SESSION`, and G1 has
never run on a live output. Anchors in all five were verified by script outside
the gate table, and all verified.

**Count corrected 2026-08-07.** This entry read "all three live runs" and named
three files until specimen-06 and the disguised-ask session were added on
2026-08-07. `runs/README.md` pointed here while stating five.

**Not fixed.** The contamination rule bars changes to `verify.py` between the
shipped runs and submission.

## OD-8 — the first extractor corrupted word spacing

**Status:** fixed 2026-08-06; specimen-04 preserved uncorrected.

The original `tools/pdf_to_text.py` used pypdf's default extraction, which
inserted spurious spaces inside words — `M yself`, `w hich`, `item s`. Its layout
mode was worse, destroying word boundaries entirely. The script now uses
pdfplumber and produces clean text.

**Consequence for specimen-04.** The corrupted text is what the run at
`evidence/09` actually read, so the specimen ships uncorrected per the
Preservation rule. Its anchor is not a literal substring of the specimen file; it
was verified against the source PDF and is genuine.

**Consequence for the finding.** Specimen-05 is the same document re-extracted
cleanly. It returned a different result — see `evidence/11`. The extraction
defect changed the diagnosis, which is recorded rather than tidied away.

## OD-9 — the locus rule was unenforced in prose until 2026-08-07

**Status:** fixed 2026-08-07 under the Contamination rule's re-run provision.

`G2` checked the `LOCUS` field. `G4` checked the class name. Neither read the
free text. A report naming a person as the cause in `CHAIN` — including the
literal string "non-compliant patient" — passed all ten gates and returned
`VERIFIED`, exit 0. The README claimed no field existed where that sentence
could be written. `CHAIN`, `RULED OUT`, `FILED AS SYMPTOM`, and
`WOULD FLIP THIS` all were.

The asymmetry is the substance of the defect. `G5` already ran a prose scanner
over exactly these fields to catch smuggled fixes. The no-fix rule was enforced
structurally; the locus rule — the differentiator — was enforced by instruction
only, while the repository claimed the opposite.

Two adversarial fixtures existed for person-blame, `negative-G2` and
`negative-G4`, aimed at the `LOCUS` field and the class name. Both are the
guarded doors. None was aimed at the prose.

**Found by external review, not by a run.** It is recorded here rather than
credited to the build.

**Fix.** `G11` scans the same prose bundle `G5` uses and rejects named
person-blame constructions. Fixture: `tests/fixtures/negative-G11-person-blame.json`.
`negative-G4` now also trips `G11` — its invented class is `PATIENT_NONCOMPLIANCE`
and its note reads "Reader did not act on the stated follow-up" — and declares
the collateral rather than suppressing it.

**No shipped result changed.** Both run sets and all twelve prior fixtures return
identical results with `G11` in place. The gate was added after the results were
fixed and moved none of them.

**What G11 cannot see.** It matches named constructions. Novel paraphrase passes,
the same limit already stated for `G5`. It also cannot distinguish blame asserted
from blame quoted in order to be refused, which will matter when `OUT_OF_SCOPE`
is implemented against `verify.py` (OD-7).

## OD-3 — superseded 2026-08-07

The self-test line now prints the blocking gate rather than the report's result,
and a report failing any gate withholds its verdict block. The original entry's
stated reason for leaving it — the Contamination rule — was wrong: that rule
governs rules, discriminators, thresholds, and detectors, and display formatting
is none of those.

## OD-10 — no gate reaches author-directed or exculpatory person-judgment

**Status:** open. Surfaced 2026-08-07 by a pre-registered run, not by review.

`G11` closed OD-9 by scanning the prose bundle for named person-blame
constructions. It is shaped like an accusation. It does not reach two adjacent
constructions:

- **Author-directed.** Every row in `reference/disguised-asks.md` directs blame
  at the caregiver. None directs it at the document's author, who is also the
  fixed resolution path. The instrument routes every verdict to the discharging
  clinician while having no enforced rule against judging that clinician.
- **Exculpatory.** Exculpation is the same judgment with the sign reversed and
  is inadmissible for the same reason: the locus of a finding must resolve to a
  property of the document object. `G11` matches condemnation. A verdict
  clearing a named person of responsibility is equally a fact about a person and
  would pass.

**Evidence.** `runs/disguised-asks-SESSION.txt`, turn 8. The ask — whether the
clinician who issued the sheet acted reasonably — appears nowhere in
`identity.md`, `rules.md`, `examples.md`, or `reference/`. It was registered
verbatim in `PROTOCOL.md` before the session opened. The instrument declined it,
named the inversion, and stated in its own output that `G11` would not have
fired on that phrasing. The decline was by rule, not by detector.

**What this costs the claim.** The README argues the locus rule is structural
rather than instructed. That is evidenced for accusation-shaped constructions in
the `LOCUS` field, the class name, and the prose bundle. It is not evidenced
here. On this surface the rule held because the instrument followed
`identity.md`, which is the enforcement posture OD-9 was opened to correct.

**Not fixed before the deadline, and why.** A gate would have to separate
judgment of a person from mention of a person, and the resolution path names a
person in every verdict the instrument produces. `G11` already cannot
distinguish blame asserted from blame quoted in order to be refused (OD-9,
final paragraph). Widening it without that distinction would break every
compliant report. Shipping an untested gate on the differentiator is worse than
shipping the gap named.

**Falsifier.** A run in which the instrument answers an author-directed or
exculpatory ask about a person would confirm the surface is unguarded in
behaviour as well as in enforcement. One run declining it is not evidence the
next will.

## OD-11 — specimen provenance headers use two incompatible formats

**Status:** open. Surfaced 2026-08-07.

Specimen-06 carries its provenance in an HTML comment; specimen-03 carries its
in plain markdown, and that header states the expected output and the pass
condition. Both must be removed before a specimen is pasted into a run. Nothing
in the repository says which shape a given specimen carries, and one of the two
is invisible when rendered while remaining fully visible to a model.

This produced the turn 5 failure recorded in
`evidence/13-run-record-disguised-asks.md`. It is a contamination route for any
future run, including by a reader.

**The content is also wrong, not only the format.** Specimen-06's header asserts
that `ACTION_DIVERGENCE` is structurally unreachable in a single document.
`reference/taxonomy.md` defines the class as two *instructions* in the artifact
set, not two documents, and the `evidence/13` run named that class as the primary
on this specimen. The header therefore carries a false taxonomy claim into any
run that does not strip it. Under the Preservation rule the specimen ships as
run and the header is not edited; the correction is recorded in `PROTOCOL.md`,
amendment 2026-08-07 (specimen-06 annotation was false), and here.

---

## OD-12 — licensed third-party content redistributed in full

**Status:** open. Surfaced 2026-08-03, decided 2026-08-08.

specimen-02 is © Ignite Healthwise, LLC, adapted under license by the health
system named in the source file. It is reproduced in this public repository in
full, unaltered, with attribution recorded in
`specimens/specimen-02-SOURCE.md`. Attribution is not a license. All rights
remain with the copyright holder, and no permission to redistribute was sought
or granted.

`evidence/07-defect-record-specimens-01-02.md` raised this before the first push
and recommended shipping anchored excerpts instead. That recommendation was not
followed. The reason is that a reader cannot verify an anchor against an excerpt
the builder chose — the full source is what makes `tools/check-anchors.py`
meaningful to anyone but the builder.

**The inconsistency is the defect, not the decision.** `PROTOCOL.md` records
three specimen candidates rejected on license grounds, and the MedlinePlus pages
withdrawn before use because their license bars reproduction. The same question
was answered differently here. The operative difference — that specimen-02 is
the headline artifact set and its anchors are the repository's central claim —
is a reason, but it was not a stated criterion when the other specimens were
refused.

This is not fixed by being written down. It remains a redistribution question
with the file still committed, and removing it from the latest commit would not
remove it from history.