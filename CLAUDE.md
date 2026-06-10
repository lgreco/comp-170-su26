# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About This Repository

This is the course repository for **COMP 170** (Introduction to Computer Science with Python), Summer 2026. It is used to distribute lecture materials, review notes, and example code to students. New weekly content is added as the course progresses.

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

> **Note:** `week03/shopping.md` is a personal shopping list accidentally committed to the repo — it is not course material and should be ignored when generating student-facing content.

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
| docs.python.org — An Informal Introduction: Text | Official docs | https://docs.python.org/3/tutorial/introduction.html#text | week03 assignment | Strings, `+`, `*`, indexing, slicing |
| docs.python.org — for Statements | Official docs | https://docs.python.org/3/tutorial/controlflow.html#for-statements | week03 assignment | `for` loop syntax and iteration over sequences |
| docs.python.org — The range() Function | Official docs | https://docs.python.org/3/tutorial/controlflow.html#the-range-function | week03 assignment | `range()` patterns for numeric loops |
| Bash cheat sheet | Reference | https://devhints.io/bash | week03 assignment | Common shell commands, shortcuts, syntax |
| Vim cheat sheet | Reference | https://vim.rtorr.com | week03 assignment | All vim modes, motion, editing, and save/quit commands |
| Vim tutorial (course repo) | In-repo reference | `tools/vim_tutorial.md` | week01 review | Modes, essential commands, workflow for this course |

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
