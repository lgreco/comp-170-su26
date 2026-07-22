# COMP 170 — Week 10 Assignment

## Week at a Glance

Here is a concise summary of what we covered in class this week. If anything felt unclear in lecture, start here.

### July 20 — Async Day

This week started with an asynchronous assignment rather than a lecture: independent practice on a handful of short problems, separate from the graded work below.

### July 21 — What Is a File? ([notes](./2026-07-21-COMP170.md))

We started from scratch: what is a "file," really? Everyday answers — "a place to store things," "information in a specific place," "a file folder" — all pointed at the same idea, that a file is any container of information, no matter its physical form. We noticed that files nest inside other files, the same way pages sit inside folders, inside drawers, inside cabinets, inside rooms — a hierarchy that's also familiar from a family tree. From there we traced how computers came to store files: punched cards, magnetic tape (read only in order, like a cassette), spinning magnetic disks (jump straight to any point, like a vinyl record needle — and prone to a "disk crash" if a spec of dust got under the read head), and finally the electronic storage that replaced spinning disks about 20 years ago. We introduced the three-tier von Neumann memory hierarchy — registers (tiny, extremely fast, inside the processor), main memory (larger, still fast, but wiped when power is lost), and storage (large, slower, permanent) — and closed by distinguishing text files, which we can read directly (like Python code), from binary files, like Word documents, JPEGs, or PNGs, meant for the computer to read.

### July 22 — Creating, Writing, and Reading Files in Python ([notes](./2026-07-22-COMP170.md))

We watched files come to life by splitting the screen: Python on one side, the folder on the other. Opening a file for writing creates it immediately, even before anything is written to it — we saw an empty `demo.txt` appear in the folder the moment we opened it. Writing a line to the file didn't make it show up right away, because what we wrote was sitting in a temporary holding area called a buffer, not yet saved to the file — only closing the file flushed it to storage, where it survived quitting and restarting Python. We compared the two ways to open a file for writing: write mode, which wipes out anything already there and starts fresh (a waiter's fresh notepad page), versus append mode, which keeps what's there and adds new lines to the end (adding more items to an existing order). Read mode lets us look at a file's contents without any risk of changing them. We then wrote a short program ([`SimpleFileOps.py`](./SimpleFileOps.py)) that reads a file one line at a time with `.readline()` until there's nothing left, and noticed that `print()` adds its own line break — so if the line we read already ends in one, we get a blank line in between, fixed with `.rstrip()`. We closed by tying files back to the "four pillars" of computing (strings, loops, if statements, arrays) and traced a short history from old comma-separated student records, where adding one new detail like a middle name could break the whole layout, to labeled formats like XML, JSON, and YAML that describe what each piece of data means.

---

## Suggested Reading

[**Introducing Python, 3rd Ed. — Ch. 20: Files**](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch20.html) (Lubanovic, on O'Reilly Learning) — covers opening, reading, and writing files in more depth than we had time for in class, including modes beyond the ones we used.

[**Computer file**](https://en.wikipedia.org/wiki/Computer_file) (Wikipedia) — background on what a file is at the operating-system level, useful context for the "files are hierarchical" discussion from July 21.

[**Memory & Storage Timeline**](https://www.computerhistory.org/timeline/memory-storage/) (Computer History Museum) — the historical background for the punched-card-to-solid-state story we told in class, if you want the fuller version.

Access to the O'Reilly book requires an account. You have one — use your LUC email to log in.

---

## A Brief Tutorial: Writing and Reading Files

Opening a file takes two things: a filename, and a **mode** describing what you intend to do with it.

```python
f = open("groceries.txt", "w")   # write mode: starts the file fresh
f.write("milk\n")
f.write("eggs\n")
f.close()
```

Three things to notice:
- `open(..., "w")` creates the file if it doesn't exist yet, and **wipes out** anything already in it if it does — every time you open in write mode, you're starting from an empty page.
- `.write()` does not add a line break for you the way `print()` does — if you want each entry on its own line, you have to include `"\n"` yourself.
- Nothing is guaranteed to actually be saved to the file until `.close()` runs. Until then, what you've written is sitting in a buffer — a temporary holding area — not yet on disk.

Appending works the same way, except the mode is `"a"` instead of `"w"`, and it never wipes out what's already there:

```python
f = open("groceries.txt", "a")   # append mode: adds to what's already there
f.write("bread\n")
f.close()
```

Reading a file back, one line at a time, looks like this:

```python
f = open("groceries.txt", "r")   # read mode: look, don't touch
line = f.readline()
while line:
    print(line.rstrip("\n"))
    line = f.readline()
f.close()
```

`.readline()` returns one line at a time, including its trailing `"\n"` — and returns an empty string once there's nothing left to read, which is what ends the `while` loop. Since `print()` adds its own line break, printing a line that still has its own `"\n"` at the end produces a blank line after it; `.rstrip("\n")` trims that trailing newline off before printing.

---

## The Problems

### Problem 1 — Write a Grocery List to a File

**Goal:** Write a program, `groceries.py`, that repeatedly asks the user to enter a grocery item, and writes each item to `groceries.txt`, one per line, stopping when the user types `done` (not case-sensitive).

**Requirements:**
- Open `groceries.txt` in write mode once, before the loop starts, so each run of the program starts the file fresh.
- Every item the user types (other than `done`) gets written as its own line — remember `.write()` doesn't add `"\n"` for you.
- Close the file once the loop ends.
- After the file is closed, reopen it in read mode and print every item back to the screen, one per line, using `.rstrip("\n")` the same way `SimpleFileOps.py` does, so there are no extra blank lines.

**Example run:**

```
$ python3 groceries.py
Enter a grocery item (or 'done' to finish): milk
Enter a grocery item (or 'done' to finish): eggs
Enter a grocery item (or 'done' to finish): bread
Enter a grocery item (or 'done' to finish): done

Your grocery list:
milk
eggs
bread
```

Organize your solution with a `main()` function and an `if __name__ == "__main__":` guard, the same way `atm.py` and `ATM.py` do.

---

### Problem 2 — A Diary That Remembers

**Goal:** Write a program, `diary.py`, that asks the user for one line of text — today's diary entry — and **appends** it to `diary.txt`, so that running the program again and again builds up a growing file instead of overwriting it each time.

**Requirements:**
- Open `diary.txt` in append mode, so previous entries are never lost.
- Write the new entry as its own line.
- Close the file, then reopen it in read mode and print the **entire** file, one line at a time — every entry ever written, not just the newest one — using `.rstrip("\n")` to avoid blank lines.

**Example run**, after having already run the program twice before with the entries `"Started COMP 170 files week"` and `"Buffers are sneaky"`:

```
$ python3 diary.py
What happened today? Finally understand write vs. append
Diary so far:
Started COMP 170 files week
Buffers are sneaky
Finally understand write vs. append
```

Run your program at least twice before submitting, so `diary.txt` actually shows more than one entry — that's the whole point of append mode.

Organize your solution with a `main()` function and an `if __name__ == "__main__":` guard.

---

### Problem 3 — Reflection on Week 9 Solutions

**Goal:** Read the posted Week 9 solutions in [`../week09/week09-solutions.py`](../week09/week09-solutions.py) and write honest, specific answers to the questions below. This is not a summary of what the code does — it is a reflection on what the solutions helped you understand, confirm, or correct in your own approach this week.

Create a file called `problem3.py`. Write your answers as comments:

```python
# Problem 3 — Reflection on Week 9 Solutions
#
# Q1. Why raise instead of return unchanged?
#
#     Week 9's withdraw() raises a ValueError on invalid input instead
#     of printing an error and returning balance unchanged, the way
#     Week 8's version did. Because of that, withdraw() never reaches
#     a point where it "returns, but nothing really happened" -- it
#     either returns a real new balance, or it doesn't return at all.
#     Why does that distinction matter to attempt_withdrawal(), the
#     function that calls it?
#
# Q2. Order of checks, again
#
#     deposit() in week09-solutions.py checks amount > 0, then method,
#     then the amount-shape rule that depends on method, in that exact
#     order. Why would checking the amount-shape rule before checking
#     method be a mistake, even though both checks eventually run?
#
# Q3. The warning that still isn't an error
#
#     The $10,000 warning in deposit() is a plain print(), not a
#     raise, even though every other invalid case in this file raises.
#     Restate, in your own words, why a warning and an error need to
#     be handled differently here.
#
# Q4. Connecting to this week
#
#     attempt_withdrawal() and attempt_deposit() both close over a
#     while loop with a tries counter and a succeeded flag, catching
#     ValueError with try/except and looping back on failure. Your
#     Problem 1 and Problem 2 this week don't raise or retry anything
#     -- they just write and read files. What's one habit from the
#     retry-loop pattern (guard clauses, checking things in a
#     particular order, closing over a single point of failure) that
#     still showed up in how you structured groceries.py or diary.py,
#     even without a try/except in sight?
#
# Q5. Your choice
#
#     Pick one part of the Week 9 solutions -- withdraw(), deposit(),
#     attempt_withdrawal(), or attempt_deposit() -- where revisiting it
#     changed how you thought about your own ATM.py. Describe what
#     changed and why.
```

A short, honest answer is better than a long vague one. Two or three sentences per question is enough; one clear sentence beats three foggy ones.

---

## How to Submit

Upload your work on **Sakai** under the assignment for **Week 10**.

Submit only your Python files:

```
groceries.py
diary.py
problem3.py
```

No screenshots, no PDFs, no other file types — Python files only. Confirm with `ls` that each file exists before you upload.

---

## How Your Work Is Evaluated

**Submission credit.** Submitting an assignment earns you 1 point; not submitting earns 0. This is not a score for quality — it simply records that you completed the work on time.

**No late work, no extensions.** We discuss solutions in class immediately after the deadline, and solutions are posted at the same time. Because the answers are public from that moment on, late submissions cannot be accepted and deadlines cannot be extended.

**Self-evaluation.** After solutions are posted, you evaluate your own work. Using the posted solutions and Leo's written instructions as a guide, you decide what you understood, what you got wrong, and what you need to practice to avoid the same mistakes in the future. Making mistakes is how learning happens. Not repeating them is the evidence that it did.
