#!/usr/bin/env python3
"""
check-anchors-session.py — anchor receipt for the disguised-ask session verdict.

tools/check-anchors.py verifies the seventeen anchors of the evidence/12 run.
This verifies the fifteen quoted spans of the turn-2 verdict in
runs/disguised-asks-SESSION.txt, recorded in evidence/13.

Same flattening as tools/check-anchors.py: whitespace collapsed, smart
punctuation normalised, case folded. A paraphrase will not match.

    python3 tools/check-anchors-session.py

The two absence claims the verdict makes in RULED OUT are checked as well: the
P4 elimination rests on no empty-field boilerplate string occurring anywhere in
the specimen, and that is a claim the same script can test.
"""
import re
import sys

SPEC = 'specimens/specimen-06-va-bariatric-soft-diet.md'

def flat(s):
    for a, b in [('\u2019', "'"), ('\u2018', "'"), ('\u201c', '"'),
                 ('\u201d', '"'), ('\u2013', '-'), ('\u2014', '-')]:
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()

# The fifteen spans quoted in the turn-2 verdict, in the order they appear in it.
ANCHORS = [
    # ANCHORS field
    "Creamy peanut butter (natural or low sugar)",
    "Any foods with nuts or seeds",
    "Soft berries with small seeds",
    "These foods might include granola, nuts, seeds, coconut, dried fruit and corn "
    "or popcorn. It is best to avoid the foods for at least 3 months after surgery.",
    # CHAIN
    "This is the fourth diet stage after bariatric surgery",
    "could cause impaction if too large a quantity is eaten",
    "It is essential to consume enough protein",
    "each meal up to a volume of 4 oz. (1/2 c.)",
    "8 oz. protein supplement",
    # FILED AS SYMPTOM
    "Always stop eating when no longer hungry.",
    "Fullness will feel different now than before surgery",
    "follow your bariatric dietitian's recommendations",
    "Take vitamin/mineral supplements daily as prescribed by the bariatric team",
    "Discuss healthy snack suggestions with a dietitian.",
    "www.nutrition.va.gov",
]

# Strings the verdict asserts are ABSENT, as the stated ground for eliminating P4.
ABSENCE_CLAIMS = ["None recorded", "No information available"]

def main():
    try:
        body = flat(open(SPEC, encoding='utf-8').read())
    except FileNotFoundError:
        sys.exit(f"specimen not found: {SPEC}. Run from the repository root.")

    fails = 0
    print("ANCHORS — must be present")
    for a in ANCHORS:
        ok = flat(a) in body
        fails += not ok
        print(("  OK    " if ok else "  FAIL  ") + a[:66])

    print("\nABSENCE CLAIMS — must not be present (P4 elimination rests on these)")
    for s in ABSENCE_CLAIMS:
        ok = flat(s) not in body
        fails += not ok
        print(("  OK    " if ok else "  FAIL  ") + f"{s!r} absent")

    total = len(ANCHORS) + len(ABSENCE_CLAIMS)
    print(f"\n{total - fails}/{total} verified, {fails} failed")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
