# COMP 170 — Week 8 Assignment

## Week at a Glance

Here is a concise summary of what we covered in class this week. If anything felt unclear in lecture, start here.

### July 6 — Complex Numbers and Designing `solve_quadratic()` ([notes](./2026-07-06-COMP170.md))

We picked back up the quadratic equation $ax^2 + bx + c = 0$ and its discriminant $\delta = b^2 - 4ac$, and talked about what happens when $\delta$ is negative: the equation still has solutions, just not real ones. We introduced the imaginary unit $i$ (defined so that $i^2 = -1$) and complex numbers $z = x + yi$, then compared tuples to lists — tuples use parentheses and order matters, which makes them the right container for an ordered pair of solutions. We worked out, case by case, every special situation `solve_quadratic()` needs to handle before it computes anything: $a = 0$, $a = 0$ and $b = 0$, and $a \ne 0$ with a negative discriminant.

### July 7 — The Flow Chart, and Three Levels of Testing ([notes](./2026-07-07-COMP170.md))

We turned the case-by-case design from July 6 into a flow chart and matching pseudocode, then looked at `solve_quadratic()` in [`mathemagics.py`](./mathemagics.py), where a complex root is represented as a 2-element tuple `(real_part, imaginary_part)`. We then compared three ways of testing the same eleven cases against that function: naive `if`/`else` printing (`test_math_naive.py`), plain helper functions (`test_math_plain.py`), and Python's `unittest` framework (`test-math.py`, shown for reference — not something you're expected to write yet). Each level removes a little more repeated, error-prone bookkeeping from the last. To show that `mathemagics.py` is a real, installable module and not just a classroom file, we also demonstrated testing it after installing it from PyPI: [`mathemagics`](https://pypi.org/project/mathemagics/).

---

## Suggested Reading

[**Errors and Exceptions**](https://docs.python.org/3/tutorial/errors.html) (Python official tutorial). This week's Problem 1 asks you to `raise` an error yourself for the first time. We've talked all course about `.index()` crashing versus `.find()` returning $-1$, and about "designing for errors" — this page gives you the syntax (`raise ValueError("message")`) behind that design choice.

[**Learning Python, 6th Edition — Ch. 34: Exception Basics**](https://learning.oreilly.com/library/view/learning-python-6th/9781098171292/ch34.html#id4405) (Mark Lutz, on O'Reilly Learning). A second, deeper pass at the same topic as the docs.python.org reading above — covers `raise`, `try`/`except`, and Python's built-in exception types in more detail.

Access to the O'Reilly book requires an account. You have one — use your LUC email to log in.

[**`mathemagics` on PyPI**](https://pypi.org/project/mathemagics/) — the published package containing `solve_quadratic()`, used in class on July 7 to demonstrate testing a real, `pip install`-able module rather than just a local `.py` file.

---

## A Brief Tutorial: Raising Errors

All course long we've seen functions report "this input doesn't work" in a *quiet* way — `.find()` returns $-1$, `solve_quadratic()` returns `(NaN, NaN)`. That works when the caller is expected to check the result before trusting it. But sometimes an input is so wrong that there is no sensible value to return at all — an amount that isn't a multiple of $20 isn't "sort of" a valid withdrawal, it's simply not one. Python's `raise` statement lets a function say that loudly, the same way `.index()` does when a character isn't found.

**The basic form:**

```python
raise ValueError("a message describing what went wrong")
```

`ValueError` is a built-in Python exception meaning "the value passed in wasn't acceptable." `raise` immediately stops the function — no code after it in that function runs — and hands control back up to whoever called it, along with the message.

**A small example**, a function that only accepts positive numbers:

```python
def square_root(x):
    if x < 0:
        raise ValueError("cannot take the square root of a negative number")
    return x ** 0.5
```

```python
>>> square_root(9)
3.0
>>> square_root(-4)
ValueError: cannot take the square root of a negative number
```

Calling `square_root(-4)` doesn't return a value at all — it crashes with a traceback showing your message, exactly like `"Chicago".index("z")` crashes with its own message. If you don't want the crash and instead want to handle the problem yourself, wrap the call in `try`/`except`:

```python
try:
    result = square_root(-4)
    print("Got:", result)
except ValueError as error:
    print("That didn't work:", error)
```

```
That didn't work: cannot take the square root of a negative number
```

**Two things worth noticing:**
- A function can `raise` more than one kind of error for more than one reason — check the conditions in whatever order makes sense, and `raise` as soon as you find one that fails. (This is why order matters in Problems 1 and 2 below: check whether `amount` is a valid number on its own *before* checking it against anything else, like `balance` or the $10,000 threshold.)
- Once a function raises, it's done — there's no "raise, then keep going." If you need to guarantee some cleanup always happens, that's a topic for another day; for this assignment, a `raise` is always the last thing your function does in that branch.

---

## The Problems

### Problem 1 — Bank Withdrawal

**Goal:** Write a function `withdraw(amount, balance)` that simulates withdrawing cash from an ATM.

**Rules the function must enforce:**
- `amount` must be a multiple of $20 (real ATMs only dispense twenty-dollar bills). If it isn't, `raise` a `ValueError` explaining why.
- `amount` cannot be greater than `balance` — you can't withdraw money that isn't there. If it is, `raise` a `ValueError` explaining why.
- If both checks pass, the function returns the updated `balance` after the withdrawal is deducted.

**Example:**

```python
>>> withdraw(60, 200)
140
>>> withdraw(50, 200)
ValueError: amount must be a multiple of $20
>>> withdraw(300, 200)
ValueError: withdrawal amount exceeds balance
```

Notice the order of the checks: a bad `amount` should be rejected *before* you even ask whether there's enough balance to cover it — an amount that isn't a multiple of $20 is invalid no matter what the balance is.

**Write your Python function directly, narrated with comments** in a file called `problem1.py`. Rather than writing separate pseudocode first, explain each step of your function *in place*, right above (or beside) the line of code it describes:

```python
# Problem 1 — Bank Withdrawal

def withdraw(amount, balance):
    # ... explain what this check is for, and what makes amount invalid here ...
    ...
    # ... explain what this check is for, and how it relates to balance ...
    ...
    # ... explain what happens once both checks pass ...
    ...
```

It's fine — encouraged, even — if your comments read like the pseudocode you sketched out before writing the code. The point is that a reader should be able to follow *why* each line exists just from your comments, without having to run the function to figure out what it does.

Your comments should explain:
- What the function needs to know (its inputs) and what it reports (its output).
- What condition makes `amount` invalid on its own, independent of `balance`.
- What condition makes `amount` invalid *relative to* `balance`.
- Why checking the multiple-of-$20 rule first, before comparing to `balance`, makes sense.
- What the function returns when both checks pass.

---

### Problem 2 — Bank Deposit

**Goal:** Write a function `deposit(amount, balance)` that simulates depositing cash into an account.

**Rules the function must enforce:**
- `amount` must be greater than $0 — you can't deposit nothing, or a negative amount. If it isn't, `raise` a `ValueError` explaining why.
- `amount` must be valid money — dollars and cents only, so at most two decimal digits (e.g. `42.50` is fine, `42.5` is fine, `42.503` is not, since there's no such thing as a third of a cent). If it isn't, `raise` a `ValueError` explaining why.
- If `amount` is **$10,000 or more**, print a warning that the deposit will trigger an IRS notice. This is a *warning*, not an error — the deposit still goes through.
- If all checks pass, the function returns the updated `balance` after the deposit is added.

**Example:**

```python
>>> deposit(150, 200)
350
>>> deposit(12000, 200)
Warning: deposits of $10,000 or more are reported to the IRS
12200
>>> deposit(-50, 200)
ValueError: deposit amount must be greater than $0
>>> deposit(42.503, 200)
ValueError: deposit amount must be valid dollars and cents
```

Narrate this function with comments the same way you did in Problem 1 — no separate pseudocode, just comments in place that explain each check as you write it. Create a file called `problem2.py`.

**Hint for checking dollars and cents:** think about what happens when you multiply an amount by $100$ — `42.50 * 100` gives you a whole number of cents, `42.503 * 100` doesn't. `round()` and the modulo operator `%` are both useful here.

---

### Problem 3 — Testing `withdraw()` and `deposit()`

**Goal:** Using the naive or plain testing style from July 7's notes (your choice — naive `if`/`else` printing, or plain helper functions like `close_enough`/`check_close`), write test cases for both functions from Problems 1 and 2. Since both functions can `raise` an error, testing them is a little different from testing `solve_quadratic()`: to check that a `ValueError` is raised (rather than a return value), wrap the call in a `try`/`except`:

```python
try:
    withdraw(50, 200)
    print("FAIL: expected a ValueError for amount=50, but none was raised")
except ValueError as error:
    print("PASS: correctly rejected amount=50 —", error)
```

For `withdraw()`, write at least **five** test cases covering:
1. A normal, valid withdrawal.
2. A withdrawal that exactly empties the balance (`amount == balance`).
3. An `amount` that is not a multiple of $20.
4. An `amount` greater than `balance`.
5. One edge case of your own choosing — think about what could still go wrong that the first four cases don't cover.

For `deposit()`, write at least **three** test cases — simpler testing than `withdraw()`, since you're just getting a feel for this function — covering:
1. A normal, valid deposit.
2. An `amount` that is not valid dollars and cents, or is $\le 0$.
3. An `amount` of $10,000 or more (check that the warning prints *and* the deposit still succeeds).

Create a file called `problem3.py` with your test cases for both functions. Briefly note, as a comment above each case, which situation it exercises.

---

### Problem 4 — Reflection on Week 7 Solutions

**Goal:** Read the posted Week 7 solutions in [`../week07/week07-solutions.md`](../week07/week07-solutions.md) and write honest, specific answers to the questions below. This is not a summary of what the code does — it is a reflection on what the solutions helped you understand, confirm, or correct in your own pseudocode.

Create a file called `problem4.py`. Write your answers as comments:

```python
# Problem 4 — Reflection on Week 7 Solutions
#
# Q1. Not stopping early
#
#     positions() keeps scanning all the way to the end of the string
#     even after it finds a match, because it needs every position, not
#     just the first. Did your own pseudocode for Problem 1 (Week 7) do
#     this? If not, what did it do instead?
#
# Q2. The match flag in find_substring
#
#     find_substring() uses an inner while loop with a match flag that
#     flips to False the instant one character fails to compare, so the
#     rest of target is never checked at that starting position. Explain
#     in your own words why this saves work compared to always checking
#     every character of target before deciding.
#
# Q3. One return, at the end
#
#     find_substring() never returns from the middle of the function —
#     it records the answer in result, flips found to True, and lets
#     the outer loop's own condition stop the search. Did your own
#     pseudocode return as soon as a match was found instead? Does it
#     still produce the correct answer?
#
# Q4. Connecting to this week
#
#     find_substring() reports "not found" with a sentinel value (-1),
#     the same convention as .find(). withdraw() and deposit() in this
#     week's Problems 1 and 2 report an invalid case differently -- by
#     raising a ValueError instead of returning a sentinel. Why does
#     raising an error make more sense than returning something like -1
#     for a failed withdrawal or deposit, but a sentinel value made
#     sense for "substring not found"?
#
# Q5. Your choice
#
#     Pick one part of the Week 7 solutions -- positions() or
#     find_substring() -- where your own approach took a noticeably
#     different path than the posted solution, or where the posted
#     solution surprised you. Describe the difference and say what you
#     learned from it.
```

A short, honest answer is better than a long vague one. Two or three sentences per question is enough; one clear sentence beats three foggy ones.

---

## How to Submit

Upload your work on **Sakai** under the assignment for **Week 08**.

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
