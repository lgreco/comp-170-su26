# COMP 170 — Course Review, Summer 2026

The course ran for eleven weeks, from a first `Hello, World!` in Bash and `vim` to reading a real book off the internet and counting its words into a dictionary. This document looks back at that arc, with particular attention to how the course built up what Leo calls the **four pillars of programming: strings, if statements, loops, and arrays** — and what, given eleven weeks, there simply wasn't time to cover.

---

## 1. Course Progression

### Weeks 1–2: Foundations before syntax

Week 1 was deliberately not about Python at all — it was about the shell. Before writing a single program, students learned that a terminal is a conversation with an interpreter (`pwd`, `ls`, `cd`, `vim`), and that `python3 file.py` is itself just another command in that conversation. Only after that did `str`, `int`, and `float` show up, along with the first hint of an operator behaving differently depending on the type of its operands (`+` on strings vs. numbers). Week 2 built the first real program — compound interest — and used it to introduce **separation of concerns**: input, logic, and output as distinct sections of a program (`interest.py` → `interest_pro.py`).

### Weeks 3–4: Strings and the first pillar, then if statements

Week 3 is where **strings** properly entered as a pillar: ASCII codes, `ord()`/`chr()`, the four anchor values (32, 48, 65, 97), and string repetition (`*`) as something conceptually different from arithmetic multiplication. This week also introduced `for` loops and `range()` through the classic "draw a shape" exercises — triangles, staircases, diamonds — which doubled as a first exposure to pattern discovery and pseudocode. Week 4 introduced the second pillar, **if statements** (Booleans, `and`/`or`, `==` vs. `=`), fused immediately with the modulo operator in the airplane-seating problem — a nice early example of `if` and arithmetic reasoning about the same problem. Week 4 also introduced the third pillar, **arrays** (Python lists): creation, zero-based indexing, `len()`, and the cumulative/running-sum pattern that would recur for the rest of the course.

### Weeks 5–6: Loops become the main event, and functions arrive

Week 5 introduced `sentence.split()` and the enhanced `for` loop, but its real contribution was packaging logic into a function with type hints, docstrings, and input validation — the first time students had to think about a program as more than one script (`that_other_program.py` showed calling a function from another file via import vs. running it directly). Week 6 pushed on the fourth pillar, **loops**, hard: the accumulator pattern, factorials and a first look at recursion, and — notably — reinventing `str.split()` from scratch character by character (`parse_brute_force.py`), including a live debugging session around the classic consecutive-delimiter bug. This is where all four pillars start actively cooperating rather than being introduced one at a time.

### Weeks 7–8: Search, correctness, and testing

Week 7 had students write `.find()`/`.index()`-style logic themselves, and introduced the definite-vs-indefinite loop distinction along with the danger of infinite loops — an important lesson once loops stopped being purely decorative (drawing shapes) and started doing real search work. Week 8 was the most mathematically dense week: the quadratic formula, complex numbers represented as tuples, and — significantly — **three levels of testing** (naive prints, plain assertion functions, and `unittest`), including testing a real published PyPI package (`mathemagics`). This week is where "does my code work" stopped being answered by eyeballing output and started being answered by writing another program to check the first one.

### Weeks 9–10: Robustness and persistence

Week 9 centered on `try`/`except` and validating user input (the birth-year and ATM-withdrawal examples), plus the important but subtle distinction between raising an error and giving the user another chance to retry — a design decision, not just a syntax choice. Week 10 moved outside the running program entirely: what a file is, why writes buffer until `.close()`, the three file modes (write/append/read), and reading files line by line. It closed by tying everything back to the four pillars and motivating labeled formats (JSON/XML/YAML) with the fragile comma-separated `records.txt` example.

### Week 11: Bringing it all together

The final week fused every pillar into one running example: reading *A Tale of Two Cities* from disk (and then from a URL, via `urllib.request`) and counting word frequencies. This week deliberately included a bug-for-its-own-sake exercise — `bad_logic_example.py`, an `IndexError`-crashing first draft kept in the repository on purpose — to make the point that a loop's stopping condition being wrong doesn't just break the loop, it silently breaks everything downstream. The two-synchronized-lists approach ("array synchronization") was built first, shown to be fragile, and then replaced with a **dictionary** — the closest the course came to introducing a data structure beyond the list. The course ended with functions used to clean up a messy twenty-line block into two readable lines, closing the loop back to Week 5's separation-of-concerns lesson.

### The four pillars, end to end

| Pillar | First introduced | Recurred |
|---|---|---|
| Strings | Week 3 (ASCII, `*`, repetition) | Weeks 5–7 (`split`, search, substring logic), Week 11 (word counting) |
| If statements | Week 4 (Booleans, `and`/`or`) | Weeks 8–9 (branching by case, ATM logic), Week 11 (word-found branching) |
| Loops | Week 3 (`for`/`range`, shapes) | Weeks 6–9 (accumulator, nested loops, retry loops), Week 11 (line-by-line file reading) |
| Arrays (lists) | Week 4 (indexing, `len()`) | Weeks 6–9 (cumulative pattern), Week 11 (synchronized lists → dictionary) |

By the end, no week introduced a pillar in isolation — every exercise from Week 6 onward asked students to combine at least two, and the capstone word-counter in Week 11 required all four plus a new structure (the dictionary) to replace the weakest pillar-based solution.

---

## 2. What the Course Didn't Have Time For

Every course is defined as much by what it deliberately leaves out as by what it covers — eleven weeks is enough to build real fluency in the four pillars, but not enough to survey the rest of the language or the discipline. A few gaps worth naming, and pursuing on your own if you want to go further:

- **Object-oriented programming.** Classes and objects were introduced and demonstrated but never treated in depth — everything was functions and data structures. `class`, `self`, `__init__`, and inheritance are a natural next step now that dictionaries have appeared.
- **Additional data structures.** Sets, tuples-as-records (beyond the complex-number use in Week 8), and nested dictionaries/lists (JSON-shaped data) were mentioned in passing (Week 10) but never built by hand.
- **Recursion, properly.** Week 6 gave a first look via factorial, but recursion as a general problem-solving tool (trees, divide-and-conquer, base-case design) was never revisited.
- **Algorithmic complexity.** We discussed why nested loops are often slower, or how to reason about a program's efficiency as input size grows — relevant the moment the word-counter is run against a much bigger book, but there is so much more to cover in future courses, including the infamous *theta* notation which a lot of people call *big-Oh* notation.
- **Error handling beyond `try`/`except`.** Custom exception classes, exception chaining, and `finally` blocks were not covered — Week 9 covered only the basics needed for input validation.
- **Command-line arguments and `argparse`, or writing reusable modules/packages.** Week 8's `mathemagics-package/` briefly showed what an installable package looks like, but building one from scratch wasn't covered.
- **Version control (git).** Students used a git-hosted repository all term without ever being taught git itself — `add`/`commit`/`push`, branches, or how to read a diff.
- **Regular expressions.** Week 11's punctuation problem (`"times,"` vs. `"times"`) is exactly the kind of problem regex solves cleanly, but regex itself was never introduced.
- **Working with real APIs or structured web data.** Week 11 touched `urllib.request` for a single plain-text file; JSON APIs, HTTP status codes, and request/response structure were not covered.

None of these are urgent — the four pillars are the load-bearing skill, and everything above is built on top of them. But if you want to keep going, OOP and basic git literacy are probably the highest-leverage next steps, since almost every real Python codebase you'll encounter next assumes both.
