# Seeded corpus spec

**Build this Sunday, before reading any real specimen closely.**

Three reasons, in order of importance:

1. **It stops you fitting discriminators to your data.** If you read eight real sheets
   first, your taxonomy will be a description of those eight sheets rather than a
   discriminating instrument. Write the seeded specimen from the taxonomy, then let the
   real documents test it.
2. **It is your test harness.** Every gate needs something to fire on.
3. **It is your floor.** Arjen Stet shipped a plan with 23 seeded flaws, the answer key,
   and a cold run that caught all 23, and got an honorable mention with it. Falsifiable in
   two minutes is a real result.

---

## What to build

**`tests/seeded/specimen.txt`** — a synthetic discharge instruction sheet for the chosen
procedure class. Realistic length and register. Written to read like a real institutional
document, not like a list of planted errors.

**`tests/seeded/answer-key.md`** — every planted defect, with:
- the defect ID and its taxonomy cause
- the exact span that carries it
- which cause it should be attributed to
- whether it should be the **primary** cause or filed as a symptom

**`tests/seeded/README.md`** — how to run it, what a correct result looks like, and how a
reader can falsify the claim in under two minutes.

---

## Composition

Plant **10–14 defects**, distributed so the instrument has to discriminate rather than
enumerate:

| Count | Purpose |
|---|---|
| 1 | The **intended primary cause** — highest severity, clearly clears the separation threshold |
| 2 | **Near neighbours** of the primary, from the confusable pairs table. These test discrimination, and they should be *filed as symptoms*, not named. |
| 4–6 | Genuine secondary defects across other taxonomy causes. All should be filed as symptoms. |
| 2 | **Readability noise** — D8-flavoured findings that are real but must not win. If D8 comes back as primary, the separation threshold is mistuned. |
| 1 | A **plausible person-blame trap** — something that reads naturally as "the caregiver got it wrong." If the instrument names it, the locus rule has failed. |

---

## The second specimen: the abstention case

**`tests/seeded/specimen-adequate.txt`** — a discharge sheet that is genuinely fine.
Clear, complete, feasible, internally consistent, at an appropriate reading level.

The correct output is **ABSTAINED**. Anything else means the locus rule is manufacturing
a defect to satisfy its own constraint, which is the false positive a judge finds in four
minutes.

**Ship the abstention receipt.** Publishing the failure your own rule creates is the
highest-scoring move available in this competition, and it is the thing that separates
this build from every other diagnostician in the field.

---

## The third specimen: the decline

**`tests/seeded/specimen-out-of-scope.txt`** — a document from outside the procedure class,
or a document that is not a discharge sheet at all.

The correct output is a **refusal**, stating the scope boundary. Ship the receipt of a
real decline rather than describing the behaviour in prose.

*This is a returning strength. The Taper Editor's scope gate was specifically praised for
exactly this, and the feedback's only criticism was that the decline lived as a
parenthetical in `rules.md` instead of as a shipped transcript. Do not repeat that.*

---

## The disguised-ask fixtures

`tests/fixtures/` — one negative fixture per gate in the enforcement spec, and one per
disguised ask in the catalogue. Each blocked on its **own named check**, so a failure tells
you which gate caught it.

Then the **coverage assertion**: a test that iterates the gate table and fails if any gate
lacks a negative fixture. No gate ships unverified.

---

## Cold-run protocol

Before running the seeded specimen through the instrument:

1. Commit the specimen, the key, and the frozen codebase. Record the hash.
2. Run it in a **fresh chat** with no access to `tests/` — the diagnostician must never
   read its own test material. (Marcelo's load-versus-verify split: the folder is the
   product, `tests/` is evidence *about* the product.)
3. Paste the transcript verbatim into `runs/`, errors included.
4. Score against the key. Record misses in `OPEN-DEFECTS.md`.
5. **Do not fix anything until every specimen has been run.** Then fix, and ship the
   corrected re-run as a separate labeled receipt so both behaviours stay on the record.

---

## What the README should be able to claim

> `python3 diagnose.py tests/seeded/specimen.txt` names D-[n] as the primary cause and
> files the remaining [n] planted defects as symptoms, matching `answer-key.md`.
> `tests/seeded/specimen-adequate.txt` returns ABSTAINED.
> `tests/seeded/specimen-out-of-scope.txt` returns a scope refusal.
> `python3 verify.py --selftest` blocks [n]/[n] broken outputs, each on its named check.
>
> Two minutes, no API key. If any of that is untrue, the build is falsified.
