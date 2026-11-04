# Class 1 Publication Quality Report

**Publication date:** 2026-11-04  
**Target repository:** `nbnayak88/one-ed-Quiz`  
**Scope:** 40 planned Markdown volumes; 28 published and structurally inspected.

## Verified structural results

| Check | Result |
|---|---|
| Uploaded source volumes | 28 |
| Questions in each uploaded volume | 250 (validated) |
| Question ID continuity inside each volume | Yes (validated) |
| Published canonical range | Q3,001–Q10,000 |
| Published questions with no range gaps in that interval | 7,000 |
| Missing canonical range | Q1–Q3,000 (12 volumes) |
| Answer line in source questions | Present in the 7,000 source questions during local audit |
| Explanation line in source questions | Present in the 7,000 source questions during local audit |
| Verified factual correctness of every answer | NOT yet independently reviewed |
| Verified absence of question-stem duplicates | NOT yet independently reviewed |
| Verified age/difficulty and syllabus fit | NOT yet independently reviewed |

## Source-availability gap

India (Q1–Q1,000), Nature (Q1,001–Q2,000), and Earth (Q2,001–Q3,000) were recorded as complete in historical chat progress reports, but full source Markdown files could not be found in current conversation attachments or accessible file search. Their folders contain only navigation/availability information, never invented filler questions.

## Reindexing

Historical Science Q1–Q1,000 is remapped to Q3,001–Q4,000. Historical Sports Q1,001–Q2,000 is remapped to Q4,001–Q5,000. This resolves canonical-number collisions and preserves each Lab's position in the 10,000-question series.

## Editorial next pass

Check answer correctness, distractor plausibility, repeated question stems, grade-appropriate difficulty, ambiguous claims, syllabus mapping, and whether every 25th question is marked as a Super Olympiad Challenge. Use `validate_bank.py` for automated structural checks, then human review for learning quality.
