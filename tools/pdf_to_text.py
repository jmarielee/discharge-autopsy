#!/usr/bin/env python3
"""Extract text from a PDF specimen. Usage: python3 tools/pdf_to_text.py in.pdf out.md

Uses pdfplumber. pypdf's default extraction inserts spurious spaces inside words
on this PDF's font encoding, and its layout mode mangles word boundaries — see
OPEN-DEFECTS.md, OD-8. Unmapped glyphs (bullets) survive as (cid:N) tokens and
are left in place rather than hand-stripped, per the Preservation rule.
"""
import sys
import pdfplumber

src, dst = sys.argv[1], sys.argv[2]
with pdfplumber.open(src) as pdf:
    text = "\n\n".join(page.extract_text() or "" for page in pdf.pages)
with open(dst, "w") as f:
    f.write(text)
print(f"{len(text)} chars -> {dst}")
