# Run log — after_source_scorer

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-28 18:29

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What is the deadline to drop a course? | pass | pass | pass |
| Which campus job earnings do not count against financial aid? | pass | pass | pass |
| Are there any benefits to declaring my major early? | pass | pass | pass |
| Can we roll over dining dollars to next semester? | pass | pass | pass |
| What is the deadline to appeal a grade? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What is the deadline to drop a course? — run 1

- Best distance: 0.2685 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, advising_registration.txt

```
Dropping a course has a window through the end of week six (*admin_add_drop_deadline.txt* and *admin_withdrawal_deadline.txt*).
```

### What is the deadline to drop a course? — run 2

- Best distance: 0.2685 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, advising_registration.txt

```
According to the document `admin_add_drop_deadline.txt`, dropping a course can be done through the end of week six.
```

### What is the deadline to drop a course? — run 3

- Best distance: 0.2685 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, advising_registration.txt

```
Dropping a course has a window through the end of week six. (Source: admin_add_drop_deadline.txt and admin_withdrawal_deadline.txt)
```

### Which campus job earnings do not count against financial aid? — run 1

- Best distance: 0.2362 (passed the gate)
- Sources retrieved: admin_campus_jobs_and_financial_aid.txt, admin_graduation_requirements.txt, admin_printing_quota.txt, admin_study_abroad.txt, money_jobs.txt

```
Work-study earnings do not count against your financial aid. This comes from `admin_campus_jobs_and_financial_aid.txt`.
```

### Which campus job earnings do not count against financial aid? — run 2

- Best distance: 0.2362 (passed the gate)
- Sources retrieved: admin_campus_jobs_and_financial_aid.txt, admin_graduation_requirements.txt, admin_printing_quota.txt, admin_study_abroad.txt, money_jobs.txt

```
Work-study earnings do not count against your financial aid the way ordinary income does (admin_campus_jobs_and_financial_aid.txt).
```

### Which campus job earnings do not count against financial aid? — run 3

- Best distance: 0.2362 (passed the gate)
- Sources retrieved: admin_campus_jobs_and_financial_aid.txt, admin_graduation_requirements.txt, admin_printing_quota.txt, admin_study_abroad.txt, money_jobs.txt

```
Work-study earnings do not count against your financial aid the way ordinary income does (admin_campus_jobs_and_financial_aid.txt).
```

### Are there any benefits to declaring my major early? — run 1

- Best distance: 0.2282 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_pass_fail_option.txt, advising_registration.txt, course_biol_160_workload.txt

```
There is no advantage to declaring early except that it assigns you a departmental adviser, who is generally more useful than the general one (admin_declaring_a_major.txt).
```

### Are there any benefits to declaring my major early? — run 2

- Best distance: 0.2282 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_pass_fail_option.txt, advising_registration.txt, course_biol_160_workload.txt

```
According to `admin_declaring_a_major.txt`, there is no advantage to declaring early except that it assigns you a departmental adviser, who is generally more useful than the general one.
```

### Are there any benefits to declaring my major early? — run 3

- Best distance: 0.2282 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_pass_fail_option.txt, advising_registration.txt, course_biol_160_workload.txt

```
There is no advantage to declaring early except that it assigns you a departmental adviser, who is generally more useful than the general one (admin_declaring_a_major.txt).
```

### Can we roll over dining dollars to next semester? — run 1

- Best distance: 0.2558 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
Yes, dining dollars roll over from the autumn semester to the spring semester, but they do not roll over from the spring semester to the following autumn semester. 

Source: admin_dining_dollars.txt
```

### Can we roll over dining dollars to next semester? — run 2

- Best distance: 0.2558 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
Yes, dining dollars roll over from the autumn semester to the spring semester, but they do not roll over from the spring semester to the following autumn semester (admin_dining_dollars.txt).
```

### Can we roll over dining dollars to next semester? — run 3

- Best distance: 0.2558 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, admin_printing_quota.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
Yes, dining dollars roll over from the autumn semester to the spring semester, but they do not roll over from the spring semester to the following autumn semester. 

Source: `admin_dining_dollars.txt`
```

### What is the deadline to appeal a grade? — run 1

- Best distance: 0.1966 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
A grade appeal must be raised within fifteen days of the grade posting. 

Source: admin_grade_appeals.txt
```

### What is the deadline to appeal a grade? — run 2

- Best distance: 0.1966 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
The deadline to appeal a grade is within fifteen days of the grade posting. 

Source: admin_grade_appeals.txt
```

### What is the deadline to appeal a grade? — run 3

- Best distance: 0.1966 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_grade_appeals.txt, admin_pass_fail_option.txt, admin_withdrawal_deadline.txt, course_stat_150.txt

```
A grade appeal must be raised within fifteen days of the grade posting. 

Source: admin_grade_appeals.txt
```
