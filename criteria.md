# Acceptance criteria - The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
before using the final results as evidence.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
The campus_life documents are short and most of my questions ask for a specific
fact, like a deadline or policy. I expect retrieval to find the right chunk most
of the time, but 4 of 5 leaves room for one question to retrieve a related admin
document before the exact one.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
This should be 5 of 5 because every retrieved chunk has a source filename and
the answer should be grounded in those chunks. If the system gives an answer
without a source, the reader cannot check where the information came from.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" -
in at least 4 of 5 tries.

**Why this target:**
The in-corpus questions I tested had best distances from about 0.197 to 0.269,
while the out-of-corpus questions were much farther away, from about 0.825 to
0.934. Because there is a large gap between those groups, the 0.6 cutoff should
refuse most unrelated questions.

---

## 4. Chunks are usable by themselves

At least 4 of 5 sampled chunks should read as a complete thought and include
enough context to answer a question without needing the previous or next chunk.

**Why this target:**
Most campus_life documents are short student-facing notes, so a useful chunk
should keep the topic and the important detail together. If chunks are too
small, a deadline or exception could get separated from the policy it belongs
to.

---

## 5. Answers cite the correct source

For at least 4 of my 5 test questions, the answer should cite the document that
actually contains the expected answer.

**Why this target:**
Naming a source is not enough if the source is the wrong document. My questions
are about specific campus policies, so the answer should point back to the admin
or campus-life file where the fact actually appears.
