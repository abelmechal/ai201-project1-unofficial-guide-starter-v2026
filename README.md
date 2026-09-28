# The Unofficial Guide

Name: ERC

Corpus: `campus_life`

---

# Unit 1

## What This Does

This project is a RAG system over the `campus_life` corpus. It answers student
questions about campus policies, dining, housing, course workload, and other
practical college-life information. The system retrieves relevant chunks from
the local corpus, refuses questions that are too far outside the corpus, and
generates answers with source filenames so the user can check the answer.

## Chunking Strategy

**Chunk size:** 800 characters

**Overlap:** 120 characters

I kept the starter chunking numbers because the campus_life documents are mostly
short notes. In the sample chunks, each chunk usually contains one complete note
or one complete section, so an 800-character chunk keeps the topic and the
important detail together. The 120-character overlap gives some protection if a
longer note crosses a chunk boundary, but most of this corpus is short enough
that the fallback splitter keeps each note readable by itself.

## Sample Chunks

**Chunk 1** - source: `admin_add_drop_deadline.txt#0` - produced by: `chunker.py::fallback_split`

```text
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window - through the end of week six - but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** - source: `course_biol_160.txt#0` - produced by: `chunker.py::fallback_split`

```text
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** - source: `course_hist_118_workload.txt#0` - produced by: `chunker.py::fallback_split`

```text
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded - the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** - source: `dining_pellew_dining_hall_followup.txt#0` - produced by: `chunker.py::fallback_split`

```text
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** - source: `housing_innisfree_hall.txt#0` - produced by: `chunker.py::fallback_split`

```text
Innisfree Hall - what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

**Question:** How late can I drop a course, and when will it appear as a W?

**Answer:**

```text
(best distance 0.217, cutoff 0.6)

You can drop a course through the end of week six. A drop shows as a W on your transcript if it occurs after week two. (Source: admin_add_drop_deadline.txt)

Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt
```

**My relevance cutoff:** 0.6

The covered questions all had best distances below 0.3. The out-of-corpus
questions all had best distances above 0.8. Since there was a large gap between
those groups, I kept the cutoff at 0.6.

| Question | In corpus? | Best distance |
|---|---|---|
| What is the deadline to drop a course? | Yes | 0.2685 |
| Which campus job earnings do not count against financial aid? | Yes | 0.2362 |
| Are there any benefits to declaring my major early? | Yes | 0.2282 |
| Can we roll over dining dollars to next semester? | Yes | 0.2558 |
| What is the deadline to appeal a grade? | Yes | 0.1966 |
| What is the capital of Mongolia? | No | 0.8246 |
| How do I change the oil in a diesel engine? | No | 0.9340 |
| Who won the 1994 World Cup? | No | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8442 |
| How do I write a for loop in Rust? | No | 0.8960 |

## How I Used AI

**1.** I asked AI to explain the project after I missed the previous class. It
explained that this project is about building a RAG pipeline and deciding in
advance what counts as success. I used that explanation to understand why
`questions.py`, `criteria.md`, and the result logs matter.

**2.** I asked AI to help pressure-test my question and scorer setup. It noticed
that an expected phrase like `Yes` was too vague and that longer expected
phrases were too brittle, so I changed the expected phrases to stable key facts
like `departmental adviser` and `roll over from the autumn semester to the
spring`.

---

# Unit 2

## Run Log - Before

Run log file: `results/run_2026-09-28_1819_before.md`

Produced by: `run_eval.py::main`

Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunks are usable by themselves | 4 of 5 sampled chunks | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Answers cite the correct source | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

Real output from the run:

```text
What is the deadline to drop a course?
  run 1: pass  (best distance 0.268)
  run 2: pass  (best distance 0.268)
  run 3: pass  (best distance 0.268)

Which campus job earnings do not count against financial aid?
  run 1: pass  (best distance 0.236)
  run 2: pass  (best distance 0.236)
  run 3: pass  (best distance 0.236)

Are there any benefits to declaring my major early?
  run 1: pass  (best distance 0.228)
  run 2: pass  (best distance 0.228)
  run 3: pass  (best distance 0.228)

Can we roll over dining dollars to next semester?
  run 1: pass  (best distance 0.256)
  run 2: pass  (best distance 0.256)
  run 3: pass  (best distance 0.256)

What is the deadline to appeal a grade?
  run 1: pass  (best distance 0.197)
  run 2: pass  (best distance 0.197)
  run 3: pass  (best distance 0.197)

Out-of-scope questions (the gate should refuse these):
  refused  (best distance 0.825)  What is the capital of Mongolia?
  refused  (best distance 0.934)  How do I change the oil in a diesel engine?
  refused  (best distance 0.886)  Who won the 1994 World Cup?
  refused  (best distance 0.844)  What is the recommended dosage of ibuprofen for a headache?
  refused  (best distance 0.896)  How do I write a for loop in Rust?
  -> gate refused 5 of 5
```

Sample generated answers from the same run:

```text
Work-study earnings do not count against your financial aid the way ordinary income does (admin_campus_jobs_and_financial_aid.txt).
```

```text
According to `admin_declaring_a_major.txt`, there is no advantage to declaring early except that it assigns you a departmental adviser, who is generally more useful than the general one.
```

```text
Dining dollars roll over from the autumn semester to the spring, but they do not roll over from the spring to the following autumn.

Source: admin_dining_dollars.txt
```

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | All five questions passed in all three runs, and each best result pointed to the document containing the answer. |
| 2 | Every answer names a source | MET | Every generated answer in the run log included at least one source filename. |
| 3 | The relevance gate stops out-of-corpus questions | MET | The gate refused 5 of 5 unrelated questions, which is above the 4 of 5 target. |
| 4 | Chunks are usable by themselves | MET | The five sampled chunks read as complete notes or complete sections and included the topic plus useful detail. |
| 5 | Answers cite the correct source | MET | The answers cited the files that actually contained the expected facts, such as `admin_dining_dollars.txt` and `admin_grade_appeals.txt`. |

## Diagnoses

No criteria missed in the official before run. The main thing I would tighten
next is the scorer: it currently checks whether a key phrase appears in the
answer, but it does not automatically verify whether the cited source is the
correct source. I judged criterion 5 manually from the run log.

## The Improvement

**What I changed:** Before the official eval run, I made the expected phrases in
`questions.py` shorter and more stable so the scorer checked the important fact
instead of requiring one exact sentence.

**Why I picked it:** Earlier trial runs showed correct answers being marked
wrong because the model used different wording. Shorter expected phrases made
the scorer measure correctness instead of sentence matching.

### Run Log - After

Run log file: `results/run_2026-09-28_1821_after.md`

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunks are usable by themselves | 4 of 5 sampled chunks | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Answers cite the correct source | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

**Did it help?**

The system stayed at the same result: all five questions passed three times and
all five out-of-corpus questions were refused. The expected-phrase cleanup made
the eval stable before these official runs, but there was no additional miss to
fix after the before log.

## What's Still Broken

The system works for my current campus_life questions, but the scorer is still
simple. It checks for expected phrases in the generated answer, so it would not
catch every possible source-citation problem automatically.

## What I'd Do Differently

I would write criterion 5 with an automatic scoring plan from the beginning,
such as checking that the expected source filename appears in the answer. That
would make source correctness easier to measure instead of relying on manual
review of the run log.
