# COMP 170 — Week 9 Assignment

## Week at a Glance

Here is a concise summary of what we covered in class this week. If anything felt unclear in lecture, start here.

### July 13 — Nested Loops and Searching Inside a String ([notes](./2026-07-13-COMP170.md))

We dug into nested loops by printing a multiplication table ([`multi.py`](./multi.py)): an outer loop picking a number 1 through 9, and for each one, an inner loop running through 1 through 9 again. We counted how many times a doubly- or triply-nested loop's innermost line prints if each loop runs 10 times ($10^2$ and $10^3$ times), and connected this to real-world examples like scanning rows and columns of a table, or numbering every seat in a theater. We then used two nested loops to search for the letters "as" inside "bananas" ([`banana.py`](./banana.py)): scan left to right for a spot where the current letter matches the first letter we're looking for, then build a running true-or-false answer with logical *and*, checking each subsequent letter against the rest of the target — the moment one letter fails to match, the whole answer becomes `False` and the search moves on.

### July 14 — Why Programs Crash on Bad Input ([notes](./2026-07-14-COMP170.md))

We looked at why `2026 - "1967"` fails the same way `2026 - "hello there"` does: anything typed at `input()` comes in as text, even if it looks like a number, so it has to be converted with `int()` before you can do arithmetic on it — but `int()` itself fails if the text isn't made of plain digits. Rather than let the program crash on the first bad answer, we talked about looping: keep asking the same question until the answer is usable, and raising the bar past "any number will do" with a reasonableness check (a birth year of 900 converts fine but makes someone over a thousand years old). We wrote a small `get_year()` function ([`age.py`](./age.py)) with a loop that wraps the risky conversion in `try`, catches failures with `except ValueError`, and loops back instead of crashing — and previewed applying the same idea to the ATM's withdrawal and deposit rules.

### July 15 — Multi-Branch If Statements, and Retrying Instead of Crashing ([notes](./2026-07-15-COMP170.md))

We came back to the ATM withdrawal problem to see why a multi-branch `if`/`elif`/`else` works better than two separate `if` statements — with two separate `if`s, nothing stops the code from falling through and attempting the withdrawal even after printing an error. We then compared two ways of handling bad input: raising a `ValueError` right away, which stops the program, versus printing a message and giving the person another chance to try again — Leo argued for the second approach when the mistake is an honest one, though some teams deliberately prefer the first when bad input should never have been possible to enter in the first place. Using this second approach, we rewrote the withdrawal program ([`atm.py`](./atm.py)) with a loop that keeps asking for an amount, wrapped in `try`/`except`, catching the same `ValueError` that `withdraw()` raises for an invalid amount and looping back instead of stopping. This week's assignment asks you to write your own version of this pattern for both withdrawals and deposits, this time with a limit on how many tries someone gets before the program gives up gently.

---

## Suggested Reading

[**Errors and Exceptions**](https://docs.python.org/3/tutorial/errors.html) (Python official tutorial) — the same reading assigned in Week 8. This week goes one step further than `raise` alone: your functions still `raise` a `ValueError` on bad input, but now the *calling* code catches it with `try`/`except` and asks again, instead of letting the program crash.

[**Learning Python, 6th Edition — Ch. 34: Exception Basics**](https://learning.oreilly.com/library/view/learning-python-6th/9781098171292/ch34.html#id4405) (Mark Lutz, on O'Reilly Learning) — a deeper pass at `try`/`except`, useful if the retry-loop pattern from class felt rushed.

[**Introducing Python, 3rd Ed. — Ch. 10: Functions**](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html) (Lubanovic, on O'Reilly Learning) — the same chapter assigned in Week 5, worth a second pass now that `ATM.py`'s functions have multiple guard clauses, a `raise`, and a retry loop wrapped around them. The following sections are **optional** — nothing in this week's problems depends on them, so treat them as a preview of topics still to come:

- Functions Are First-Class Citizens
- Function Arguments Are Not a Tuple
- Inner Functions
- Closures
- Anonymous Functions: Lambda
- Generators
- Generator Comprehensions
- Decorators
- Recursion
- Async Functions, Briefly

Access to the O'Reilly book requires an account. You have one — use your LUC email to log in.

---

## A Brief Tutorial: Retrying Instead of Crashing

Week 8 introduced `raise` as a way for a function to say "this input doesn't work" loudly, stopping execution immediately. On its own, that means one bad answer ends the whole program — fine for a script that runs once, but not for something like an ATM, which should keep asking a real person for input until they get it right (or run out of chances).

The fix is to pair `raise` with `try`/`except`, inside a loop that counts attempts:

```python
def ask_positive_number(max_tries=3):
    """Ask for a positive number, retrying on bad input."""
    tries = 0
    while tries < max_tries:
        tries = tries + 1
        try:
            value = float(input("Enter a positive number: "))
            if value <= 0:
                raise ValueError("the number must be greater than 0")
            return value
        except ValueError as error:
            print("That didn't work:", error)
            print("Try again.")
    print("Sorry, you're out of tries.")
    return None
```

Notice the shape of this:
- The `raise` still happens inside the risky code (here, right after checking `value <= 0`) — that part doesn't change from Week 8.
- The **loop** is what's new: it wraps the risky call in `try`/`except` and, if the `except` runs, simply goes around again instead of letting the program crash. `float(input(...))` itself can also raise (a `ValueError`, if the text isn't a number), and the same `except` catches that too — you don't need a separate `try` for each kind of failure.
- `tries` is capped at `max_tries`. Without a cap, someone who keeps entering garbage would be stuck forever, and the function would never *give up gently* — printing an apologetic message and returning, rather than looping forever or crashing.
- The `return` inside the `try` only runs on success, so it also doubles as the loop's exit — there's no separate `break` needed here (though writing one instead, as we did in class with `atm.py`, works just as well).

`atm.py` in this folder now uses exactly this pattern for `withdraw()` — a `succeeded` flag instead of an early `return`, since the loop needs to keep updating `balance` — including the "out of tries" message at the end. Read it before starting the problems below.

---

## The Problems

### Problem 1 — Your Own `ATM.py`: Withdrawals with Limited Retries

**Goal:** Write your own version of the withdrawal program from class, in a new file called `ATM.py` (uppercase, to distinguish it from `atm.py`). Don't just copy `atm.py` — write it in your own words and structure, so it's clear you understand *why* each part is there.

**Rules the program must enforce**, same as `atm.py`:
- `amount` must be a multiple of $20. If it isn't, `raise` a `ValueError` explaining why.
- `amount` cannot be greater than `balance`. If it is, `raise` a `ValueError` explaining why.

**What's different from `atm.py`:** you decide `max_tries` yourself (anything reasonable, e.g. 3–5), and your program must never let a `ValueError` reach the point of crashing — every raised error should be caught, reported, and followed by another chance to enter an amount, up until the limit is reached, at which point the program gives up gently (a message, not a traceback) and moves on.

**Example run:**

```
$ python3 ATM.py
How much would you like to withdraw? 50
Something's wrong: amount must be a multiple of $20
Try again.
How much would you like to withdraw? 300
Something's wrong: withdrawal amount exceeds balance
Try again.
How much would you like to withdraw? 60
Success! New balance: 140
```

Organize your solution with a `main()` function and an `if __name__ == "__main__":` guard, the same way `atm.py` does.

---

### Problem 2 — Cash vs. Cheque Deposits

**Goal:** In the same `ATM.py` file, write a `deposit(amount, balance, method)` function and a retry loop around it, following the same pattern as Problem 1 — but this time the rules depend on *how* the money is being deposited.

**Rules the function must enforce:**
- `amount` must be greater than $0. If it isn't, `raise` a `ValueError` explaining why.
- `method` must be either `"cash"` or `"cheque"`. If it's anything else, `raise` a `ValueError` explaining why.
- If `method` is `"cash"`, `amount` must be a **whole dollar amount** — no coins, no cents. A cash deposit of `42.50` is invalid; you cannot physically hand an ATM a fraction of a dollar in cash the way you can write one on a cheque. If it isn't whole, `raise` a `ValueError` explaining why.
- If `method` is `"cheque"`, `amount` may include cents, but it still must be valid money — at most two decimal digits, same rule as Week 8's `deposit()` (`42.50` is fine, `42.503` is not).
- Carry forward the Week 8 rule: if `amount` is $10,000 or more, print a warning that the deposit will be reported to the IRS — this is a *warning*, not an error, and the deposit still goes through, regardless of `method`.
- If all checks pass, the function returns the updated `balance`.

**Hint:** for the whole-dollar check, think about what `amount == int(amount)` tells you, or reuse the `amount * 100` trick from Week 8 for the two-decimal-digit check.

**Example run:**

```
Deposit method (cash/cheque)? cash
How much would you like to deposit? 42.50
Something's wrong: cash deposits cannot include cents
Try again.
Deposit method (cash/cheque)? cheque
How much would you like to deposit? 42.50
Success! New balance: 182.50
```

Just like Problem 1, wrap the call in a `try`/`except` inside a limited-tries loop (an invalid `method` answer should also count as a failed try and prompt the user to try again), and give up gently once the limit is reached. Call this from the same `main()` as Problem 1, after the withdrawal is done.

---

### Problem 3 — Reflection on Week 8 Solutions

**Goal:** Read the posted Week 8 solutions in [`../week08/week08-solutions.py`](../week08/week08-solutions.py) and write honest, specific answers to the questions below. This is not a summary of what the code does — it is a reflection on what the solutions helped you understand, confirm, or correct in your own approach this week.

Create a file called `problem3.py`. Write your answers as comments:

```python
# Problem 3 — Reflection on Week 8 Solutions
#
# Q1. Printing vs. raising
#
#     Week 8's withdraw() and deposit() report an invalid case by
#     printing an error message and returning the balance unchanged —
#     the file's own note calls this a "teaching shortcut, not a
#     pattern to copy in general." This week's ATM.py instead raises a
#     ValueError, caught by a try/except in a retry loop. Why does the
#     raise-and-catch version fit a program that keeps interacting with
#     a live user better than the print-and-return version?
#
# Q2. Order of checks
#
#     Week 8's withdraw() checks whether amount is a multiple of $20
#     before checking it against balance, because the first check
#     doesn't depend on balance at all. Does that same reasoning still
#     apply now that the checks raise instead of print? Why or why not?
#
# Q3. Where the function stops
#
#     Week 8's withdraw() and deposit() always reach a single return
#     statement, at the very end, even in an invalid case — because an
#     invalid case just leaves new_balance unchanged rather than
#     exiting early. Your Problem 1 and Problem 2 functions raise
#     instead. Does "one return, at the end" still describe what
#     happens on an invalid case in your version? What replaces it?
#
# Q4. A warning that isn't an error
#
#     Week 8's deposit() prints an IRS warning for amounts >= $10,000
#     without raising anything — the deposit still succeeds. Why does
#     that case call for a plain print() instead of a raise, when every
#     other invalid case in this week's assignment calls for a raise?
#
# Q5. Your choice
#
#     Pick one part of the Week 8 solutions -- withdraw(), deposit(),
#     or the reflection questions at the bottom of the file -- where
#     revisiting it changed how you approached this week's ATM.py.
#     Describe what changed and why.
```

A short, honest answer is better than a long vague one. Two or three sentences per question is enough; one clear sentence beats three foggy ones.

---

## How to Submit

Upload your work on **Sakai** under the assignment for **Week 09**.

Submit only your Python files:

```
ATM.py
problem3.py
```

No screenshots, no PDFs, no other file types — Python files only. Confirm with `ls` that each file exists before you upload.

---

## How Your Work Is Evaluated

**Submission credit.** Submitting an assignment earns you 1 point; not submitting earns 0. This is not a score for quality — it simply records that you completed the work on time.

**No late work, no extensions.** We discuss solutions in class immediately after the deadline, and solutions are posted at the same time. Because the answers are public from that moment on, late submissions cannot be accepted and deadlines cannot be extended.

**Self-evaluation.** After solutions are posted, you evaluate your own work. Using the posted solutions and Leo's written instructions as a guide, you decide what you understood, what you got wrong, and what you need to practice to avoid the same mistakes in the future. Making mistakes is how learning happens. Not repeating them is the evidence that it did.
