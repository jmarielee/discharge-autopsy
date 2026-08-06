# Verdict schema

Every run returns exactly one of four structures: a verdict, a refusal, an unresolved tie,
or a scope decline.

---

## 1. Verdict

```
PRIMARY DEFECT     One class from the closed taxonomy. Exactly one.
TIER               P1–P6. Determines the primary; not chosen.
LOCUS              The document property the defect resolves to. Must be a member of
                   the locus schema. Cannot be an execution-side fact.
ANCHORS            Verbatim spans from the specimen, with locations. String-matched.
CHAIN              defect → mechanism → the failure a caregiver would experience.
                   Each link cites an anchor.
RULED OUT          The two strongest alternative classes, each with the specific
                   evidence that eliminated it.
WOULD FLIP THIS    What would have to be shown to change the verdict.
FILED AS SYMPTOM   Everything else observed, demoted, each with a reason.
RESOLUTION PATH    Fixed string. Not generated, not varied.
```

`RESOLUTION PATH` is always, exactly:

> Bring this document to the discharging clinician or a pharmacist.

---

## 2. Refusal

Returned when the threshold in `rules.md` §4 is not met.

```
RESULT             REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE
ANCHORED DEFECTS   The candidates found, with tiers and anchors.
WHY REFUSED        Which of the two threshold conditions failed.
WOULD RESOLVE      The specific evidence that would lift this above threshold.
RESOLUTION PATH    Fixed string.
```

A refusal is a valid output. The instrument is more useful for being able to return one.

---

## 3. Unresolved tie

Returned when two or more defects share the top tier and survive all three tie-breaks.

```
RESULT             TIE_UNRESOLVED
TIED CANDIDATES    Each with class, tier, anchors.
BREAKS ATTEMPTED   The three break rules and how each failed to separate.
WOULD RESOLVE      What would discriminate between them.
RESOLUTION PATH    Fixed string.
```

---

## 4. Scope decline

Returned when the request is not a diagnosis of an artifact set.

```
RESULT             OUT_OF_SCOPE
REQUEST TYPE       Named. If it is a disguised rewrite, name which disguise.
WHY                The rule that excludes it.
RESOLUTION PATH    Fixed string.
```

---

## Fields that do not exist

There is no `RECOMMENDATION`, `FIX`, `SUGGESTED WORDING`, `IMPROVED VERSION`, or
`NEXT STEPS`. The absence is the enforcement. A fix has nowhere to be written.
