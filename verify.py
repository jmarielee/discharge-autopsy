#!/usr/bin/env python3
"""
verify.py — the deterministic layer of Discharge Autopsy.

The model labels. This decides.

The model's job is to produce candidate defects, each with a taxonomy class, a locus,
and one or more verbatim anchors. It does not choose the primary defect, does not
assign a tier, and does not decide whether to refuse. This script does all three,
from the ranking in reference/taxonomy.md, and then runs eleven gates against the result.

Python standard library only. No network, no key, no model call.

    python3 verify.py runs/specimens-01-02.json
    python3 verify.py --test
"""

import argparse
import html
import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# The closed taxonomy. Order is the ranking. reference/taxonomy.md is the prose
# version of this table; if the two disagree, that is a bug in one of them.
# ---------------------------------------------------------------------------

TAXONOMY = {
    "ACTION_DIVERGENCE":                   ("P1", "internal_consistency"),
    "THRESHOLD_ABSENCE":                   ("P2", "observability"),
    "STATE_MISMATCH":                      ("P3", "completeness"),
    "STRUCTURED_NARRATIVE_CONTRADICTION":  ("P4", "internal_consistency"),
    "CONTACT_ABSENCE":                     ("P5", "completeness"),
    "FIELD_INCOMPLETENESS":                ("P6", "completeness"),
}

TIER_ORDER = ["P1", "P2", "P3", "P4", "P5", "P6"]

# The locus schema. A LOCUS outside this set fails G2. Execution-side facts —
# what a person did, when, how much — are admissible as evidence and can never
# be a locus.
DOCUMENT_PROPERTIES = {
    "readability",
    "arithmetic_demand",
    "schedule_feasibility",
    "internal_consistency",
    "prerequisite_gap",
    "observability",
    "navigability",
    "completeness",
}

RESOLUTION_PATH = "Bring this document to the discharging clinician or a pharmacist."

REFUSAL = "REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE"
TIE = "TIE_UNRESOLVED"

# Refusal threshold. Both conditions must hold to return a verdict.
MIN_ANCHORED_DEFECTS = 2
MIN_TIER_FOR_VERDICT = "P3"

# G5 — prescriptive language. A diagnostician that proposes wording is an editor.
PRESCRIPTIVE = [
    r"\bshould (?:say|read|include|state|be)\b",
    r"\bshould have (?:said|read|included|stated)\b",
    r"\brecommend(?:s|ed|ation)?\b",
    r"\bsuggest(?:s|ed|ion)?\b",
    r"\brewrite\b", r"\brewritten\b",
    r"\brevise\b", r"\brevised\b",
    r"\bthe fix is\b", r"\bto fix (?:this|it)\b",
    r"\badd(?:ing)? a (?:line|sentence|section|field)\b",
    r"\bcould be improved\b",
    r"\binstead,? (?:say|write|use)\b",
    r"\bnext steps?\b",
    r"\btry\b.{0,20}\binstead\b",
]

# G9 — clinical-correctness assertions. Out of scope by identity.
CLINICAL = [
    r"\bmedically (?:in)?correct\b",
    r"\b(?:the |this )?dose is (?:too |in)?(?:high|low|correct|wrong|incorrect)\b",
    r"\bwrong (?:dose|drug|medication)\b",
    r"\bcontraindicat",
    r"\bshould (?:not )?(?:take|be prescribed|be given)\b",
    r"\bthe correct dose\b",
    r"\bclinically (?:in)?appropriate\b",
]

# G11 — person-blame in prose. The locus rule, enforced where a reader reads.
# G2 checks the LOCUS field and G4 checks the class name. Neither reads the free
# text. Until 2026-08-07 a report could name a person in CHAIN and pass all ten
# gates; see OPEN-DEFECTS.md, OD-9.
PERSON_BLAME = [
    r"\bnon-?compliant\b", r"\bnon-?adheren", r"\bnoncompliance\b",
    r"\b(?:patient|caregiver|family|reader|user|carer)\s+(?:error|fault|failure|mistake)\b",
    r"\b(?:failed|neglected|forgot)\s+to\s+(?:read|follow|comply|call|administer|attend|give|take)\b",
    r"\b(?:patient|caregiver|family|reader|user|carer)\b[^.]{0,40}\b(?:did not|didn't|failed to|neglected to|forgot to|ignored|disregarded|misread|overlooked|never read)\b",
    r"\bagainst (?:instruction|instructions|advice|orders|guidance)\b",
    r"\bshould have (?:read|followed|called|known|noticed|asked|checked)\b",
    r"\b(?:careless|negligent|negligence)\b",
    r"\b(?:patient|caregiver|family|reader|user|carer)\s+(?:administered|gave|applied|took|used|continued|stopped|skipped)\b",
]

# The full gate list, in one place. Previously hardcoded as range(1, 11) in
# three separate loops.
GATES = [f"G{i}" for i in range(1, 12)]


# ---------------------------------------------------------------------------
# Anchor matching (G1)
# ---------------------------------------------------------------------------

def flatten(text):
    """Reduce a document or an anchor to a comparable form.

    Formatting is flattened; wording is not. HTML tags, markdown blockquote and
    list markers, and runs of whitespace are removed because they are artifacts
    of how a document was stored rather than of what it says. Case is folded.
    Nothing else is touched: a paraphrase will not match.
    """
    text = html.unescape(text)
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"<script.*?</script>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)          # html tags
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)   # blockquote markers
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.M)  # list bullets
    text = re.sub(r"[`*_#|]", " ", text)          # markdown punctuation
    text = re.sub(r"[\u2018\u2019]", "'", text)
    text = re.sub(r"[\u201c\u201d]", '"', text)
    text = re.sub(r"[\u2013\u2014]", "-", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().casefold()


def load_specimens(paths):
    corpus = {}
    for p in paths:
        f = (REPO / p) if not Path(p).is_absolute() else Path(p)
        if not f.exists():
            raise FileNotFoundError(f"specimen not found: {p}")
        corpus[p] = flatten(f.read_text(encoding="utf-8", errors="replace"))
    return corpus


def anchor_holds(anchor, corpus):
    """True if the anchor text appears verbatim in the specimen it cites."""
    src = corpus.get(anchor.get("file"))
    if src is None:
        return False
    needle = flatten(anchor.get("text", ""))
    return bool(needle) and needle in src


# ---------------------------------------------------------------------------
# The ranking. This is the part the model does not do.
# ---------------------------------------------------------------------------

def rank(candidates, corpus):
    """Return (result, primary, anchored, dropped).

    A candidate whose anchors do not all hold is dropped from the ranking
    entirely — not demoted. A fluent claim about a line that does not say that
    is not a weak finding; it is not a finding.
    """
    anchored, dropped = [], []
    for c in candidates:
        anchors = c.get("anchors", [])
        bad = [a for a in anchors if not anchor_holds(a, corpus)]
        if not anchors or bad:
            dropped.append((c, bad))
            continue
        cls = c.get("class")
        if cls not in TAXONOMY:
            dropped.append((c, []))
            continue
        c = dict(c)
        c["tier"] = TAXONOMY[cls][0]
        anchored.append(c)

    if not anchored:
        return REFUSAL, None, anchored, dropped

    best = min(TIER_ORDER.index(c["tier"]) for c in anchored)
    top = [c for c in anchored if TIER_ORDER.index(c["tier"]) == best]

    # Refusal threshold: both conditions must hold.
    enough = len(anchored) >= MIN_ANCHORED_DEFECTS
    severe = best <= TIER_ORDER.index(MIN_TIER_FOR_VERDICT)
    if not (enough and severe):
        return REFUSAL, None, anchored, dropped

    if len(top) == 1:
        return "VERDICT", top[0], anchored, dropped

    # Tie-break a: most distinct anchored instances.
    top = _keep_max(top, lambda c: len(c.get("anchors", [])))
    if len(top) == 1:
        return "VERDICT", top[0], anchored, dropped

    # Tie-break b: within or adjacent to a stated emergency instruction.
    top = _keep_max(top, lambda c: int(bool(c.get("emergency_adjacent"))))
    if len(top) == 1:
        return "VERDICT", top[0], anchored, dropped

    # Tie-break c: earlier document position.
    positioned = [c for c in top if c.get("position") is not None]
    if positioned:
        top = _keep_max(positioned, lambda c: -c["position"])
        if len(top) == 1:
            return "VERDICT", top[0], anchored, dropped

    # A coin flip dressed as a diagnosis is a worse failure than a refusal.
    return TIE, None, anchored, dropped


def _keep_max(items, key):
    best = max(key(i) for i in items)
    return [i for i in items if key(i) == best]


# ---------------------------------------------------------------------------
# The eleven gates
# ---------------------------------------------------------------------------

def all_prose(report, primary):
    parts = []
    for k in ("chain", "would_flip_this", "resolution_path", "why", "why_refused"):
        v = report.get(k)
        if isinstance(v, str):
            parts.append(v)
    for c in report.get("candidates", []):
        for k in ("chain", "note"):
            if isinstance(c.get(k), str):
                parts.append(c[k])
    for r in report.get("ruled_out", []):
        if isinstance(r.get("why"), str):
            parts.append(r["why"])
    for s in report.get("filed_as_symptom", []):
        if isinstance(s, dict) and isinstance(s.get("reason"), str):
            parts.append(s["reason"])
    return "\n".join(parts)


def run_gates(report, result, primary, anchored, dropped, corpus):
    g = {}

    # G1 — every anchor verbatim in the specimen it cites.
    bad = []
    for c in report.get("candidates", []):
        for a in c.get("anchors", []):
            if not anchor_holds(a, corpus):
                bad.append(a.get("text", "")[:60])
    g["G1"] = (not bad, f"{len(bad)} anchor(s) not found verbatim" if bad
               else "all anchors verbatim")

    # G2 — locus is a document property.
    off = [c.get("locus") for c in report.get("candidates", [])
           if c.get("locus") not in DOCUMENT_PROPERTIES]
    g["G2"] = (not off, f"locus outside schema: {off}" if off else "locus in schema")

    # G3 — exactly one primary, and the report does not name it itself.
    # The ranking selects the primary. A report that asserts one is a model
    # doing the deciding, which is the thing this layer exists to prevent.
    claimed = report.get("claimed_primary")
    if claimed is not None:
        if isinstance(claimed, list) and len(claimed) != 1:
            g["G3"] = (False, f"report named {len(claimed)} primary defects")
        else:
            name = claimed[0] if isinstance(claimed, list) else claimed
            computed = primary["class"] if primary else result
            ok = name == computed
            g["G3"] = (ok, "claimed primary matches computed" if ok
                       else f"report claimed {name}, ranking computed {computed}")
    elif result == "VERDICT":
        ok = primary is not None
        g["G3"] = (ok, "one primary defect, computed" if ok else "no primary resolved")
    else:
        g["G3"] = (True, f"no primary claimed ({result})")

    # G4 — every class named is in the closed taxonomy; result is a verdict on
    # a taxonomy class or a named refusal. An invented class is not a finding.
    invented = [c.get("class") for c in report.get("candidates", [])
                if c.get("class") not in TAXONOMY]
    if invented:
        g["G4"] = (False, f"class(es) outside taxonomy: {invented}")
    elif result == "VERDICT":
        g["G4"] = (True, f"class {primary['class']} in taxonomy")
    else:
        g["G4"] = (result in (REFUSAL, TIE), f"named result {result}")

    # G5 — no prescriptive verb anywhere in the prose.
    prose = all_prose(report, primary)
    hits = [p for p in PRESCRIPTIVE if re.search(p, prose, re.I)]
    g["G5"] = (not hits, f"prescriptive language: {hits}" if hits else "no fix proposed")

    # G6 — resolution path is the fixed string, exactly.
    rp = report.get("resolution_path", "")
    g["G6"] = (rp == RESOLUTION_PATH,
               "resolution path exact" if rp == RESOLUTION_PATH
               else "resolution path altered or missing")

    # G7 — at least two ruled-out alternatives, each citing evidence.
    if result == "VERDICT":
        ro = report.get("ruled_out", [])
        ok = len(ro) >= 2 and all(r.get("why", "").strip() for r in ro)
        g["G7"] = (ok, f"{len(ro)} alternative(s) ruled out with reasons")
    else:
        g["G7"] = (True, "not applicable to a non-verdict result")

    # G8 — tier matches the deterministic ranking, not a model choice.
    if result == "VERDICT":
        claimed = report.get("claimed_tier")
        computed = primary["tier"]
        ok = claimed is None or claimed == computed
        g["G8"] = (ok, f"tier {computed} computed"
                   + ("" if ok else f"; report claimed {claimed}"))
    else:
        g["G8"] = (True, "no tier claimed")

    # G9 — no clinical-correctness assertion.
    hits = [p for p in CLINICAL if re.search(p, prose, re.I)]
    g["G9"] = (not hits, f"clinical assertion: {hits}" if hits
               else "no clinical judgment asserted")

    # G10 — falsifiability.
    wf = report.get("would_flip_this", "").strip()
    ok = len(wf.split()) >= 8
    g["G10"] = (ok, "falsifier stated" if ok else "falsifier missing or too vague")


    # G11 — no person named as the cause, anywhere in the prose.
    hits = [p for p in PERSON_BLAME if re.search(p, prose, re.I)]
    g["G11"] = (not hits, f"person-blame: {hits}" if hits else "locus holds in prose")

    return g


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def emit(report, result, primary, anchored, dropped, gates):
    out = []
    out.append("=" * 70)
    out.append(f"DISCHARGE AUTOPSY — deterministic layer")
    out.append(f"specimen set: {', '.join(report.get('specimen_set', []))}")
    out.append("=" * 70)
    out.append("")

    rejected = any(not ok for ok, _ in gates.values())

    if result == "VERDICT" and rejected:
        out.append("PRIMARY DEFECT     WITHHELD — a gate failed; see GATES below.")
    elif result == "VERDICT":
        out.append(f"PRIMARY DEFECT     {primary['class']}")
        out.append(f"TIER               {primary['tier']}  (computed, not claimed)")
        out.append(f"LOCUS              {primary['locus']}")
    elif result == REFUSAL:
        out.append(f"RESULT             {REFUSAL}")
        enough = len(anchored) >= MIN_ANCHORED_DEFECTS
        severe = anchored and min(TIER_ORDER.index(c['tier'])
                                  for c in anchored) <= TIER_ORDER.index(MIN_TIER_FOR_VERDICT)
        out.append(f"WHY REFUSED        anchored defects: {len(anchored)} "
                   f"(need >= {MIN_ANCHORED_DEFECTS}) — {'pass' if enough else 'FAIL'}")
        out.append(f"                   tier {MIN_TIER_FOR_VERDICT} or higher present — "
                   f"{'pass' if severe else 'FAIL'}")
    else:
        out.append(f"RESULT             {TIE}")

    out.append("")
    out.append(f"ANCHORED           {len(anchored)}")
    for c in anchored:
        mark = " <-- primary" if primary is not None and c is primary else ""
        out.append(f"  {c['tier']}  {c['class']}{mark}")
    if dropped:
        out.append("")
        out.append(f"DROPPED            {len(dropped)}  (failed anchor, or class "
                   f"outside taxonomy)")
        for c, bad in dropped:
            why = "anchor not verbatim" if bad else "class outside taxonomy"
            out.append(f"  --  {c.get('class', '?')}  [{why}]")

    out.append("")
    out.append("GATES")
    for name in GATES:
        ok, msg = gates[name]
        out.append(f"  {name}  {'PASS' if ok else 'FAIL'}  {msg}")

    failed = [n for n, (ok, _) in gates.items() if not ok]
    out.append("")
    out.append(f"RESOLUTION PATH    {RESOLUTION_PATH}")
    out.append("")
    out.append("-" * 70)
    out.append("VERIFIED" if not failed else f"REJECTED — failed {', '.join(sorted(failed))}")
    return "\n".join(out), not failed


def verify_file(path, quiet=False):
    report = json.loads(Path(path).read_text())
    corpus = load_specimens(report.get("specimen_set", []))
    result, primary, anchored, dropped = rank(report.get("candidates", []), corpus)
    gates = run_gates(report, result, primary, anchored, dropped, corpus)
    text, ok = emit(report, result, primary, anchored, dropped, gates)
    if not quiet:
        print(text)
    return ok, result, primary, gates


# ---------------------------------------------------------------------------
# Self-test: every gate must have at least one negative fixture that it blocks.
# ---------------------------------------------------------------------------

def self_test():
    fixtures = sorted((REPO / "tests" / "fixtures").glob("*.json"))
    if not fixtures:
        print("no fixtures found in tests/fixtures/")
        return False

    covered, failures = set(), []
    print("FIXTURES")
    for f in fixtures:
        meta = json.loads(f.read_text())
        expect = meta.get("_expect", {})
        ok, result, primary, gates = verify_file(f, quiet=True)

        want_gate = expect.get("blocked_by")
        want_result = expect.get("result")
        problems = []

        if want_gate:
            if gates[want_gate][0]:
                problems.append(f"{want_gate} did not fire")
            else:
                covered.add(want_gate)
            # A negative fixture must fail its own gate and no unrelated ones.
            others = [n for n, (g_ok, _) in gates.items() if not g_ok and n != want_gate]
            if others and not expect.get("allow_collateral"):
                problems.append(f"also failed {others}")
        else:
            if not ok:
                bad = [n for n, (g_ok, _) in gates.items() if not g_ok]
                problems.append(f"expected clean, failed {bad}")

        if want_result and result != want_result:
            problems.append(f"result {result}, expected {want_result}")

        status = "ok" if not problems else "FAIL"
        if want_gate:
            outcome = f"blocked by {want_gate}" if not problems else f"NOT blocked ({result})"
        else:
            outcome = f"clean -> {result}"
        print(f"  {status:4}  {f.name}  ->  {outcome}"
              + (f"  [{'; '.join(problems)}]" if problems else ""))
        if problems:
            failures.append(f.name)

    print()
    print("COVERAGE ASSERTION")
    missing = [n for n in GATES if n not in covered]
    for n in GATES:
        print(f"  {n}  {'covered' if n in covered else 'NO NEGATIVE FIXTURE'}")

    print()
    if failures or missing:
        if failures:
            print(f"FAILED: {', '.join(failures)}")
        if missing:
            print(f"UNVERIFIED GATES: {', '.join(missing)}")
        return False
    print("All fixtures behaved as declared. Every gate has a negative fixture.")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", nargs="?", help="path to a diagnosis JSON")
    ap.add_argument("--test", action="store_true",
                    help="run every fixture and assert gate coverage")
    args = ap.parse_args()

    if args.test:
        sys.exit(0 if self_test() else 1)
    if not args.report:
        ap.print_help()
        sys.exit(2)
    ok, *_ = verify_file(args.report)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
