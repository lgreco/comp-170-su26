# COMP 170 — Week 7 Assignment

## Week at a Glance

Here is a concise summary of what we covered in class this week. If anything felt unclear in lecture, start here.

### June 29 — `find` vs. `index`, and Writing Our Own `indexOf` ([notes](./2026-06-29-COMP170.md))

We compared `.find()` and `.index()` for locating a character in a string: both return the same position when the character is present, but `.index()` raises a crash-causing error when it's absent, while `.find()` returns $-1$. We wrote our own `contains` and `indexOf` methods in [`demo_contains.py`](./demo_contains.py) and [`find.py`](./find.py) to see that behavior implemented from scratch, and discussed why $-1$ as a sentinel value is a little riskier in Python than in other languages — negative indices are meaningful here (`"Arlo"[-1]` is `"o"`).

### June 30 — Loops, and Boolean Logic in Loop Conditions ([notes](./2026-06-30-COMP170.md))

We introduced **definite loops** (a fixed number of repetitions known in advance) and **indefinite loops** (repeat until a condition changes), and looked at what causes an **infinite loop** — a condition that can never become false, or a loop variable that never gets updated. We connected this to Boolean logic: the `while` condition in `find.py` is an AND expression — keep going as long as we haven't reached the end of the string **and** haven't found the target yet.

### July 1 — Counting Occurrences, and Guarding Against Missing Input ([notes](./2026-07-01-COMP170.md))

We wrote pseudocode first, then Python, for counting how many times a letter appears in a string ([`occurrences.py`](./occurrences.py)), and compared a position-based loop, an enhanced `for` loop, and a one-line version. We also added a guard clause that checks the string and character actually exist before doing any work, so the method reports $-1$ instead of crashing on missing input.

---

## Suggested Reading

[**Chapter 3 — Numbers**](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch03.html#c03_h_booleans), focusing on the **Booleans** section (*Introducing Python, 3rd Edition*, Bill Lubanovic, on O'Reilly Learning). We used Boolean expressions all week to build precise loop conditions — "keep going while X **and** not Y." This section gives you the vocabulary (`and`, `or`, `not`, truth values) behind what we did on the whiteboard June 30.

Access to the O'Reilly chapter requires an account. You have one — use your LUC email to log in.

---

## A Reminder About Pseudocode

As in Week 6, you are writing **pseudocode** — a plain-English, step-by-step description of an algorithm — before any Python. See the [Week 6 assignment](../week06/week06-assignment.md#what-is-pseudocode) for the full explanation of what makes pseudocode good and the squared-paper mental model for stepping through a string one character at a time.

---

## The Problems

**What to submit:** Write your pseudocode as comments inside a Python file. You are welcome to also write Python code alongside it to check your thinking, but it is the plain-English pseudocode that will be read and evaluated.

---

### Problem 1 — Finding Every Occurrence

**Goal:** Write pseudocode for a function `positions` that takes a single letter and a string, and returns a **list** containing every position where that letter appears. If the letter does not appear at all, the function returns an empty list.

**Example:**

```
Letter: 'a'
String: "banana"
Answer: [1, 3, 5]
```

Why `[1, 3, 5]`? The characters of `"banana"` occupy positions $0, 1, 2, \ldots$:

```
Position:  0     1     2     3     4     5
           +-----+-----+-----+-----+-----+-----+
Character: |  b  |  a  |  n  |  a  |  n  |  a  |
           +-----+-----+-----+-----+-----+-----+
```

The letter `'a'` appears at positions $1$, $3$, and $5$ — so `positions('a', 'banana')` returns `[1, 3, 5]`.

This is a close relative of Problem 1 from Week 6 (finding the *first* occurrence with `.find()`), but here the function does not stop at the first match — it keeps looking for every match, all the way to the end of the string.

**Write your pseudocode for this function.** Your description should explain:
- What the function needs to know (its inputs).
- Where the results are collected as the function steps through the string.
- How it recognizes a match and what it does when one is found.
- What it reports when the letter never appears — and why an empty list, and not $-1$, is the right way to report "not found" here.

Create a file called `problem1.py`. Write your pseudocode as comments:

```python
# Problem 1 — Finding Every Occurrence
#
# Inputs: ...
# Output: ...
#
# Steps:
#   1. ...
#   2. ...
#   ...
```

---

### Problem 2 — Finding a Substring

**Goal:** Write pseudocode for a function that takes two strings and finds the position where the **first string** begins inside the **second string**. If the first string does not appear inside the second at all, the function returns $-1$. This mirrors the behavior of `str.find()` when it is given a substring rather than a single character.

**Example:**

```
First string:  "cag"
Second string: "Chicago"
Answer:        3
```

Why $3$? The characters of `"Chicago"` occupy positions $0, 1, 2, \ldots$:

```
Position:  0     1     2     3     4     5     6
           +-----+-----+-----+-----+-----+-----+-----+
Character: |  C  |  h  |  i  |  c  |  a  |  g  |  o  |
           +-----+-----+-----+-----+-----+-----+-----+
```

`"cag"` begins matching at position $3$: the character at position $3$ is `'c'`, the character at position $4$ is `'a'`, and the character at position $5$ is `'g'` — three characters in a row that match `"cag"` exactly. So the function reports $3$, the position where the match *starts*.

This is a harder problem than Problem 1 of Week 6, because a single-character comparison is no longer enough — at each position in the second string, you must check whether the *whole* first string matches, character by character, starting there.

**Write your pseudocode for this function.** Your description should explain:
- What the function needs to know (its inputs), and which is the string being searched *for* versus searched *within*.
- How it checks, starting at a given position, whether the whole first string matches.
- What happens as soon as a single character fails to match during that check.
- What it reports when a full match is found, and what it reports when no starting position works.
- What should happen if the first string is longer than the second string — think about why no starting position could ever succeed in that case.

Create a file called `problem2.py`. Use the same comment format as Problem 1.

---

### Problem 3 — Reflection on Week 6 Solutions

**Goal:** Read the posted Week 6 solutions in [`../week06/week06-solutions.md`](../week06/week06-solutions.md) and write honest, specific answers to the questions below. This is not a summary of what the code does — it is a reflection on what the solutions helped you understand, confirm, or correct in your own pseudocode.

Create a file called `problem3.py`. Write your answers as comments:

```python
# Problem 3 — Reflection on Week 6 Solutions
#
# Q1. Stopping early
#
#     The Week 6 solution to find_char returns as soon as it finds a
#     match, instead of finishing the loop and checking every position.
#     Did your own pseudocode do this? If not, what did it do instead,
#     and does it still produce the correct answer — just with extra
#     unnecessary work?
#
# Q2. The ASCII range test
#
#     The Week 6 solution to to_upper only changes a character when its
#     ASCII code falls between 97 and 122. Explain in your own words why
#     characters that are already uppercase, digits, spaces, and
#     punctuation all safely fall through that test unchanged, using the
#     ASCII grid model.
#
# Q3. The empty-string edge case
#
#     The Week 6 solution to is_word checks for an empty string
#     *before* entering the while loop, with a comment explaining that
#     an empty string would otherwise "sail through" the loop and
#     incorrectly report True. Did your own pseudocode catch this case?
#     Walk through, step by step, what your pseudocode would have done
#     with an empty string as input.
#
# Q4. Connecting to this week
#
#     Problem 1 of this assignment (finding every position of a letter)
#     builds directly on find_char from Week 6. In one or two sentences,
#     describe exactly what you had to add or change to go from "find
#     the first match and stop" to "find every match."
#
# Q5. Your choice
#
#     Pick one problem from the Week 6 assignment where your own
#     solution took a noticeably different approach than the posted
#     solution — or where the posted solution surprised you. Describe
#     the difference and say what you learned from it.
```

A short, honest answer is better than a long vague one. Two or three sentences per question is enough; one clear sentence beats three foggy ones.

---

## How to Submit

Upload your work on **Sakai** under the assignment for **Week 07**.

Submit only your Python files:

```
problem1.py
problem2.py
problem3.py
```

No screenshots, no PDFs, no other file types — Python files only. Confirm with `ls` that each file exists before you upload.

---

## How Your Work Is Evaluated

**Submission credit.** Submitting an assignment earns you 1 point; not submitting earns 0. This is not a score for quality — it simply records that you completed the work on time.

**No late work, no extensions.** We discuss solutions in class immediately after the deadline, and solutions are posted at the same time. Because the answers are public from that moment on, late submissions cannot be accepted and deadlines cannot be extended.

**Self-evaluation.** After solutions are posted, you evaluate your own work. Using the posted solutions and Leo's written instructions as a guide, you decide what you understood, what you got wrong, and what you need to practice to avoid the same mistakes in the future. Making mistakes is how learning happens. Not repeating them is the evidence that it did.
