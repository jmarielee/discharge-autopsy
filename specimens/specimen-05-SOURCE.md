# Specimen 05 — source

**Title:** Taking Care of Myself: A Guide for When I Leave the Hospital
**Publisher:** Agency for Healthcare Research and Quality, Rockville, MD
**Publication:** AHRQ Pub. No. 10-0059, April 2010
**Source URL:** https://www.ahrq.gov/sites/default/files/publications/files/goinghomeguide.pdf
**Retrieved:** 2026-08-06
**Rung:** PUBLIC

**Rights:** A work of the United States Government, not subject to copyright
protection under 17 U.S.C. § 105. The `.pdf` is committed as an explicit
exception to the `.gitignore` rule excluding PDFs, which exists to prevent
patient-record material entering history. This document contains none.

**Relationship to specimen-04.** Same source PDF, byte-identical. The only
difference is the text extraction. Specimen-04's extraction was defective
(OD-8); specimen-05's was produced by the corrected `tools/pdf_to_text.py`
using pdfplumber. Specimen-04 is preserved as-is because it is the text the
first run actually read.

**Known artifact:** four `(cid:0)` tokens appear where bullet glyphs are
unmapped in the source font. Left in place rather than hand-stripped, per the
Preservation rule.
