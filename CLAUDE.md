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
| `week03/` | `2026-06-01-COMP170.md`, `ascii.py`, `hello.py` | ASCII character codes, `ord()`/`chr()`, strings, string repetition operator, drawing shapes with loops |
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

## Code Style

Student-facing example code is intentionally simple and beginner-readable. Type annotations are used on function signatures (see `quad.py`) but internal implementation stays plain. `if __name__ == "__main__":` guards are used in runnable examples to separate reusable logic from demo invocations.
