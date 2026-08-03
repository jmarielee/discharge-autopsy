# Build blueprint — folder shape, word budgets, seven-day plan

---

## The folder

The brief asks for five things. Ship exactly five at the top level and put everything else
one directory down. A stranger should meet the diagnostician before they meet anything
else.

```
/
├── README.md                 ≤ 900w   quickstart · 90-second verify · limits · judge protocol
├── identity.md               ≤ 500w   who it is, what it diagnoses, what it refuses
├── rules.md                  ≤ 900w   operating law only. Numbered IDs. No format, no math spec.
├── examples.md               ≤ 1,500w EXACTLY THREE. One clean, one abstention, one decline.
├── reference/
│   ├── failure-taxonomy.md            the named causes + discriminating evidence each
│   ├── output-contract.md             the verdict schema (moved OUT of rules.md)
│   └── readability-benchmarks.md      the thresholds the arithmetic turns on, with sources
├── diagnose.py                        deterministic layer + --selftest
├── verify.py                          gates every shipped diagnosis + --selftest
├── tests/
│   ├── fixtures/                      one negative fixture per gate + coverage assertion
│   └── seeded/                        seeded specimen + answer key
├── specimens/                         source documents, by rung, with retrieval metadata
├── runs/                              dated verbatim transcripts
├── receipts/                          full diagnosis reports (NOT in examples.md)
├── PROTOCOL.md                        pre-registered, dated, unedited
├── OPEN-DEFECTS.md                    including the one the gate cannot see
├── LIMITATIONS.md                     where the checks reach their limit
└── CREDITS.md                         where each borrowed idea came from
```

## Hard limits

These are not guidelines. Proportion is the deduction that cost a tier last time.

- **`examples.md` ≤ 1,500 words. Three examples. Non-negotiable.** Every full diagnosis
  report goes to `receipts/`. When a beautiful specimen appears, it goes in `receipts/`.
- **`README.md` shorter than `rules.md` + `examples.md` combined.**
- **Nothing appears in two files.** One canonical source; others cite it. (A drifted
  duplicate cost `job-fit` real quality and cost another entrant ~10 places.)
- **≤ 12 files at repo root.** The Taper Editor had 40. That is what buried its best
  artifact.
- **No `build/` folder, no pipeline folder, no process record in the shipped repo.**
- **`LIMITATIONS.md` must be linked from the README's first screen.** Last time this file
  was one of the best artifacts in the field and went unmentioned in the feedback because
  nobody could find it.

## What goes where

| File | Holds | Does NOT hold |
|---|---|---|
| `identity.md` | who, what domain, what's out of scope and why, the safety boundary | rules, format, examples |
| `rules.md` | numbered operating law, thresholds by reference | output format, the math spec, worked examples |
| `examples.md` | three worked diagnoses demonstrating contract, abstention, decline | full reports, philosophy, calibration notes |
| `reference/` | domain knowledge, taxonomy, format contracts, benchmarks | operating law |
| `receipts/` | every full diagnosis with its run transcript | anything the folder needs to operate |

---

## Seven-day plan

**Saturday 2 Aug (tonight)**
- Create the repo. Fill the procedure class into `PROTOCOL.md`. **Commit it dated.**
- Download 8 public specimens. Record source URL + retrieval date for each. Do not read
  them closely yet.
- Draft the practitioner ask and queue it to send Sunday morning.

**Sunday 3 Aug**
- Send the practitioner ask. This is the highest-leverage 10 minutes of the week.
- Build the **seeded specimen and its answer key** — before reading any real document
  closely. This is what stops you fitting discriminators to the first real sheet you see.
- `reference/failure-taxonomy.md` first pass.

**Monday 4 Aug**
- `diagnose.py`: readability computation, dose-arithmetic detection, schedule feasibility,
  contradiction detection, evidence mass per cause, separation threshold, abstention.
- `--selftest`. One negative fixture per gate. The coverage assertion.

**Tuesday 5 Aug**
- `identity.md`, `rules.md`, `reference/output-contract.md`.
- Rules file is operating law with citable IDs only. Format contracts live in reference.
- If the practitioner has replied, schedule the call for Wednesday.

**Wednesday 6 Aug**
- Run all specimens against the **frozen commit**. Record the hash in each transcript.
- Paste transcripts verbatim into `runs/`. Fix nothing mid-run; log everything.
- Practitioner call if it happens. Transcribe into `reference/`.

**Thursday 7 Aug**
- `verify.py`: Rule 0 quote grounding, locus-field validation, no-prescription scan,
  one-primary-cause assertion, terminal-routing assertion.
- Run the seeded specimen cold against the key.
- `LIMITATIONS.md` and `OPEN-DEFECTS.md`, including the defect the gate cannot see.

**Friday 8 Aug**
- `examples.md` (three, hard cap), `README.md`, `CREDITS.md`.
- Ask two strangers to break it. Ship what they find in `OPEN-DEFECTS.md`.
- Re-read for anything appearing in two files.
- **Submit before the buzzer.** Six entrants last round were pinned to pre-deadline
  commits and lost work that landed after.

---

## The 90-second judge protocol

Put this near the top of the README. Three commands, no API key, no browser.

```
python3 diagnose.py tests/seeded/specimen.txt   → matches tests/seeded/answer-key.md
python3 verify.py --selftest                    → N/N gates blocked on their named check
python3 verify.py                               → every shipped receipt passes, 0 violations
```

Then a list of four specific things the diagnostician **cannot** do, and one worked input
with its expected output shape inline.
