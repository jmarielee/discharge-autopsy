# Run record — specimen-06

**Specimen.** `specimens/specimen-06-va-bariatric-soft-diet.md`, a text extraction of
*Bariatric Surgery Soft Diet Stage Nutrition Therapy* (03/2023), published by the U.S.
Department of Veterans Affairs, Nutrition and Food Services. One document, four pages.
PUBLIC rung; U.S. Government work in the public domain. Both the source PDF and the
extraction are committed.

**Pre-registered** at `2da2136`, before the PDF was converted or read. See `PROTOCOL.md`,
amendment 2026-08-07 (specimen-06 pre-registration), including the commit-order
disclosure.

**Selection.** Chosen by Google Gemini with no access to this repository, its taxonomy,
its schema, or any prior run. Both selection prompts are committed verbatim in the
amendment. The builder did not choose the specimen.

**Run.** Fresh Claude Project loaded with `identity.md`, `rules.md`, `examples.md`, and
`reference/` only. One run. No re-roll, no follow-up prompts.

---

## Contamination: the specimen header was not stripped

**This is stated before the result because it bears on the result.**

The extraction file carries a header comment block recording provenance. It was not
removed before the specimen text was pasted into the diagnostician project. The model
read it. Verbatim:

```
SPECIMEN 06
Source: U.S. Department of Veterans Affairs, Nutrition and Food Services
URL: https://www.nutrition.va.gov/docs/UpdatedPatientEd/BariatricSurgerySoftDietStageNutritionTherapyMar2023.pdf
Accessed: 2026-08-07
Rung: PUBLIC — U.S. Government work, public domain
Selected by: Google Gemini, no repository access. See PROTOCOL.md amendment 2026-08-07.
Procedure class: bariatric surgery (widened for this specimen only)
Extraction: tools/pdf_to_text.py, 6447 chars, inspected and clean
Single document, not a set. ACTION_DIVERGENCE structurally unreachable.
```

The last line is the damaging one. The model was told, in its input, that the taxonomy's
P1 class could not apply to this specimen. It returned a P2 primary.

**What the model did with it.** It disputed the annotation rather than accepting it. Its
own words: the locus schema defines `internal_consistency` as contradiction "within or
across sheets," so the class is reachable inside a single document. It then tested
`ACTION_DIVERGENCE` anyway, produced an anchored candidate — the Grains row recommending
short pasta against the narrative warning that refined carbohydrates expand — and
eliminated it on the class definition, on the ground that a food listing is not an
observable finding and the narrative span assigns no required action.

That is better behaviour than compliance. It is also not independence.

**What this run therefore does not show.** The elimination of `ACTION_DIVERGENCE` cannot
be treated as independent. A reader cannot distinguish elimination on the evidence from
elimination in the presence of an instruction, and neither can the builder. The primary
defect named here is a P2 arrived at by a model that had been told P1 was unavailable.

The model also knew it was a test specimen, that it had been externally selected, and
that its output would be examined. Any unusual rigor in the `RULED OUT` section should be
read in that light.

**Not corrected by re-running.** The pre-registration states that the first run is the
shipped run, with no re-roll. The extraction was clean and the anchors are verifiable, so
this is not the OD-8 case, where a defective conversion made anchors unverifiable. The
contamination is bounded, nameable, and disclosed. The run stands.

---

## Result

```
PRIMARY DEFECT     THRESHOLD_ABSENCE
TIER               P2
LOCUS              observability
```

The document's governing stop rule is a sensation — stop eating when no longer hungry —
stated twice. The same paragraph states that the criterion has changed after surgery and
does not describe how. No substitute cue appears anywhere in the four pages. The numeric
figure in the set is a planning ceiling the next sentence defers, with no rate or
increment given for the progression, so a reader cannot convert it into a stop rule for
the current meal.

Full output: `runs/specimen-06-threshold-absence.txt`.

## Anchor verification

**17 of 17 anchors verified verbatim against the source. Zero fabricated.**

Checked by script (`check-anchors.py`), whitespace flattened and smart punctuation
normalised, as with specimens 04, 05, and 01. G1 has never run on a live output because
`verify.py` ingests JSON and the model returns text; see OD-7. This is the largest anchor
set any live run has produced and the first in a procedure class the taxonomy was not
built for.

## Refusal threshold

Three anchored defects; highest tier P2; one class at P2; no tie. Both conditions met:
total ≥ 2, and one defect at P3 or higher. The threshold did not fire.

## What this changes for OD-5

OD-5 states that no blind run has named a primary defect. A blind run has now named one.

The gap narrows rather than closes, for three reasons:

1. No independent answer key exists for this specimen. The run shows that a blind
   specimen can produce a primary; it does not show that this primary is correct.
2. The header contamination above bears directly on which class was named.
3. The specimen is a single document, so the taxonomy's P1 class was reachable only
   through a within-sheet reading. Whether that reading is right is itself unsettled.

## Observations the instrument could not file

The model surfaced two findings and stated that neither was a finding, because no class
covers them: the low end of the sample meal plan's water rows totals less than the stated
daily fluid goal, and the compound timing demand of four to six meals, twenty to thirty
minutes each, separated from liquids by thirty minutes, is never totalled. Both fall in
`arithmetic_demand` and `schedule_feasibility`, two of the five locus properties with no
matching defect class.

This is the second time a live specimen has walked into that gap. The first was the
practitioner session, `evidence/08`. The gap is documented in `reference/taxonomy.md` and
is not patched here.

The model also flagged a `FIELD_INCOMPLETENESS` candidate — an empty cell in the Food
Choices table — and noted on its own that an empty cell is not distinguishable from an
extraction artifact in a text conversion of a PDF table. That is the OD-8 failure mode
recognised from inside a run.
