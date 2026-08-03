# Failure taxonomy — draft

This becomes `reference/failure-taxonomy.md`. It is the file that carries the build:
every cause needs a **discriminator** — the evidence that is consistent with this cause
and *not* with its neighbours. A taxonomy without discriminators is a list, and a list
produces an audit rather than a diagnosis.

**Closed set.** The instrument may name a cause from this list or abstain. It may not
invent one. Target 8–12 causes; more than that and the separation threshold stops
discriminating.

**Every cause below resolves to a document property.** None of them can be restated as a
fact about a person. If a candidate cause can only be phrased as something the reader did,
it does not belong in this file.

---

## D1 — Unstated conversion

**Locus:** `arithmetic_demand`

The document states a quantity in one unit and the available form in another, without
stating the conversion. The reader must derive it.

**Discriminators:** a dose stated in mg where the dispensed form is a concentration; a
volume stated without the strength it assumes; a frequency stated as "every N hours" with
a daily maximum stated in a different unit; any place two numbers must be combined to
produce an action.

**Not to be confused with D2** — the conversion here is *absent*, not *wrong*. The
instrument never evaluates whether a stated conversion is correct.

---

## D2 — Arithmetic demanded of the reader

**Locus:** `arithmetic_demand`

The document requires the reader to compute something — a total, a taper, a cumulative
cap, a running count — with no worked value supplied.

**Discriminators:** instructions containing "do not exceed" with no per-dose arithmetic
shown; tapering schedules stated as a rule rather than a table; two medications sharing an
active ingredient whose combined ceiling is stated only once.

---

## D3 — Schedule infeasibility

**Locus:** `schedule_feasibility`

The regimen assumes a household pattern the document never confirms.

**Discriminators:** an interval that necessarily places a dose between midnight and 6am; a
follow-up requiring a call during standard business hours; a step requiring the patient to
be transported on a day the document also restricts them from being alone; a frequency
that cannot be satisfied by a single caregiver within a waking day.

---

## D4 — Unconfirmed prerequisite

**Locus:** `prerequisite_gap`

The document assumes equipment, personnel, or a physical feature of the home that nobody
confirmed exists.

**Discriminators:** an instruction requiring a second able-bodied adult; assumed access to
a shower with a seat, a stair-free route, a refrigerator for a medication, a scale, a
thermometer; an instruction assuming the patient can reach or bear weight in a way the
same document restricts.

*This is the highest-yield cause in post-operative orthopedic discharge and the reason
that class was chosen.*

---

## D5 — Unobservable warning sign

**Locus:** `observability`

The document tells the reader to watch for something described in clinical rather than
observable terms.

**Discriminators:** a warning sign named by its clinical term with no lay description; a
threshold stated qualitatively ("excessive," "significant") with no comparator; a sign
requiring a measurement the household has no instrument for; "call if it worsens" with no
baseline established.

---

## D6 — Internal contradiction

**Locus:** `internal_consistency`

Two statements in the packet cannot both be followed.

**Discriminators:** two sheets giving different intervals for the same action; a
restriction on one page permitted on another; a discharge summary and a medication list
disagreeing; a printed default contradicting a handwritten amendment.

*Discriminator against D7: contradiction is two statements that conflict. D7 is one
decision with no statement at all.*

---

## D7 — Unresolved decision point

**Locus:** `completeness`

The document creates a situation it gives no rule for.

**Discriminators:** no stated rule for a missed dose; no rule for what to do if a symptom
appears outside the listed set; no re-entry rule after an interruption; a conditional
("if X, then Y") with no branch for not-X.

---

## D8 — Reading demand above the population

**Locus:** `readability`

The document is written above the reading level of the population it is handed to.

**Discriminators:** computed grade level against the benchmark in
`reference/readability-benchmarks.md`; clinical term density; sentence length distribution;
terms used before they are defined, or never defined.

*Weak as a primary cause on its own — a sheet can be readable and still unfollowable.
Usually a supporting finding. Say so in the taxonomy, and let the separation threshold do
its job rather than letting D8 win by default because it is the easiest to compute.*

---

## D9 — Navigability failure

**Locus:** `navigability`

The information exists but cannot be found at the moment it is needed.

**Discriminators:** time-critical information appearing only in a later section; the
emergency threshold placed after routine care; information split across non-adjacent
pages; no heading structure; a packet with no stated order of use.

---

## D10 — Instruction with no stated actor

**Locus:** `completeness`

The document states an action without stating who performs it, in a household where the
patient may not be able to.

**Discriminators:** passive-voice instructions ("the dressing should be changed") with no
named actor; an action the same document restricts the patient from performing; a task
requiring two hands, standing, or reaching where mobility restrictions are also stated.

---

## Discrimination rules

Written into `rules.md` with citable IDs. These are the pairs the instrument will most
often confuse, and each needs a stated separator.

| Pair | Separator |
|---|---|
| D1 vs D2 | D1 = the conversion is absent. D2 = the conversion is present but must be computed. |
| D3 vs D4 | D3 = timing the household cannot meet. D4 = a thing the household does not have. |
| D5 vs D8 | D5 = the sign is unobservable at any reading level. D8 = observable but written above the reader. |
| D6 vs D7 | D6 = two statements conflict. D7 = no statement exists. |
| D7 vs D10 | D7 = no rule for the situation. D10 = a rule exists with no actor named. |
| D8 vs anything | D8 wins only when no other cause clears the threshold. Never by computational convenience. |

---

## To fill from the practitioner interview

The parts of this file that cannot be reasoned into and must come from someone who hands
these documents out:

- **Which causes actually recur.** The ranked frequency, in their experience.
- **The threshold question.** What counts as a failure — a callback? a readmission? a
  phone call to the unit? Their answer defines what the instrument is diagnosing.
- **The neighbour-confusion question.** Which two of these do they see conflated, and how
  do they tell them apart by eye?
- **The contrarian question.** *What do people usually blame that isn't actually the
  cause?* This is the single most valuable answer for the locus rule, and it should be
  quoted verbatim in `identity.md`.
- **What's missing from this list entirely.** The cause that only shows up if you've done
  this a thousand times.
