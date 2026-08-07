import re
spec = open('specimens/specimen-06-va-bariatric-soft-diet.md').read()
def flat(s):
    s = s.replace('\u2019',"'").replace('\u2018',"'").replace('\u201c','"').replace('\u201d','"').replace('\u2013','-').replace('\u2014','-')
    return re.sub(r'\s+', ' ', s).strip().lower()
body = flat(spec)
anchors = [
  "Always stop eating when no longer hungry.",
  "Fullness will feel different now than before surgery.",
  "Stop eating when you are no longer hungry.",
  "It is important to work up slowly to these amounts.",
  "could cause impaction if too large a quantity is eaten",
  "Aim to consume 4-6 planned meals with each meal up to a volume of 4 oz. (1/2 c.)",
  "may lead to discomfort in your chest or abdomen or induce vomiting",
  "Refined carbohydrates like white breads, rice and pastas expand in your new structure which can cause discomfort",
  "This is the fourth diet stage after bariatric surgery",
  "at least 3 months after surgery",
  "follow your bariatric dietitian's recommendations",
  "Take vitamin/mineral supplements daily as prescribed by the bariatric team.",
  "Discuss healthy snack suggestions with a dietitian.",
  "Aim to consume at least 48-64 ounces (6-8 cups) of fluids each day.",
  "Take 20-30 minutes to finish a meal.",
  "Remember to separate meals from liquids by at least 30 minutes.",
  "Short pasta and noodles",
]
fails = 0
for a in anchors:
    ok = flat(a) in body
    if not ok: fails += 1
    print(("OK   " if ok else "FAIL "), a[:70])
print(f"\n{len(anchors)-fails}/{len(anchors)} verified, {fails} failed")