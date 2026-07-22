# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About This Repository

This is the course repository for **COMP 170** (Introduction to Computer Science with Python), Summer 2026. It is used to distribute lecture materials, review notes, and example code to students. New weekly content is added as the course progresses.

This is the student-facing counterpart to the private `comp170su26/` folder in the `redesign-foundational-sequence` repo, where weekly plans and reviews are drafted before publishing here.

## Running Code

Python 3 is the only runtime used in this course. Run any script directly:

```bash
python3 quad.py
python3 <week-folder>/<script>.py
```

There is no build step, no package manager, and no virtual environment — scripts use only the Python standard library.

## Repository Structure

Content is organized by week:

- `weekNN/` — weekly review notes and exercises (Markdown + `.py` files)
- `tools/` — standalone reference documents (e.g., `vim_tutorial.md`)
- Root-level `.py` files (e.g., `quad.py`) are standalone example scripts used in class

### Current content

| Week | Files | Topics |
|------|-------|--------|
| `week01/` | `week01-review.md` | Week 1 review notes |
| `week02/` | `week02-review.md`, `2026-05-26-COMP170.md`, `2026-05-27-COMP170.md`, `interest.py`, `interest_pro.py` | Terminal basics, compound interest program, separation of concerns (input / logic / output) |
| `week03/` | `2026-06-01-COMP170.md`, `2026-06-03-COMP170.md`, `ascii.py`, `hello.py`, `demo_scope.py`, `week03-assignment.md`, `week03_solutions.py` | ASCII character codes, `ord()`/`chr()`, strings, string repetition operator, `int()` conversion, positional number systems (decimal/binary/hex), drawing shapes with loops, scope and indentation; `demo_scope.py` is a `range()` / indentation demo used in class; `week03_solutions.py` contains posted solutions for all four assignment problems |
| `week04/` | `2026-06-08-COMP170.md`, `2026-06-09-COMP170.md`, `2026-06-10-COMP170.md`, `airline.py`, `seat_arrangements.py`, `temperatures.py`, `claude_demo.md`, `week04-assignment.md` | Booleans, `and`/`or`, `==` vs. `=`, the modulo operator, the airplane seating problem (`%` and `//`), lists (creation, zero-based indexing, `len()`), the cumulative algorithm (running sum/average) |
| `week05/` | `2026-06-15-COMP170.md`, `2026-06-16-COMP170.md`, `2026-06-17-COMP170.md`, `play_with_words.py`, `fun_with_words.py`, `managing_complexity.py`, `that_other_program.py`, `week05-assignment.md` | `sentence.split()`, plain vs. enhanced `for` loops, packaging logic into a function with type hints/docstrings/input validation (`managing_complexity.py`), running a function via `if __name__ == "__main__":` vs. importing it from another file (`that_other_program.py`) |
| `week06/` | `2026-06-22-COMP170.md`, `2026-06-23-COMP170.md`, `2026-06-24-COMP170.md`, `cumulative.py`, `fact.py`, `parse_brute_force.py`, `week06-assignment.md` | Loop variable naming, accumulator pattern (running sum/product), factorials and first look at recursion, reinventing `str.split()` character by character (`parse_brute_force.py`), debugging consecutive-delimiter bug, function headers (type hints, default parameters); assignment asks students to write pseudocode for `str.find()`, `str.upper()`, and `str.isalpha()` analogues |
| `week07/` | `2026-06-29-COMP170.md`, `2026-06-30-COMP170.md`, `2026-07-01-COMP170.md`, `demo_contains.py`, `find.py`, `occurrences.py`, `week07-assignment.md`, `week07-solutions.md` | `.find()` vs. `.index()`, writing `contains`/`indexOf` from scratch, definite vs. indefinite loops, infinite loops, Boolean logic in loop conditions, counting occurrences, guard clauses against missing input; assignment/solutions cover pseudocode for `positions()` (every occurrence of a letter) and `find_substring()` (substring search via nested loops) |
| `week08/` | `2026-07-06-COMP170.md`, `2026-07-07-COMP170.md`, `2026-07-08-COMP170.md`, `mathemagics.py`, `mathemagics-package/`, `quad.py`, `quadratic_flow_chart.svg`/`.png`/`.drawio`, `gpa.py`, `test_math_naive.py`, `test_math_plain.py`, `test-math.py`, `week08-assignment.md`, `week08-solutions.py` | The quadratic equation and discriminant, imaginary/complex numbers as tuples `(real_part, imaginary_part)`, tuples vs. lists, designing `solve_quadratic()` case by case with a flow chart and matching pseudocode, three levels of testing (naive prints, plain helper functions, `unittest`), and testing the published [`mathemagics` PyPI package](https://pypi.org/project/mathemagics/) (`mathemagics-package/` holds its packaging files); designing a GPA tracker from a vague request (`gpa.py`'s `enter_grade`, averaging letter-grade values into a running GPA) and catching bad input (lowercase or mistyped letter grades, negative GPA); assignment introduces `raise`/`ValueError` via bank-withdrawal and bank-deposit functions (narrated with in-place comments rather than separate pseudocode; deposit also prints a non-error IRS-notice warning for amounts $\ge \$10{,}000$) and asks students to test both, plus a reflection on the week07 solutions; `week08-solutions.py` holds the posted solutions |
| `week09/` | `2026-07-13-COMP170.md`, `2026-07-14-COMP170.md`, `2026-07-15-COMP170.md`, `age.py`, `atm.py`, `banana.py`, `multi.py`, `sum.py`, `week09-assignment.md`, `week09-solutions.py` | Nested loops (`multi.py`'s multiplication table, commented and cleaned up; counting iterations of doubly/triply nested loops), substring search by scanning for a starting-letter match and confirming the rest with a running Boolean `and` (`banana.py`, searching for `"as"` inside `"bananas"`; fixed from an in-class syntax error and commented), `try`/`except` around `int()` conversion of bad `input()` (`age.py`'s `get_year()`, birth-year example; now implements the `max_tries` cap and the $1901$–$2025$ reasonableness check the in-class version had left as a TODO comment), multi-branch `if`/`elif`/`else` vs. separate `if` statements for the ATM withdrawal (why separate `if`s fall through where `elif` doesn't), raising errors vs. giving the user another chance to retry, and rewriting the withdrawal program with a retry loop and `try`/`except` (`atm.py`, organized into `withdraw()`/`attempt_withdrawal()`/`main()`, giving up gently with a message after `max_tries` failed attempts); previews memory vs. storage for next week. `sum.py` is an in-progress live-coding scratch file and currently contains a syntax error. Assignment has students write their own `ATM.py` combining a `withdraw()` retry loop with a new `deposit()` that distinguishes cash (whole dollars only) from cheque (cents allowed) deposits, both with limited retries, plus a reflection on the week08 solutions; `week09-solutions.py` holds the posted solutions for `withdraw()`/`attempt_withdrawal()` and `deposit()`/`attempt_deposit()`, used in week10's reflection problem. |
| `week10/` | `monday-async.md`, `2026-07-21-COMP170.md`, `2026-07-22-COMP170.md`, `demo.txt`, `SimpleFileOps.py`, `StringAsObject.py`, `records.txt`, `records.csv`, `week10-assignment.md` | Monday async day (`monday-async.md` lists shared COMP 170/COMP 271 LeetCode practice; only the COMP 170-labeled items apply to this course, and they are independent practice, not part of the week10 assignment). What a file is and why files are naturally hierarchical, the history of file storage (punched cards, magnetic tape, spinning disks, solid-state), the three-tier von Neumann memory hierarchy (registers/main memory/storage), and text vs. binary files. Creating and writing files in Python, why writes sit in a buffer until `.close()`, write mode (wipes the file) vs. append mode (keeps existing content) vs. read mode (no writes allowed), and reading a file line by line with `.readline()` and `.rstrip()` (`SimpleFileOps.py`, reading `demo.txt`); closes by tying files back to the "four pillars" (strings, loops, if statements, arrays) and motivating labeled formats (XML/JSON/YAML) via the fragile comma-separated `records.txt`/`records.csv` student-record example. `StringAsObject.py` is an empty in-class scratch file. Assignment has students write `groceries.py` (write mode, list building) and `diary.py` (append mode, growing log), plus a reflection on the week09 solutions. |
| `tools/` | `vim_tutorial.md` | Vim reference |

### Tutorial file naming convention

Dated tutorial files follow the pattern `YYYY-MM-DD-COMP170.md` and live inside the relevant week folder. They are narrative lesson documents written for students, combining explanation, examples, pseudocode, and runnable Python snippets.

### `week03/2026-06-01-COMP170.md` content outline

- ASCII background and the `ord()`/`chr()` functions
- Four anchor values worth memorizing: 32 (space), 48 (`'0'`), 65 (`'A'`), 97 (`'a'`)
- Hand-drawn ASCII art examples (coffee, rocket, skull, cat, game controller)
- What strings are and why they matter
- The `*` operator on strings (repetition vs. arithmetic)
- Drawing a triangle: line-by-line analysis, pattern discovery, pseudocode, LaTeX notation, hard-coded vs. loop implementation
- Loop-friendly shapes: diamond and bar chart

### `week03/week03-assignment.md` content outline

- Assigned reading: *Introducing Python, 3rd Ed.* Chapters 1–4 and Chapter 7 (`for` section); students access via LUC O'Reilly account
- CLI + vim workflow walkthrough (step-by-step commands, folder navigation, troubleshooting)
- Problem 1: string repetition prediction exercise (`*` operator, `+` concatenation)
- Problem 2: staircase drawing with a `for` loop and `range()`; students write pseudocode first
- Problem 3: right-aligned triangle using `' ' * (N-i) + '*' * i` per row
- Problem 4 *(challenge)*: filled circle using `import math` and `math.sqrt()`; covers discretization and terminal aspect ratio

### `week03/week03_solutions.py` content outline

- Problem 1: all eight `print` expressions with predicted output as inline comments; written answers to the three reflection questions (commutativity of `*`, operator precedence of `*` vs `+`, `'*' * 0` as empty string)
- Problem 2: pseudocode retained as comments; explanation of why `range(1, N+1)` is used instead of `range(N)`; staircase loop for `N = 5`
- Problem 3: row-by-row table (spaces = `N-i`, stars = `i`) as a comment; right-aligned triangle loop for `N = 5` using `' ' * (N-i) + '*' * i`
- Problem 4: three comment blocks explaining the circle equation ($x^2 + y^2 = r^2$), discretization (`int(x_max + 0.5)`), and aspect-ratio compression; complete circle loop for `r = 8`

### `week06/week06-assignment.md` content outline

- Assigned reading: *Introducing Python, 3rd Ed.* Chapter 10 (Functions) — second assignment; focus this week is on using function vocabulary (inputs, outputs, def line) to write pseudocode
- Week at a Glance covering June 22–24: accumulator pattern, factorials/recursion, reinventing `split`, debugging, function headers
- Introduction to pseudocode: the squared-paper/grid mental model; worked example (counting spaces in a string)
- Problem 1: pseudocode for finding the first occurrence of a character — mirrors `str.find()`; example "Chicago" / 'i' → position $2$
- Problem 2: pseudocode for converting a string to uppercase — mirrors `str.upper()`; hint uses ASCII gap of $32$ between `'a'` ($97$) and `'A'` ($65$)
- Problem 3: pseudocode for deciding if a string is a word (letters only) — mirrors `str.isalpha()`; table distinguishes `"HELL0"` (zero, not a word) from `"hELlo"` (all letters)
- Problem 4: reflection on Week 5 posted solutions — five questions covering `find()` vs. `index()` failure behavior, case sensitivity in `.count()`, why spaces disqualify a word (grid model), method chaining, and a free-choice comparison

> **Note:** `week03/shopping.md` is a personal shopping list accidentally committed to the repo — it is not course material and should be ignored when generating student-facing content.

## Linking to Files in Assignments

When an assignment markdown file (`weekNN-assignment.md`) mentions a `.py` file by name — e.g. "the `atm.py` file from class" — turn its first mention into a Markdown link to that file, e.g. `` [`atm.py`](./atm.py) `` (or `` [`atm.py`](../weekNN/atm.py) `` if it lives in a different week's folder). Only link a file that actually exists in the repo at the time of writing; don't link a file students haven't created yet (e.g. their own `problem1.py`). Subsequent mentions of the same file later in the document can stay as plain backticked text — no need to repeat the link.

## Assignment Submission Instructions

Every assignment must end with a **"How to Submit"** section (after the Quick Reference). Use this template, substituting the correct week number:

```markdown
## How to Submit

Upload your work on **Sakai** under the assignment for **Week NN**.

Submit only your Python files:

\```
problem1.py
problem2.py
...
\```

No screenshots, no PDFs, no other file types — Python files only. Confirm with `ls` that each file exists before you upload.
```

- The Sakai assignment name matches the week the assignment was created (e.g., Week 03, Week 04).
- List only the `.py` files students are expected to submit.
- Do not mention any other submission method.

Every assignment must also end with a **"How Your Work Is Evaluated"** section immediately after "How to Submit". Use this text verbatim:

```markdown
## How Your Work Is Evaluated

**Submission credit.** Submitting an assignment earns you 1 point; not submitting earns 0. This is not a score for quality — it simply records that you completed the work on time.

**No late work, no extensions.** We discuss solutions in class immediately after the deadline, and solutions are posted at the same time. Because the answers are public from that moment on, late submissions cannot be accepted and deadlines cannot be extended.

**Self-evaluation.** After solutions are posted, you evaluate your own work. Using the posted solutions and Leo's written instructions as a guide, you decide what you understood, what you got wrong, and what you need to practice to avoid the same mistakes in the future. Making mistakes is how learning happens. Not repeating them is the evidence that it did.
```

## Reading Materials

Resources assigned or referenced across the course. Use this table when adding reading links to new assignments so that descriptions stay consistent and URLs are not duplicated.

| Resource | Type | URL | First assigned | Coverage |
|----------|------|-----|----------------|----------|
| *Introducing Python, 3rd Ed.* — Ch. 1: Introduction | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ | week03 assignment | What Python is, the interpreter, running a first program |
| *Introducing Python, 3rd Ed.* — Ch. 2: Types and Variables | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch02.html#id642 | week03 assignment | Data types, variables, how values are stored and named |
| *Introducing Python, 3rd Ed.* — Ch. 3: Numbers | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html | week03 assignment | Integers, floats, arithmetic |
| *Introducing Python, 3rd Ed.* — Ch. 4: Strings | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch04.html | week03 assignment | String creation, `+`, `*`, indexing, slicing |
| *Introducing Python, 3rd Ed.* — Ch. 7: Loops | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html | week03 assignment | `for` loops (first half only assigned); `while` loops deferred |
| *Introducing Python, 3rd Ed.* — Ch. 8: Lists | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html#c08_h_list_create | week04 assignment | Creating and working with lists; indexing, slicing, mutating |
| *Introducing Python, 3rd Ed.* — Ch. 10: Functions | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html | week05 assignment | Defining functions with `def`, parameters/arguments, `return`, default parameter values, docstrings; reassigned in week09 for a second pass, with the chapter's remaining sections (first-class functions, function arguments as tuples, inner functions, closures, lambda, generators, generator comprehensions, decorators, recursion, async functions) marked optional there — still not required reading |
| docs.python.org — An Informal Introduction: Text | Official docs | https://docs.python.org/3/tutorial/introduction.html#text | week03 assignment | Strings, `+`, `*`, indexing, slicing |
| docs.python.org — for Statements | Official docs | https://docs.python.org/3/tutorial/controlflow.html#for-statements | week03 assignment | `for` loop syntax and iteration over sequences |
| docs.python.org — The range() Function | Official docs | https://docs.python.org/3/tutorial/controlflow.html#the-range-function | week03 assignment | `range()` patterns for numeric loops |
| docs.python.org — Defining Functions | Official docs | https://docs.python.org/3/tutorial/controlflow.html#defining-functions | week05 assignment | `def` syntax, default argument values, docstrings |
| docs.python.org — Errors and Exceptions | Official docs | https://docs.python.org/3/tutorial/errors.html | week08 assignment | `raise`, `ValueError`, `try`/`except` |
| *Learning Python, 6th Ed.* — Ch. 34: Exception Basics | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/learning-python-6th/9781098171292/ch34.html#id4405 | week08 assignment | `raise`, `try`/`except`, built-in exception types |
| `mathemagics` on PyPI | Published package | https://pypi.org/project/mathemagics/ | week08 assignment | Published version of `solve_quadratic()`, used to demonstrate testing a real, installable module |
| Bash cheat sheet | Reference | https://devhints.io/bash | week03 assignment | Common shell commands, shortcuts, syntax |
| Vim cheat sheet | Reference | https://vim.rtorr.com | week03 assignment | All vim modes, motion, editing, and save/quit commands |
| Vim tutorial (course repo) | In-repo reference | `tools/vim_tutorial.md` | week01 review | Modes, essential commands, workflow for this course |
| *Introducing Python, 3rd Ed.* — Ch. 20: Files | Textbook (O'Reilly) | https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch20.html | week10 assignment | Reading and writing files |
| Computer file (Wikipedia) | Reference | https://en.wikipedia.org/wiki/Computer_file | week10 assignment | What a file is at the operating-system level |
| Memory & Storage Timeline (Computer History Museum) | Reference | https://www.computerhistory.org/timeline/memory-storage/ | week10 assignment | Historical context for persistent storage vs. in-memory structures |

> Students access O'Reilly via their LUC (Loyola) institutional account.

## Code Style

Student-facing example code is intentionally simple and beginner-readable. Type annotations are used on function signatures (see `quad.py`) but internal implementation stays plain. `if __name__ == "__main__":` guards are used in runnable examples to separate reusable logic from demo invocations.

## Math Formatting

All mathematical expressions in course documents must be written in LaTeX, consistent with the existing lecture files. Use `$...$` for inline math and `$$...$$` for display (block) math.

| Context | Format | Example |
|---------|--------|---------|
| Variable or value in prose | Inline: `$...$` | "the number of spaces is $N - i$" |
| Equation worth its own line | Display: `$$...$$` | $$x^2 + y^2 = r^2$$ |
| Python code or expression | Backtick code: `` `...` `` | "call `range(1, N+1)`" |

**Key rule:** if it is a mathematical object (variable, formula, inequality, equation), use LaTeX. If it is Python syntax or a terminal command, use a code span or code block. Never use Unicode math characters (², ≤, √, →) in place of LaTeX.
