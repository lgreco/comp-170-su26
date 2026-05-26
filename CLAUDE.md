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

## Code Style

Student-facing example code is intentionally simple and beginner-readable. Type annotations are used on function signatures (see `quad.py`) but internal implementation stays plain. `if __name__ == "__main__":` guards are used in runnable examples to separate reusable logic from demo invocations.
