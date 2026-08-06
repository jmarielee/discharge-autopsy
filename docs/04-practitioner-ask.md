# The practitioner ask

**This is the single highest-leverage ten minutes of the week.** It is what converts the
evidence ladder from PUBLIC to something with an observed failure behind it — the exact
dimension that separated the top three from everyone else in Comp #9.

Gabriel Azoulay built the second-strongest folder in that field, had nine strangers attack
it, and was still told: *"A real practitioner run. One regulatory reviewer putting live
copy through this, with the transcript kept, would have taken it."*

**Send it Sunday morning. The pool is thousands of people, not one.**

---

## Who to ask

In rough order of yield:

1. **Nurses** — they hand these out daily, they have strong opinions about which ones are
   badly written, and they've watched people fail to follow them in real time.
2. **Physical therapists** — especially in post-operative orthopedic settings, they see the
   downstream consequence of a bad sheet a week later.
3. **Discharge planners and case managers** — closest to the document as an artifact.
4. **Pharmacists** — the terminal routing target, and the people who field the calls a
   defective sheet generates.
5. **Anyone who has recently cared for someone post-surgery** — for specimens, not for the
   interview.

Personal network first. Pickleball, the gym, the running group, Pam, Sue, Lucie's
contacts, neighbours. One warm introduction beats twenty cold messages.

---

## The message

Short, discloses nothing, asks for one specific thing.

> Hi [name] — I'm building a small tool that reads discharge instruction sheets and finds
> where the *document* fails the person taking it home. It never looks at a patient and
> it doesn't give medical advice — it reads the paperwork and names one design defect.
>
> Two things I'd love, either or both:
>
> 1. Twenty minutes on the phone about which discharge sheets you see people struggle
>    with and why. I'd record and transcribe it if that's OK.
> 2. If you can think of a specific time a sheet went home and someone couldn't follow
>    it — what happened, and roughly what the sheet said.
>
> No patient information needed, nothing identifiable. Happy to show you what it finds.

**If asking for a specimen:**

> If you have a blank or sample discharge sheet — the template, not a filled-in one —
> I'd love a photo or PDF. Blank templates are ideal because there's nothing to redact.

*Blank templates are the ask to lead with. They carry every document-level defect, and
they eliminate the consent problem entirely.*

---

## Interview guide — 20 to 30 minutes

Record. Transcribe. The transcript becomes `reference/`, and quoting a practitioner
verbatim in `identity.md` is worth more than any amount of reasoning.

### Part A — the failure (5 min)

1. When a discharge sheet doesn't work, how do you find out? What's the signal — a
   callback, a readmission, a question at the next appointment?
2. Tell me about a specific time. What did the sheet say, and what did the person do?
3. Roughly how often does this happen?

*A2 is the observed-failure account. It's the whole reason for the call.*

### Part B — the causes (8 min)

4. What are the top five things that go wrong with these documents, in order of how often
   you see them?
5. Which two of those get confused with each other? How do you tell them apart?
6. **What do people usually blame that isn't actually the cause?**

*Q6 is the most valuable question in the guide. It is the locus rule in the
practitioner's own words, and the answer should be quoted verbatim in `identity.md`.*

### Part C — the thresholds (5 min)

7. Is there a reading level or plain-language standard your institution works to?
8. What does the sheet assume about the home that often isn't true?
9. What does it assume about who's there to help?

*Q8 and Q9 feed D4, the highest-yield cause in this taxonomy.*

### Part D — the artifact (5 min)

10. Who actually writes these? Is it a template, generated, or written per patient?
11. What can't be changed about them — what's mandated or locked?
12. Would a blank template be shareable?

*Q11 matters: a defect in a locked template is a different finding from one in
discretionary text, and knowing which is which keeps the instrument honest.*

### Part E — if there's time

13. What would you want to know about a sheet before it goes home?
14. Who would you want to see this? Whose problem is it?

---

## After the call

- Transcribe verbatim. Do not clean it up.
- Extract the ranked failure list into `reference/failure-taxonomy.md`, attributed.
- Extract the Q6 answer into `identity.md` as a quoted line.
- Record consent for quoting, and whether they want to be named or described by role.
- If they described an observed failure of a specific sheet, that is the **PRACTITIONER**
  rung. Ship the account and the document together.

## If nobody replies by Wednesday

Do not chase it into the deadline. Ship the ladder at SEEDED / PUBLIC / AUTHOR, leave the
PRACTITIONER rung visible and explicitly empty, and say in `OPEN-DEFECTS.md` that no
practitioner has run this and that it is the next step.

Alex Brown did exactly that. The judges said the discipline was right even though it cost
him the top spot. A named empty rung is worth more than a stretched full one.
