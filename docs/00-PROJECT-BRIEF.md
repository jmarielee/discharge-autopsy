# The Discharge Autopsy — project brief

Written 2026-08-01. This file stands alone: paste it into any chat that has no prior context.

---

## The competition

Cliefnotes Comp #10, **The Diagnostician**. Due **Saturday 8 August 2026, 11:59 PM EST**.
Winner announced 15 August. Prize: a Lyceum seat. Premium/VIP only.

**The brief.** Build a folder-based AI diagnostician that reads something broken and says
*why* it broke. Not how to fix it. Five things in the folder: `identity.md`, `rules.md`,
`examples.md`, `reference/`, `README.md`. Drop it in a Claude Project and Claude becomes
the diagnostician.

**The bar, verbatim from the brief:**
1. It names ONE primary cause. A ranked list is a symptom inventory, not a diagnosis.
2. It shows its reasoning — what in the artifact points there.
3. It separates cause from symptom.

If the output is a checklist, it's an audit tool. If it rewrites, it's an editor. If it
jumps to "try this instead," it's a consultant. None of those are the assignment.

**Judged on:** does it actually diagnose · is the domain specific enough · is the
methodology clean (each file one job) · README quality for a stranger.

**Submission:** public GitHub repo link in the comments, plus 2–3 sentences on what it
diagnoses and who it's for.

---

## Author context

Jodi Paige-Lee. Senior product designer, intelligence layer design. 62, athlete,
caregiver in a household where her husband has memory issues. Comp #9 entry
(`jmarielee/taper-editor`) took an **honorable mention**.

**Her thesis, which every build expresses:** *the model labels what it sees; the math
decides the outcome.* Deterministic guardrails over a probabilistic core, with a
human-in-the-loop audit point.

**Prior repos:** `jmarielee/taper-editor` (best — receipts, offline verifier, third-party
specimens), `jmarielee/job-fit` (strongest idea, deterministic scoring engine,
Evidence Ledger), `jmarielee/debrief-specialist` (weakest against this rubric — no
enforcement in code, no receipts).

---

## What Comp #9's judging actually rewarded

Read from all 42 feedback files. The "what would have moved you up a tier" lines tally to
four failure modes:

| Failure mode | Count |
|---|---|
| **Proportion** — one file swallowing another's job | ~14 |
| **No run by a third party** on an artifact you didn't make | ~9 |
| Reference layer too thin for the rules' claims | ~7 |
| Structural clutter, duplicated files, scaffolding in front of the product | ~6 |
| Domain too broad | ~5 |

**Jodi's own deduction was proportion.** Her `examples.md` was 6,053 words, the largest
file in the field. Feedback: *"The evidence here is genuinely top-five and the folder's
shape is what held it back. Same specimens, moved one directory over, and this reads
differently."* This must not happen twice.

**The winner's distinguishing move.** Marcelo Michelsohn pre-registered his method —
runtime, inputs, preservation rule, and the stated assumption that his tool made at least
one mistake — dated and committed *before* he ran anything. That converted receipts from a
highlight reel into evidence. He was told: *"Nothing. You are at the top of this one."*

**Mechanics worth stealing, by name:**
- **Gabriel Azoulay — Rule 0.** Every quoted span must be a verbatim substring of the
  input, checked by string match, not by a reader inclined to trust confident prose.
- **Joshua Hubbard — a schema with no field a fix could live in.** Structural refusal
  rather than a promise. *"The closest a plain-text system gets to a compile error."*
- **Alex Brown — coverage assertion.** A test that asserts every gate has a negative
  fixture, so nothing is left unverified.
- **Alex Brown — honest labels.** `ILLUSTRATIVE` / `CONSTRUCTED` / `REAL`, with `REAL`
  deliberately empty. It cost him placement and the judges said it was still right.
- **Nicolas Patron — publish the defect your own gate cannot see**, and fix the *rule*
  rather than patching the detector against one observed miss.
- **Arjen Stet — seeded corpus with the answer key attached.** Falsifiable in two minutes.
- **Marcelo — load vs. verify split.** The folder is the product; `tests/` is evidence
  *about* the product; the diagnostician never reads its own test material.
- **Gabriel — the best README in the field:** quickstart, offline verification with no
  API key, an explicit list of what it cannot do, a six-minute judge protocol.
- **Craig Howard — `CREDITS.md`** naming where each borrowed idea came from. Matters here
  because Comp #9 enforcement machinery is being reused in an adjacent domain.

**Skip:** any build-record or pipeline folder (Alex was dinged for `build/` sitting
between a stranger and the product). Any duplicate-copy experiment. Anything that adds a
folder rather than a receipt.

---

## The build

**The Discharge Autopsy.** A diagnostician that reads a written discharge or
post-procedure instruction sheet that a patient or caregiver could not follow at home,
and names the **one primary defect in the document** that caused it.

**Procedure class:** ONE, chosen before collecting anything. Recommended:
**post-operative orthopedic discharge** — high volume, heavy home-care burden, and the
instructions almost always assume a second able-bodied adult is present.

**User:** the caregiver or discharge planner reviewing instructions before they go home.
Not the patient. Never a clinician making a care decision.

**Example verdict shape:** *the medication schedule requires the caregiver to perform a
dose conversion the sheet never states, at a 2am interval, in a document written at grade
11 — the arithmetic error it invites is the one the reported failure describes.*

### The locus rule — the core idea

The diagnostician is **structurally forbidden from naming the person as the cause.**
"Non-compliant patient," "the family didn't follow through," "they didn't understand"
are classified as symptoms. It must keep searching until it finds something in the
document.

That phrase appears in medical records constantly and is usually a defect in a document
written by a clinician for another clinician. Forbidding it produces a diagnosis that is
both surprising and correct.

**Enforced structurally, not lexically.** A word-list check catches "non-compliant." It
does not catch *"the caregiver administered the wrong dose"* — person-blame restated as
observation, which sails through a lexical gate wearing the tool's own credibility. The
fix: the verdict's **locus field must resolve to a property of the document object.**
Execution-side facts are admissible as evidence but can never be the locus.

**And the rule can be wrong.** Sometimes the document was fine. A tool structurally
forbidden from saying so will manufacture a defect to satisfy its own constraint. The
answer is an **abstention verdict** — when the search exhausts the label set, it says so
and names the evidence that would resolve it, rather than inventing a cause. Ship a
specimen where it abstains for exactly that reason. *Publishing the failure your own rule
creates is the highest-scoring move available.*

### The safety boundary — in the schema, not the prose

This is a sensitive domain. Drift toward medical advice is fatal, not a deduction.

- The verdict addresses **document properties only**: readability, arithmetic the reader
  must perform unaided, schedule feasibility, internal contradiction, unstated
  prerequisites.
- It **never** addresses the clinical content of an instruction. It cannot say a dose is
  wrong — only that the sheet requires an unstated conversion to arrive at one.
- **Every output terminates at the discharging clinician or pharmacist** as the resolution
  path. A caregiver who reads "this sheet is defective" and improvises is a worse outcome
  than the confusion you started with.

That terminal-routing constraint is also the sharpest differentiator: it is Hubbard's
no-field-a-fix-could-live-in move, applied where the stakes make its necessity obvious.

**Precedent that this is a returning strength, not a risk:** the Taper Editor's scope gate
refused non-endurance plans and refused physiology, and the judges specifically praised
shipping the receipt of a real decline rather than describing the behaviour.

---

## Evidence ladder

Labeled honestly in the README. Alex Brown's discipline: ship what you have, name what
you don't, never stretch a rung.

| Rung | What it is | Status |
|---|---|---|
| **SEEDED** | Synthetic sheet with N planted defects + answer key. Proves the mechanism. | Build first, this weekend |
| **PUBLIC** | Real institutional documents from open patient-education libraries. Proves it works on real writing. | Downloadable tonight |
| **AUTHOR** | Sheets from the author's own household, redacted, declared as her own. | In hand |
| **PRACTITIONER** | A nurse or PT's observed account of a real failure of a real sheet. | **The one ask that matters** |

**PUBLIC carries a property almost nothing in Comp #9 had:** a judge can re-download the
exact PDF and independently verify every quoted span. Most of that field shipped specimens
nobody could check.

**A rung that was considered and DROPPED — do not resurrect it.** "REPORTED": pairing a
public PDF with forum accounts of confusion. That gives a document *type* plus separate
anecdotes, not a documented failure of that document. The judges clone repos and execute
self-tests; this is exactly the claim that gets caught. Let the practitioner interview
carry the observed failure instead.

---

## Ideas considered and rejected

Recorded so they aren't re-litigated.

- **Adherence / Race / Plateau / Stall Autopsy** (endurance and lifting). Strong, but
  specimen supply depended on one busy coach's calendar and an unconfirmed log export.
- **The Log Autopsy** (nutrition logging errors, with coach Natalie's sealed cases).
  Highest ceiling in the whole set — an expert answer key written before she sees output
  is evidence nobody in Comp #9 had. **Rejected for Comp #10 on variance, not merit:** two
  unconfirmed dependencies, one of them a person's reply inside 72 hours. **Decoupled, not
  cancelled** — it runs properly in September as Phase 1 of the Natalie project, with a
  recorded interview and unrushed consent.
- **Support Chat Autopsy, Reposted Req Autopsy, Review Evidence Autopsy, Prompt Autopsy,
  Recipe / Group Chat / Gift / Trip Day / Fridge / Booking / Rulebook Autopsies.** All
  viable; all lost on either specimen supply, domain authority, or the author's actual
  interest.

---

## Files in this project

- `PROTOCOL.md` — pre-registration. **Commit dated, before any specimen is read.**
- `01-build-blueprint.md` — folder shape, word budgets, seven-day plan
- `02-enforcement-spec.md` — locus rule, verdict schema, disguised-ask catalogue, verifier
- `03-failure-taxonomy-draft.md` — candidate causes and their discriminators
- `04-practitioner-ask.md` — the nurse/PT message and the interview guide
- `05-seeded-corpus-spec.md` — the synthetic sheet and its answer key
