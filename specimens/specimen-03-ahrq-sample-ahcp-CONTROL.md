# Specimen 03 — AHRQ Sample After Hospital Care Plan (CONTROL)

**Role in this corpus:** control. This is the reference standard against which
Specimens 01 and 02 are read. It is included so that the instrument can be tested
on a document where the expected output is *no primary defect identified*. A
diagnostician that names a primary defect here has failed the test.

**Source:** Agency for Healthcare Research and Quality, Re-Engineered Discharge
(RED) Toolkit, Tool 3 — Example After Hospital Care Plan. Public domain, U.S.
government publication. Fictional patient ("Oscar Sanchez"); contains no PHI and
required no de-identification.
https://www.ahrq.gov/professionals/systems/hospital/red/toolkit/ahcp-sample.html

**Artifact class:** patient-facing after-hospital care plan, purpose-built to a
plain-language standard. Not auto-generated from an EHR.

---

## Known properties of this specimen, recorded before any diagnostic run

**1. Dated exemplar.** The document carries a 2012 discharge date and reflects the
plain-language standard of that period. It is a reference standard, not a claim
about what health systems produce today.

**2. A malformed dose unit is present and is known to the author.**
On the Noon medication table, LISINOPRIL is listed as `40 m` — the `g` in `mg`
is absent. This is a real transcription error in the published exemplar.

It is recorded here deliberately, before any run, so that it functions as a test
rather than as a surprise. Two outputs are acceptable when the instrument reads
this specimen:

- *No primary document defect identified* — on the reasoning that the drug name,
  quantity ("1 pill"), route, and indication are all intact, and a caregiver
  administering one pill by mouth is not misdirected by the missing unit; or
- *Malformed dose unit, explicitly ranked as non-primary* — named, but not
  advanced as a cause of caregiver failure at home.

An output that advances this typo as the primary defect is a **failure of the
instrument**, not a finding. It would indicate the diagnostician is defect-seeking
rather than defect-ranking, which is the specific failure mode this control exists
to detect.

**3. Visual structure is not preserved in this transcription.** The original uses
color-coded medication tables (yellow/pink/green/purple by time of day), sun,
clock, moon, and bed icons as time-of-day cues, and printed monthly calendars.
These are load-bearing features of the original document's usability and are lost
in markdown. Any assessment of this specimen's plain-language quality should be
made against the source PDF, not this file.

---

## Sample After Hospital Care Plan (AHCP)

**\*\*Bring This Plan to ALL Appointments\*\***

### After Hospital Care Plan for:

# Oscar Sanchez

**Discharge Date: August 1, 2012**

> TRY TO QUIT SMOKING: Call Jon Doe at (555) 555-3344 at ABC Medical Center.
>
> Question or Problem with this Packet? Call your Discharge Educator: (555) 555-2222
>
> Serious health problem? Call Dr. Mark Avery: (555) 555-5555

**EACH DAY follow this schedule:**

---

## MEDICINES

### Morning

| What time of day do I take this medicine? | Why am I taking this medicine? | Medicine name / Amount | How many (or how much) do I take? | How do I take this medicine? |
|---|---|---|---|---|
| Morning | Blood pressure | PROCARDIA XL<br>NIFEDIPINE<br>90 mg | 1 pill | By mouth |
| | Blood pressure | HYDROCHLOROTHIAZIDE<br>25 mg | 1 pill | By mouth |
| | Blood pressure | CLONIDINE HCl<br>0.1 mg | 3 pills | By mouth |
| | Cholesterol | LIPITOR<br>ATORVASTATIN CALCIUM<br>20 mg | 1 pill | By mouth |
| | Stomach | PROTONIX<br>PANTOPRAZOLE SODIUM<br>40 mg | 1 pill | By mouth |
| | Heart | ASPIRIN EC<br>325 mg | 1 pill | By mouth |
| | To stop smoking | NICOTINE<br>14 mg/24 hour | 1 patch | On skin |
| | Then, after 4 weeks use → | NICOTINE<br>7 mg/24 hour | 1 patch | On skin |
| | Blood pressure | COZAAR<br>LOSARTAN POTASSIUM<br>50 mg | 1 pill | By mouth |
| | Infection in eye | VIGAMOX<br>MOXIFLOXACIN HCl<br>0.5% solution | 1 drop | In your left eye |

### Noon

| What time of day do I take this medicine? | Why am I taking this medicine? | Medicine name / Amount | How many (or how much) do I take? | How do I take this medicine? |
|---|---|---|---|---|
| Noon | Blood pressure | ATENOLOL<br>75 mg | 1 pill | By mouth |
| | Blood pressure | LISINOPRIL<br>40 m | 1 pill | By mouth |
| | Infection in eye | VIGAMOX<br>MOXIFLOXACIN HCl<br>0.5% solution | 1 drop | In your left eye |

*(`40 m` is reproduced exactly as printed in the source. See header note 2.)*

### Evening

| What time of day do I take this medicine? | Why am I taking this medicine? | Medicine name / Amount | How many (or how much) do I take? | How do I take this medicine? |
|---|---|---|---|---|
| Evening | Infection in eye | VIGAMOX<br>MOXIFLOXACIN HCl<br>0.5 % solution | 1 drop | In your left eye |

### Bedtime

| What time of day do I take this medicine? | Why am I taking this medicine? | Medicine name / Amount | How many (or how much) do I take? | How do I take this medicine? |
|---|---|---|---|---|
| Bedtime | Blood pressure | CLONIDINE HCl<br>0.1 mg | 3 pills | By mouth |

### As needed

| What time of day do I take this medicine? | Why am I taking this medicine? | Medicine name / Amount | How many (or how much) do I take? | How do I take this medicine? |
|---|---|---|---|---|
| If you need it for headache | Headache | TRAMADOL HCl<br>50 mg | 1-2 pills<br>Every 6 hours<br>If you need it | By mouth |
| If you need it for chest pain | Chest pain | NITROGLYCERIN<br>0.4 mg | 1 pill every 5 minutes<br>(if need more than 3 pills, call 911) | Under your tongue |
| If you need it to stop smoking | To stop smoking | NICORELIEF<br>NICOTINE POLACRILEX<br>4 mg gum | Gum | Chew |

---

**\*\* Bring this Plan to ALL Appointments \*\***

**Oscar Sanchez**

## What is my main medical problem?

Chest Pain

## When are my appointments?

| | | |
|---|---|---|
| **Wednesday, August 8 at 11:30 a.m.** | **Thursday, August 16 at 3:20 p.m.** | **Wednesday, September 12 at 9:00 a.m.** |
| Dr. Mark Avery<br>Primary Care Provider (Doctor) | Dr. Anita Jones<br>Rheumatologist | Dr. Lin Wu<br>Cardiologist |
| 100 Main St, 2nd Floor<br>Anytown, ST | 100 Pleasant Rd, Suite 105<br>Anytown, ST | 100 Park Rd, Suite 504<br>Anytown, ST |
| For a Followup appointment | For your arthritis | To check your heart |
| Office Phone #: (555) 555-5555 | Office Phone #: (555) 555-6666 | Office Phone #: (555) 555-4444 |

## What exercises are good for me?

Walk for at least 20 minutes each day.

## What should I eat?

Eating food that is low in fat and low in cholesterol will help you stay healthy.

## What are my medicine allergies?

REMEMBER you are ALLERGIC to MOTRIN.

## Where is my pharmacy?

Joe's Pharmacy
1234 Summertime Ave.
Anytown, ST 55555
(555) 555-7777

---

## Questions for Dr. Avery

**For my appointment on Wednesday, August 8th, at 11:30 am**

**Check the box and write notes to remember what to talk about with Dr. Avery.**

I have questions about:

- ☐ My medicines \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- ☐ My pain \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- ☐ Feeling stressed \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

What other questions do you have? \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Dr. Avery: When I left the hospital, results from some tests were not available. Please check for results of these tests.

- ☐ I am having trouble with the stairs in my house.
- ☐ Someone I live with smokes.
- ☐ I feel stressed or overwhelmed.
- ☐ I am having trouble getting food.
- ☐ There are other things going on in my life that are affecting my health.

---

## August 2012

| Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|---|---|---|---|---|---|---|
| | | | **1**<br>Delivery of Bed by Martin, Inc. 555-555-6767 | **2**<br>N.E. VNA to visit 555-555-8888 | **3**<br>Pharmacist will call | **4** |
| **5** | **6** | **7** | **8**<br>Dr. Avery at 11:30am<br>100 Main St, 2nd Floor, Anytown, ST | **9** | **10** | **11** |
| **12** | **13** | **14** | **15** | **16**<br>Dr. Jones at 3:20 pm, 100 Pleasant Rd, Suite 105, Anytown, ST | **17** | **18** |
| **19** | **20** | **21** | **22** | **23** | **24** | **25** |
| **26** | **27** | **28** | **29** | **30** | **31** | |

## September 2012

| Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |
|---|---|---|---|---|---|---|
| | | | | | | **1** |
| **2** | **3** Labor Day | **4** | **5** | **6** | **7** | **8** |
| **9** | **10** | **11** | **12**<br>Dr. Wu at 9:00 am at 100 Park Rd, Suite 504, Anytown, ST | **13** | **14** | **15** |
| **16** | **17** | **18** | **19** | **20** | **21** | **22** |
| **23** | **24** | **25** | **26** | **27** | **28** | **29** |
| **30** | | | | | | |

---

## My Medical Problem: Noncardiac Chest Pain

Noncardiac chest pain is pain that is <u>not</u> caused by a heart problem.

- If your chest pain gets different or worse, call your doctor.
- Take your medicines as prescribed.
- See your doctor and ask questions.

## My Medical Problem: High Blood Pressure

High blood pressure is also called hypertension.

- Avoid salty foods.
- Take your medicines as prescribed.
- See your doctor and ask questions.

*Source: National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK).*
