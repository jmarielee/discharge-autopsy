#!/usr/bin/env python3
"""Extract text from a PDF specimen. Usage: python3 tools/pdf_to_text.py in.pdf out.md"""
import sys
from pypdf import PdfReader

src, dst = sys.argv[1], sys.argv[2]
reader = PdfReader(src)
text = "\n\n".join(page.extract_text() or "" for page in reader.pages)
with open(dst, "w") as f:
    f.write(text)
print(f"{len(reader.pages)} pages, {len(text)} chars -> {dst}")
