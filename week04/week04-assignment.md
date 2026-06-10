# COMP 170 — Week 4 Assignment
*Lists and Cumulative Algorithms*

---

## Week 4 at a Glance

Here is a concise summary of what we covered in class this week, followed by reading pointers for each topic. If anything felt unclear in lecture, start here before opening the textbook.

### June 8 -- Boolean Values, Logic, and Modulo

We opened with a classic logic puzzle: "Go buy bread. If they have eggs, get a dozen." A literal reading produces twelve loaves of bread -- the punchline illustrates why conditional logic needs precise scope. We introduced **Boolean** as a data type with exactly two possible values: `True` and `False`. Any unambiguous yes-or-no question produces a Boolean. Questions that depend on opinion do not.

We built truth tables for `and` and `or`. OR is `True` whenever at least one part is true; AND requires both. Python spells these as lowercase keywords: `or` and `and`. We also drew a sharp line between `=` (assignment: stores a value into a variable) and `==` (comparison: tests whether two values are equal). String comparison is case-sensitive and space-sensitive -- `"Leo"` and `"leo"` are not equal.

We then introduced the **modulo operator** (`%`): the remainder after integer division. Dividing any integer by 2 leaves 0 (even) or 1 (odd). A concrete application: alternating gray/white row shading in data tables uses `row_number % 2 == 0` to decide which color to apply.

### June 9 -- The Airplane Seating Problem

We posed a concrete challenge: take a line of passengers numbered 0, 1, 2, ... and assign each one a seat label like "1A" or "3B". Before writing any code, we looked for patterns. Bella observed that seat letters repeat in groups equal to `seats_per_row`; Erica noted the cycle A, B, C, A, B, C ...

Two operators unlocked the problem:

- `passenger % seats_per_row` produces the seat position within the row (0, 1, 2, 0, 1, 2, ...). Adding that number to 65 and calling `chr()` converts it to a letter -- the same ASCII trick from Week 3.
- `passenger // seats_per_row + 1` produces the row number. Integer division discards the remainder and keeps the quotient; `+ 1` converts from zero-based counting to the one-based row numbers passengers expect on a ticket.

Changing `seats_per_row` from 3 to 4 instantly produced a correct layout for a wider plane -- one variable, zero other edits.

### June 10 -- Lists and the Cumulative Algorithm

Omar helped us build the first intuition for a list: imagine being the first employee at a startup airline, walking down the line of passengers, asking each person their name, and writing the names on a piece of paper in order. That piece of paper is a list.

A list is a **contiguous** collection of items stored next to one another in memory, accessible by position. We compared it to an apartment building where every unit is the same size: you reach any resident by counting doors from the entrance. Contrast that with 100 people scattered across Manhattan in separate hotels -- collecting them takes forever. Lists make data easy to find because everything lives together in a predictable layout.

Andrew helped us unpack zero-based indexing at an imaginary grocery checkout. Your position in line equals the number of people in front of you. If no one is ahead of you, you are position 0. `list[0]` is the first element; `list[len(list) - 1]` is the last.

Using Cheska's temperature readings from North Carolina, we compared two implementations of an average. The first hard-coded the denominator -- every new data point required a manual edit, and forgetting that edit produced a silent wrong answer. The second stored temperatures in a list and used `len()` to compute the denominator automatically. The loop added each temperature to a running total; the average was the total divided by however many items the list contained. This pattern -- initialize a sum, loop through the list with `range(len(...))`, divide at the end -- is called a **cumulative algorithm**. It is one of the four or five most important patterns in all of programming.

### Reading for This Week's Topics

| Topic | Where to read |
|-------|---------------|
| Lists -- creating, indexing, `len()` | [*Introducing Python* Ch. 8](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html#c08_h_list_create) |
| `for` loops and `while` loops | [docs.python.org -- for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements) · [*Introducing Python* Ch. 7](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html) |
| `range()` with `len()` | [docs.python.org -- The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function) |

---

## Assigned Reading

Before working through the problems, read the following from **Introducing Python, 3rd Edition** (Bill Lubanovic) on O'Reilly Learning:

- [**Chapter 7 -- Loops**](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch07.html) -- re-read the `for` section now that you are using it to iterate over lists; this time also read the `while` loop section.
- [**Chapter 8 -- Lists**](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch08.html#c08_h_list_create) -- creating lists, accessing elements by index, using `len()`, and looping over lists. This chapter maps directly onto all four problems below.

Access requires an O'Reilly account. You have one -- use your LUC email to log in.

---

## Before You Begin: Working in the Terminal

This assignment is written and run entirely in the terminal using `vim` and `python3`. The workflow is identical to last week. If you need a reminder, the full reference is in [`tools/vim_tutorial.md`](../tools/vim_tutorial.md).

### Your Workflow, Step by Step

For every problem below, repeat this same loop:

```
1. Open (or create) a Python file in vim
2. Write your code
3. Save and quit
4. Run the file with python3
5. Look at the output, decide if it is right
6. If not -- go back to step 1
```

Here is the exact sequence of commands:

```
$ vim problem1.py        <- opens the file (creates it if it does not exist)
```

Inside vim:

```
i                        <- enters Insert mode; you can now type
(write your code here)
Esc                      <- leaves Insert mode; back to Normal mode
:wq                      <- saves the file and quits vim
```

Back in the terminal:

```
$ python3 problem1.py    <- runs your program; output appears below
```

### Navigating to the Right Folder

Your files should live in your `comp170/week04/` folder. Before opening vim, confirm you are in the right place:

```
$ pwd                    <- shows where you are right now
$ cd ~/comp170/week04    <- adjust this path to match your setup
$ ls                     <- confirm you are in the right folder
```

---

## The Problems

---

### Problem 1 -- Reading a List

**Goal:** Build familiarity with list indexing and `len()` before writing any loops.

Create a file called `problem1.py`. Copy this list into your file exactly:

```python
scores = [92, 78, 85, 90, 67, 88]
```

Then add one `print` statement for each line below. **Write your prediction first** (on paper or as a comment), then run the file and check each result.

```python
print(scores[0])
print(scores[1])
print(scores[5])
print(len(scores))
print(scores[len(scores) - 1])
print(scores[0] + scores[1])
```

After running, think through these questions (no written submission required):

1. `scores[5]` and `scores[len(scores) - 1]` produce the same value. Why? Would that still be true if the list had seven items instead of six?
2. The list has 6 items. What happens if you write `print(scores[6])`? Try it and read the error message carefully -- Python error messages tell you exactly what went wrong and on which line.
3. `scores[0] + scores[1]` adds two items from the list. Is the result an integer, or does Python convert it to something else?

---

### Problem 2 -- Sum and Average

**Goal:** Implement the cumulative algorithm from the June 10 class and compute two summary statistics.

Create a file called `problem2.py`.

Use this list of weekly high temperatures (degrees Fahrenheit) from Cheska's location in North Carolina:

```python
temps = [72, 68, 85, 91, 77, 83, 89]
```

Write a program that:

1. Computes the **total** of all temperatures using a `for` loop and `range(len(temps))`.
2. Computes the **average** by dividing the total by the number of items.
3. Prints both results.

Your output should look like this:

```
Total: 565
Average: 80.71428571428571
```

**Loop skeleton to get you started:**

```python
temps = [72, 68, 85, 91, 77, 83, 89]
N = len(temps)
total = 0

for i in range(N):
    total = total + temps[i]

average = total / N
print("Total:", total)
print("Average:", average)
```

Run it, confirm the output matches, then **delete the skeleton and rewrite it yourself from memory**. Rebuilding from scratch -- not copying -- is how this pattern becomes automatic.

**Note:** The loop in [`temperatures.py`](./temperatures.py) from the June 10 class uses this same structure. Compare your solution with that file after you finish.

---

### Problem 3 -- Finding the Maximum

**Goal:** Use a `for` loop and an `if` statement to scan a list and track the largest value seen so far.

Create a file called `problem3.py`.

Use the same temperature list:

```python
temps = [72, 68, 85, 91, 77, 83, 89]
```

Write a loop that finds the highest temperature. Your output should be:

```
Highest temperature: 91
```

**The pattern:**

Keep a running record of the best value seen so far. Before the loop starts, assume the first item is the current maximum. Then, for each item in the list, ask: is this item larger than the current maximum? If yes, update.

```python
max_so_far = temps[0]

for i in range(len(temps)):
    if temps[i] > max_so_far:
        max_so_far = temps[i]

print("Highest temperature:", max_so_far)
```

Once this works, **modify the list** to test two edge cases:

- Move 91 to position 0. Does the loop still find it?
- Replace every value with the same number (e.g., `[80, 80, 80]`). What does the loop return?

---

### Problem 4 -- Counting Above a Threshold *(Challenge)*

**Goal:** Combine the cumulative pattern with an `if` statement to count how many items in a list satisfy a condition.

Create a file called `problem4.py`.

Use this list of exam scores:

```python
scores = [92, 78, 85, 90, 67, 88, 95, 72, 81, 64]
```

Write a program that counts how many scores are **80 or above** and prints the result. Your output should be:

```
Scores at or above 80: 6
```

**The pattern:**

A counting loop works like the sum loop in Problem 2, except instead of adding up values, you add 1 each time a condition is true.

```python
count = 0

for i in range(len(scores)):
    if scores[i] >= 80:
        count = count + 1

print("Scores at or above 80:", count)
```

Once it works, try these variations:

1. Change the threshold to 90. How many scores are at or above 90?
2. Count how many scores are **below** 70. What single change to the `if` condition does that require?
3. *(Optional)* Combine Problem 2 and this problem: compute the average first, then count how many scores exceed the average.

---

### Problem 5 -- Reflection on Week 3

**Goal:** Compare your Week 3 solutions with the posted solutions and explain the choices each version makes.

The posted solutions are in [`../week03/week03_solutions.py`](../week03/week03_solutions.py). Open that file and your own Week 3 `problem1.py` through `problem4.py` side by side. For each question, look at the relevant section of the posted solution before answering.

Create a file called `problem5.py`. Write your answers as comments:

```python
# Reflection -- Week 3 Solutions Review
#
# Q1. Problem 1 -- the * operator and order
#     The posted solution notes that 3 * 'ab' and 'ab' * 3 produce the
#     same result: string repetition is commutative (order does not matter).
#     Is string + also commutative? Write a specific example -- two
#     expressions using + in opposite order -- and state whether they
#     produce the same string or different ones.
#
# Q2. Problem 2 -- range(1, N+1) vs. range(N)
#     The posted solution uses range(1, N+1) so that the loop variable i
#     takes the values 1, 2, 3, 4, 5. Your staircase label on each row is
#     the step number, which matches i directly.
#     Could the loop be rewritten with range(N) instead (i goes 0, 1, 2,
#     3, 4)? Write out what the loop body would need to look like to
#     produce the exact same output.
#
# Q3. Problem 2 vs. Problem 3 -- comma vs. +
#     Problem 2 uses:   print(i, '*' * i)
#     Problem 3 uses:   print(' ' * (N-i) + '*' * i)
#     Both print a line with two parts. Why could Problem 2 use a comma
#     while Problem 3 had to use +? What would the triangle look like if
#     Problem 3 used print(' ' * (N-i), '*' * i) with a comma instead?
#
# Q4. Problem 3 -- tracing the formula
#     The formula is: ' ' * (N-i) + '*' * i  with N = 5.
#     For i = 1: write out the exact string produced and count its length.
#     For i = 5: do the same.
#     Does the total number of characters change from row to row?
#     What does your answer tell you about the shape of the triangle?
#
# Q5. Problem 4 -- rounding vs. truncating
#     The circle uses int(x_max + 0.5) to round to the nearest integer.
#     int(x_max) alone always rounds down (truncates the decimal part).
#     For r = 8 and y = -2: y_scaled = -4, so
#         x_max = sqrt(64 - 16) = sqrt(48) ≈ 6.928
#     Compute int(6.928 + 0.5) and int(6.928) by hand.
#     How many stars does each value produce for that row (formula: 2*x_max+1)?
#     In one sentence, explain what visual difference truncating would cause.
```

A short, honest answer is better than a long vague one. Two or three sentences per question is enough; one clear sentence beats three foggy ones.

---

---

## Quick Reference

### Bash

```
pwd                   where am I?
ls                    what files are here?
cd ~/comp170/week04   go to your week04 folder
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

### Python -- Week 4

```python
temps = [72, 68, 85, 91]      # a list of integers
temps[0]                       # 72   -- first item (index 0)
temps[3]                       # 91   -- fourth item (index 3)
len(temps)                     # 4    -- number of items

N = len(temps)
for i in range(N):             # i goes 0, 1, 2, ..., N-1
    print(temps[i])            # access each item by index

total = 0                      # cumulative sum
for i in range(N):
    total = total + temps[i]
average = total / N

max_so_far = temps[0]          # running maximum
for i in range(N):
    if temps[i] > max_so_far:
        max_so_far = temps[i]

count = 0                      # counting loop
for i in range(N):
    if temps[i] > 80:
        count = count + 1
```

---

## How to Submit

Upload your work on **Sakai** under the assignment for **Week 04**.

Submit only your Python files:

```
problem1.py
problem2.py
problem3.py
problem4.py
problem5.py
```

No screenshots, no PDFs, no other file types -- Python files only. Confirm with `ls` that each file exists before you upload.

---

## How Your Work Is Evaluated

**Submission credit.** Submitting an assignment earns you 1 point; not submitting earns 0. This is not a score for quality -- it simply records that you completed the work on time.

**No late work, no extensions.** We discuss solutions in class immediately after the deadline, and solutions are posted at the same time. Because the answers are public from that moment on, late submissions cannot be accepted and deadlines cannot be extended.

**Self-evaluation.** After solutions are posted, you evaluate your own work. Using the posted solutions and Leo's written instructions as a guide, you decide what you understood, what you got wrong, and what you need to practice to avoid the same mistakes in the future. Making mistakes is how learning happens. Not repeating them is the evidence that it did.
