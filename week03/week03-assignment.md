# COMP 170 — Week 3 Assignment
*String Repetition and Loops*

---

## Assigned Reading

Before working through the problems, read the following from **Introducing Python, 3rd Edition** (Bill Lubanovic) on O'Reilly Learning:

- [**Chapter 1 — Introduction**](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/) — what Python is, how the interpreter works, and how to run your first program.
- **Chapter 2 — Types and Variables** — Python's data types, how variables work, and how values are stored and named.
- **Chapter 3 — Numbers** — integers, floats, and arithmetic. Short but worth reading carefully before moving to strings.
- **Chapter 4 — Strings** — everything about text in Python: creating strings, concatenation, the `*` repetition operator, indexing, and slicing. This chapter maps directly onto Problems 1 through 3 below.
- **Chapter 7 — For and While, first half (the `for` section only)** — read up to and including the `for` loop material; stop when the `while` loop section begins. This connects directly to Problems 2 and 3.

Access requires an O'Reilly account. You have one! Use your LUC email to login.

---


## Before You Begin: Working in the Terminal

This assignment is written and run entirely in the terminal using `vim` and `python3`. If this is one of your first times doing that, expect it to feel awkward — that is completely normal. The tools are powerful but unfamiliar, and the friction you feel right now is temporary. Every professional programmer went through the same thing.

The full reference for `vim` is in [`tools/vim_tutorial.md`](../tools/vim_tutorial.md) in the course repository. Read it before you start if you haven't already. This section gives you everything you need for this assignment specifically.

---

### Your Workflow, Step by Step

For every problem below, you will repeat this same loop:

```
1. Open (or create) a Python file in vim
2. Write your code
3. Save and quit
4. Run the file with python3
5. Look at the output, decide if it's right
6. If not — go back to step 1
```

Here is the exact sequence of commands:

```
$ vim problem1.py        ← opens the file (creates it if it doesn't exist)
```

Inside vim:

```
i                        ← enters Insert mode; you can now type
(write your code here)
Esc                      ← leaves Insert mode; back to Normal mode
:wq                      ← saves the file and quits vim
```

Back in the terminal:

```
$ python3 problem1.py    ← runs your program; output appears below
```

That is the complete cycle. Nothing else is required.

---

### Navigating to the Right Folder

Your files should live in your `comp170/week03/` folder (or wherever you keep course work). Before opening vim, make sure you are in the right place:

```
$ pwd                    ← shows where you are right now
$ cd ~/comp170/week03    ← adjust this path to match your setup
$ ls                     ← confirm you are in the right folder
```

If you are already in the right folder from a previous session, just confirm with `pwd` and continue.

---

### When Things Go Wrong in Vim

**"I pressed some keys and now the screen looks strange."**
Press `Esc` several times — this always returns you to Normal mode. Then press `u` to undo recent changes. When in doubt, `Esc` is your reset button.

**"I can't quit."**
Press `Esc` to make sure you are in Normal mode, then type `:q!` and press Enter. The `!` forces quit without saving. You will lose unsaved work, but you can start fresh.

**"I saved but I'm not sure the file is there."**
Back in the terminal, run `ls`. Your file should appear in the list. If it doesn't, you may have saved under a different name — check with `ls -l`.

**"I get an error when I run python3."**
Read the error message carefully. Python error messages tell you exactly what went wrong and on which line. Common causes: a missing closing quote, mismatched parentheses, or wrong indentation. Open the file in vim again and fix it.

---

## The Problems

---

### Problem 1 — Predicting String Repetition

**Goal:** Build confidence with the `*` operator on strings before using it inside a loop.

**Reading:** [An Informal Introduction to Python — Text](https://docs.python.org/3/tutorial/introduction.html#text) covers string concatenation with `+` and repetition with `*`, along with indexing and slicing. Read through the string examples before starting this problem.

Create a file called `problem1.py`. For each line below, **write down your prediction first** (on paper, or in a comment), then add it to the file and run it to check.

```python
print('*' * 1)
print('*' * 5)
print('*' * 0)
print('-' * 20)
print('ha' * 4)
print('Na' * 8 + ' Batman!')
print(3 * 'ab')
print('=' * 10 + ' SCORE ' + '=' * 10)
```

After running, answer these questions for yourself (you do not need to submit written answers — just think through them):

1. What does `'*' * 0` produce? Does the result make sense?
2. The last line uses `*` twice and `+` twice. In what order does Python evaluate these? Does the order matter here?
3. `3 * 'ab'` and `'ab' * 3` both work. Is there any case where the order would matter?

---

### Problem 2 — Drawing a Staircase

**Goal:** Use a `for` loop to draw a shape, building on the triangle from class.

**Reading:** [More Control Flow Tools — for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements) explains how Python's `for` loop works. Then read the very next section, [The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function), which covers exactly the `range(1, N+1)` pattern used in this problem.

Create a file called `problem2.py`.

In class we drew a triangle that grows from the top:

```
*
**
***
****
*****
```

Your task is to draw a **staircase** that uses two characters per step — the row number printed as a label, plus the stars. The output for `N = 5` should look like this:

```
1 *
2 **
3 ***
4 ****
5 *****
```

Each line prints the step number, a space, then the stars.

**Start with pseudocode.** Before writing any Python, write out the steps in plain English as a comment at the top of your file:

```python
# Pseudocode:
# choose how many steps N
# for each number i from 1 to N:
#     print i, then a space, then '*' repeated i times
```

Then translate that pseudocode into Python below it.

**Hints:**
- `range(1, N+1)` gives you the numbers 1, 2, 3, … N
- `print(i, '*' * i)` will print the number and the stars on the same line, but it puts a space between them automatically — that is fine
- Test with `N = 5` first, then try `N = 10`

---

### Problem 3 — Right-Aligned Triangle

**Goal:** Use spaces and stars together inside a loop to control the position of output.

Create a file called `problem3.py`.

So far the left edge of our shapes has been flush with the left margin. Now you will push the shape to the right. For `N = 5`, the output should look like this:

```
    *
   **
  ***
 ****
*****
```

The bottom row has no leading spaces. Each row above it has one more leading space than the row below it.

Look at the pattern row by row:

| Row `i` | Leading spaces | Stars |
|---------|---------------|-------|
| 1       | 4             | 1     |
| 2       | 3             | 2     |
| 3       | 2             | 3     |
| 4       | 1             | 4     |
| 5       | 0             | 5     |

Notice: when `N = 5` and the row is `i`, the number of leading spaces is `N - i`.

**Your task:**

Write a loop that produces the right-aligned triangle for `N = 5`. Each iteration should print `' ' * (N - i)` followed immediately by `'*' * i` on the same line.

**Hint:** `print(' ' * (N - i) + '*' * i)` prints them joined with no gap between them — the `+` concatenates the two strings before printing.

Once it works for `N = 5`, change `N` to `8` and make sure the shape still looks correct.

---

### Problem 4 — A Filled Circle *(Challenge)*

**Goal:** Use a loop, string repetition, and a little geometry to draw a filled circle. This problem is harder than the previous three — expect to think carefully and experiment.

The target output looks like this (for a radius of 8):

```
     *******
  *************
 ***************
*****************
*****************
*****************
 ***************
  *************
     *******
```

#### The Math

A circle centered at the origin satisfies the equation:

```
x² + y² = r²
```

Any point where `x² + y² ≤ r²` is *inside* the circle. To draw a filled circle, you scan row by row (each row is one value of `y`). For a given `y`, the rightmost `x` that still falls inside the circle is:

```
x_max = sqrt(r² - y²)
```

Each row then prints `2 * x_max + 1` stars (from `-x_max` to `+x_max`), centered with leading spaces.

#### Discretization

The terminal is a grid of characters — you can only place a character at an integer position, not at `x = 3.7`. So you round `x_max` to the nearest integer with `int(x_max + 0.5)`. This is called **discretization**: mapping a continuous shape onto a discrete grid. The result is an approximation; the edges will look slightly stepped rather than smooth.

#### Aspect Ratio

Terminal characters are roughly **twice as tall as they are wide**. If you loop `y` from `-r` to `r` (that's `2r + 1` rows) and each row is `2r + 1` characters wide, the shape will look like a tall oval, not a circle.

To compensate, loop `y` over a compressed range — from `-r//2` to `r//2` — and then scale each `y` back up by 2 before applying the formula. This halves the number of rows while keeping the width the same, making the character grid approximately square.

#### A New Tool: `import math`

Python's `math` module provides `math.sqrt()` for square roots. To use it, add this line at the very top of your file:

```python
import math
```

Then call it like this:

```python
x_max = int(math.sqrt(r*r - y_scaled*y_scaled) + 0.5)
```

#### Putting It Together

```python
import math

r = 8

for y in range(-r//2, r//2 + 1):
    y_scaled = y * 2                              # undo vertical compression
    x_max = int(math.sqrt(r*r - y_scaled*y_scaled) + 0.5)
    print(' ' * (r - x_max) + '*' * (2 * x_max + 1))
```

Try running this as-is first, then experiment: change `r`, replace `'*'` with another character, or adjust the aspect ratio factor to see what changes.

---

## Further Reading

All links used in this assignment, collected in one place:

| Topic | Link |
|-------|------|
| Textbook Ch. 1–4, Ch. 7 (for) — *Introducing Python, 3rd Ed.* | [O'Reilly Learning](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/) |
| Strings — `+`, `*`, indexing, slicing | [docs.python.org — Text](https://docs.python.org/3/tutorial/introduction.html#text) |
| `for` loop syntax | [docs.python.org — for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements) |
| `range()` function | [docs.python.org — The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function) |
| Bash command cheat sheet | [devhints.io/bash](https://devhints.io/bash) |
| Vim cheat sheet | [vim.rtorr.com](https://vim.rtorr.com) |
| Vim reference (course repo) | [`tools/vim_tutorial.md`](../tools/vim_tutorial.md) |

---

## Submitting Your Work

When you are done, you should have four files in your `week03/` folder:

```
problem1.py
problem2.py
problem3.py
problem4.py
```

Confirm with `ls` before you submit. If a file is missing, you have not saved it yet — open it in vim and use `:wq`.

---

## Quick Reference

### Bash

```
pwd                   where am I?
ls                    what files are here?
cd ~/comp170/week03   go to your week03 folder
python3 file.py       run a Python script
vim file.py           open a file for editing
```

### Vim (the essentials)

```
vim file.py    open or create a file
i              enter Insert mode (start typing)
Esc            return to Normal mode (stop typing)
:w             save
:q             quit
:wq            save and quit
:q!            quit WITHOUT saving (discard changes)
u              undo last change (in Normal mode)
```

### Python — Week 3

```python
'*' * 5              # '*****'   — repeat a string
'ha' * 3             # 'hahaha'  — works with any string
' ' * 4 + '*' * 2    # '    **'  — concatenate two repeated strings

for i in range(1, N+1):   # loop from 1 to N inclusive
    print('*' * i)         # use i inside the loop
```
