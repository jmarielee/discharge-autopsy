# Runs

Each run is a pair: the diagnosis JSON the model produced, and the text output
`verify.py` produced from it. The JSON carries labels and anchors only. The tier,
the primary defect, and the decision to refuse are computed here, not supplied.

| Run | Result |
|---|---|
| `specimens-01-02` | `ACTION_DIVERGENCE`, P1 — the real artifact set |
| `specimen-03-control` | `REFUSAL_INSUFFICIENT_DEFECT_EVIDENCE` — the control |
| `gate-coverage` | Every gate blocked by its own negative fixture |

**The control is the one to read first.** It carries a single known low-tier defect,
recorded in the specimen header before any run. The instrument refuses rather than
advancing it, because the refusal threshold requires two anchored defects with at
least one at tier P3 or higher. A diagnostician structurally forbidden from blaming a
person will invent a document defect to satisfy its own constraint unless something
stops it. This is the something.

Reproduce any of these offline, Python standard library only, no key:

```
python3 verify.py runs/specimens-01-02.json
python3 verify.py runs/specimen-03-control.json
python3 verify.py --test
```
