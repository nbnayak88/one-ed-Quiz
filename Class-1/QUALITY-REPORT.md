# Class 1 Publication Quality Report

**Inventory reconciliation date:** 2026-11-05  
**Repository:** `nbnayak88/one-ed-Quiz`  
**Scope:** Class-1, all 10 Labs and 40 expected Markdown volumes.

## Current repository inventory

| Check | Current finding |
|---|---|
| Expected Labs | 10 |
| Lab directories present | 10 / 10 |
| Expected Markdown question volumes | 40 |
| Question volume files present | 40 / 40 |
| Assigned canonical numbering ranges | Q1–Q10,000 |
| Expected questions per volume | 250 |
| Total question slots covered by filenames | 10,000 |
| Missing expected volume files | 0 |
| Question-by-question structural validation on current revision | Not yet rerun |
| Independent factual/editorial verification | Not certified |
| Duplicate/near-duplicate content review | Not certified |
| Class 1 reading-level and Olympiad calibration | Not certified |

## Correction to previous report

The 2026-11-04 report described **28 published volumes / 7,000 questions** and an unavailable **Q1–Q3,000** source range. That description is superseded: all twelve India, Nature and Earth volume files are now present in the live repository. The earlier 7,000-question count is **not** the current publication inventory.

## Source provenance and caution

India, Nature and Earth are reconstructed editions rather than recovered originals. Repeated concepts and formulaic questions may remain. Science and Sports were renumbered from legacy overlapping ranges into canonical Q3,001–4,000 and Q4,001–5,000 respectively.

**Publication coverage is complete at the file-inventory level; question quality is not yet certified.** Do not equate 10,000 numbered slots with 10,000 independently validated, unique, accurate questions.

## Next quality gate

1. Run `python Class-1/validate_bank.py` against the latest main branch.
2. Confirm Q1–Q10,000 continuity, A–D options, answers, explanations and each set's Super Olympiad label.
3. Detect exact and semantic duplicates; prioritize reconstructed Labs 1–3.
4. Fact-check correct answers and explanations, distractor quality and ambiguous claims.
5. Check Class 1 age suitability, difficulty progression and curriculum alignment.
6. Record reviewer sign-off before describing the bank as assessment-ready.

_This report records a live file-inventory reconciliation, not a completed question-level audit._
