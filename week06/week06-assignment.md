# COMP 170 — Week 6 Assignment

## Week at a Glance

Here is a concise summary of what we covered in class this week. If anything felt unclear in lecture, start here.

### June 22 — Loop Variables, Accumulators, and Factorials ([notes](./2026-06-22-COMP170.md))

We examined loop variable naming: whether we write `for word in test_strings` or `for broccoli in test_strings`, the code behaves identically — what matters is choosing a name that tells a reader what each item represents. We then built [`cumulative.py`](./cumulative.py), which computes a running total of temperatures using the **accumulator pattern**: initialize a variable to zero *before* the loop, then add each new value to it *inside* the loop, one step at a time. The same pattern applies to multiplication, and we used it to compute factorials in [`fact.py`](./fact.py) — first with a straightforward loop, then with a function that calls itself on a smaller number each time. That self-calling approach is called **recursion**, and we will return to it.

### June 23 — Reinventing `split` from Scratch ([notes](./2026-06-23-COMP170.md))

Our goal was to build our own version of `str.split()` without using it. We imagined a sentence written one character per box on a sheet of squared paper, with the constraint that we could only examine one box at a time and had to write down anything we wanted to remember. Working box by box, we described the process in plain English — *look at the current character; if it is a letter, copy it into the word in progress; if it is a space, save the word and start a fresh one* — and then translated that plain-English description directly into Python. A plain-English, step-by-step description of an algorithm is called **pseudocode**. The resulting method is in [`parse_brute_force.py`](./parse_brute_force.py).

### June 24 — Debugging and the Purpose of Methods ([notes](./2026-06-24-COMP170.md))

We fixed a bug in `our_split`: consecutive spaces caused empty strings to appear in the output. Tracing the logic together, we found that the fix was a single `if len(new_entry) > 0` guard before appending. We then read the `def` line carefully — function name, parameters, type hints, default values — and saw that type hints do not change behavior; they communicate intent. We closed with the bigger picture: a function is one clearly defined step in a larger solution. The skill of breaking a problem into small, independent steps is what programming — and most organized human endeavor — is built on.

---

## Suggested Reading


[**Chapter 10 — Functions**](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html) (*Introducing Python, 3rd Edition*, Bill Lubanovic, on O'Reilly Learning) — focus on: defining a function with `def`, what a parameter is, what `return` does, and how a function's inputs and outputs are described in a docstring. This chapter was first assigned in Week 5; this week it becomes the vocabulary you need to write pseudocode. Each problem below asks you to describe a function — what it receives, what it does step by step, and what it gives back. Those three things are exactly what a function definition specifies.

Access to the O'Reilly chapter requires an account. You have one — use your LUC email to log in.

---

## What Is Pseudocode?

When a programmer sits down to solve a new problem, they rarely start by typing Python. They start by thinking through the *steps* the solution requires, written in plain language, without worrying about syntax.

That plain-language description is called **pseudocode**.

Pseudocode has no fixed rules. It does not need to be valid Python, or valid anything. What it must be is *clear* and *sequential*: a list of steps, each one concrete enough that you could carry it out yourself, with no ambiguity about what comes next.

The most useful mental model for thinking about strings as pseudocode targets is the one we used in class: imagine a page divided by a square grid, where each character of the string occupies exactly one square.

```
Position:  0     1     2     3     4     5     6     7     8     9
           +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
Character: |  c  |  o  |  u  |  n  |  t  |     |  m  |  e  |  !  |     |
           +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
```

Each box has a position number (starting at 0), and you can examine only one box at a time. Anything you need to remember must be written down — in a named variable.

### A Worked Example

**Task:** Count how many spaces appear in a string.

Here is pseudocode for that task:

```
Set a counter to 0.
Set the current position to 0.
While the current position is less than the length of the string:
    Look at the character at the current position.
    If that character is a space:
        Add 1 to the counter.
    Move to the next position (add 1 to the current position).
Report the counter.
```

Notice what makes this pseudocode good:
- It starts by naming every "notepad" variable it will use (`counter`, `current position`).
- Each step is a single, concrete action.
- The condition on the `while` line is precise enough to translate directly into code.
- It never skips over a detail by saying "process the characters somehow."

Your pseudocode for the problems below should have the same qualities.

---

## The Problems

The goal of this assignment is to write pseudocode — plain English descriptions of algorithms — for a set of string tasks. These tasks deliberately mirror things Python's built-in string methods already do. We are reinventing the wheel on purpose: the goal is not the wheel, it is learning to describe a solution one clear step at a time.

**What to submit:** Write your pseudocode as comments inside a Python file. You are welcome to also write Python code alongside it to check your thinking, but it is the plain-English pseudocode that will be read and evaluated.

---

### Problem 1 — Finding a Character

**Goal:** Write pseudocode for a function that finds the position of the **first occurrence** of a single character within a string. If the character is not present, the function reports $-1$. This mirrors the behavior of `str.find()`.

**Example:**

```
String:    "Chicago"
Character: 'i'
Answer:    2
```

Why 2? Because the characters of `"Chicago"` occupy positions $0, 1, 2, \ldots$:

```
Position:  0     1     2     3     4     5     6
           +-----+-----+-----+-----+-----+-----+-----+
Character: |  C  |  h  |  i  |  c  |  a  |  g  |  o  |
           +-----+-----+-----+-----+-----+-----+-----+
```

The character `'i'` first appears at position $2$.

**Write your pseudocode for this function.** Your description should explain:
- What the function needs to know (its inputs).
- How it steps through the string, one box at a time.
- How it recognizes a match.
- What it reports when a match is found.
- What it reports when no match is found.

Create a file called `problem1.py`. Write your pseudocode as comments:

```python
# Problem 1 — Finding a Character
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

### Problem 2 — Converting to Uppercase

**Goal:** Write pseudocode for a function that converts every character in a string to its uppercase equivalent, producing a new string. This mirrors the behavior of `str.upper()`.

**Example:**

```
Input:  "Chicago"
Output: "CHICAGO"
```

**Hint:** The connection between uppercase and lowercase letters lives in their ASCII values. Every letter has a numeric code. The codes for uppercase letters run from $65$ (`'A'`) through $90$ (`'Z'`). The codes for lowercase letters run from $97$ (`'a'`) through $122$ (`'z'`). The gap between any lowercase letter and its uppercase twin is always the same: $97 - 65 = 32$.

This means: to convert a lowercase letter to uppercase, subtract $32$ from its ASCII value. In Python, `ord(c)` gives you the ASCII value of character `c`, and `chr(n)` gives you the character whose ASCII value is $n$. Your pseudocode does not need to use Python syntax — use whatever phrasing makes the steps clear.

**Write your pseudocode for this function.** Your description should explain:
- What the function does with characters that are already uppercase.
- What the function does with characters that are not letters at all (digits, spaces, punctuation).
- How the new string is built up, one character at a time.

Create a file called `problem2.py`. Use the same comment format as Problem 1.

---

### Problem 3 — Is This String a Word?

**Goal:** Write pseudocode for a function that decides whether a string could be a word. A string qualifies as a word if and only if **every** character in it is a letter. This mirrors the behavior of `str.isalpha()`.

**Examples:**

| String | Is it a word? | Reason |
|--------|---------------|--------|
| `"Hello"` | Yes | Every character is a letter |
| `"hELlo"` | Yes | Mixed case is fine — all characters are still letters |
| `"qqwwwee"` | Yes | Meaningless, but still all letters |
| `"HELL0"` | **No** | The last character is the digit zero, not the letter oh |
| `"good bye"` | **No** | The space in the middle is not a letter |
| `""` | **No** | An empty string has no characters at all, so it has no letters |

**Write your pseudocode for this function.** Your description should explain:
- How the function decides whether a single character is a letter (think about ASCII ranges).
- What the function does as soon as it finds a non-letter character.
- How the function handles an empty string.

Create a file called `problem3.py`. Use the same comment format as Problems 1 and 2.

---

### Problem 4 — Reflection on Week 5 Solutions

**Goal:** Read the posted Week 5 solutions in [`../week05/week05-solutions.py`](../week05/week05-solutions.py) and write honest, specific answers to the questions below. This is not a summary of what the code does — it is a reflection on what the solutions helped you understand, confirm, or correct.

Create a file called `problem4.py`. Write your answers as comments:

```python
# Problem 4 — Reflection on Week 5 Solutions
#
# Q1. find() vs. index() — failure behavior
#
#     The Week 5 solutions show that .find() returns -1 when the target is
#     not in the string, while .index() raises a ValueError and halts.
#     Describe a situation where you would deliberately choose .find() over
#     .index(). Then describe a situation where .index() might actually be
#     the better choice.
#
# Q2. Case sensitivity
#
#     In Problem 2 of the Week 5 solutions, sentence2.count("the") returns 1
#     even though the sentence begins with "The". Explain why in one sentence.
#     Then explain how you would count both "the" and "The" in a single call
#     to .count() — or why you cannot, and what you would do instead.
#
# Q3. .isalpha() and spaces
#
#     The Week 5 solutions show that "hello world".isalpha() returns False.
#     Now look at Problem 3 of this week's assignment — the "is it a word?"
#     problem. In one sentence, explain why a space disqualifies a string
#     from being a word, using the ASCII grid model.
#
# Q4. Method chaining
#
#     In Problem 4, Task 3 of the Week 5 solutions, the line reads:
#         cleaned = raw.strip().expandtabs()
#     Two methods are called on the same line. Describe in plain English what
#     this line does, step by step, as if you were explaining it to someone
#     who has never seen method chaining before.
#
# Q5. Your choice
#
#     Pick one problem or task from the Week 5 assignment where your own
#     solution took a noticeably different approach than the posted solution —
#     or where the posted solution surprised you. Describe the difference and
#     say what you learned from it.
```

A short, honest answer is better than a long vague one. Two or three sentences per question is enough; one clear sentence beats three foggy ones.

---

## How to Submit

Upload your work on **Sakai** under the assignment for **Week 06**.

Submit only your Python files:

```
problem1.py
problem2.py
problem3.py
problem4.py
```

No screenshots, no PDFs, no other file types — Python files only. Confirm with `ls` that each file exists before you upload.

---

## How Your Work Is Evaluated

**Submission credit.** Submitting an assignment earns you 1 point; not submitting earns 0. This is not a score for quality — it simply records that you completed the work on time.

**No late work, no extensions.** We discuss solutions in class immediately after the deadline, and solutions are posted at the same time. Because the answers are public from that moment on, late submissions cannot be accepted and deadlines cannot be extended.

**Self-evaluation.** After solutions are posted, you evaluate your own work. Using the posted solutions and Leo's written instructions as a guide, you decide what you understood, what you got wrong, and what you need to practice to avoid the same mistakes in the future. Making mistakes is how learning happens. Not repeating them is the evidence that it did.
