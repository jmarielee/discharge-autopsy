# Fixtures

Ten negative fixtures, one per gate. Each is the passing diagnosis with exactly one
thing changed, and each declares in `_expect.blocked_by` which gate should stop it.
`python3 verify.py --test` runs all of them and then asserts that **every gate has at
least one negative fixture**, so no gate ships unverified.

| Fixture | The failure it stages |
|---|---|
| `negative-G1-fabricated-quote` | A plausible sentence that appears nowhere in the specimen |
| `negative-G2-execution-side-locus` | Person-blame smuggled into the LOCUS field |
| `negative-G3-model-named-primary` | The model deciding instead of labelling |
| `negative-G4-invented-class` | A class outside the taxonomy — here, the one the locus rule forbids |
| `negative-G5-smuggled-fix` | A rewrite wearing a declarative, no imperative verb |
| `negative-G6-generated-routing` | Resolution path generated rather than fixed |
| `negative-G7-unruled-out` | A verdict that never eliminated its runner-up |
| `negative-G8-model-chosen-tier` | A tier asserted rather than computed |
| `negative-G9-clinical-judgment` | A dose judgment — out of scope by identity |
| `negative-G10-unfalsifiable` | A falsifier too vague to satisfy |

Two fixtures declare `allow_collateral`: they trip a second gate as well, because the
failure they stage genuinely carries two problems. That is recorded rather than
engineered away.

**The diagnostician never reads this folder.** Test material is evidence *about* the
product and is not part of the product.
