# COMP 170 — Week 5 Assignment

## Week at a Glance

Here is a concise summary of what we covered in class this week, followed by reading pointers for each topic. If anything felt unclear in lecture, start here before opening the textbook.

### June 15 -- Splitting Sentences into Words ([notes](./2026-06-15-COMP170.md))

We set out to write a program that takes a sentence — `"The relentless summer heat in Chicago made even the sidewalks shimmer"` — and produces a list of every word longer than a given number of characters, converted to uppercase. The key tool was `.split()`: because a string is an object with built-in behavior, `sentence.split()` breaks it into a list of words wherever it finds a space. With the word list in hand, we looped with `range(len(words))`, checked each word's length, and used `.upper()` to convert qualifying words.

### June 16 -- Loops, Lists, and Strings Together ([notes](./2026-06-16-COMP170.md))

We compared two ways to loop over the same list: the **plain for-loop**, which counts through index positions (`for i in range(len(words))`, then `words[i]`), and the **enhanced for-loop**, which hands you each item directly (`for word in words`) with no index at all. [`play_with_words.py`](./play_with_words.py) and [`fun_with_words.py`](./fun_with_words.py) are the same program written both ways — compare them side by side. We also covered why a string behaves like a list of characters under the hood, which is why `len()` works on both.

### June 17 -- Packaging Code into a Function ([notes](./2026-06-17-COMP170.md))

Instead of leaving the word-checking code loose, we wrapped it in a function called `filter_words` (see [`managing_complexity.py`](./managing_complexity.py)), which takes a sentence and a cutoff length and returns the matching words in capital letters. We added **type hints** (`sentence: str`, `-> list[str]`) and a **docstring** explaining what the function expects and returns. We added **input validation** — checking the sentence isn't empty and the cutoff length is reasonable — combining three conditions with a single `and`. Finally, we saw two different ways to actually run the function: directly in the same file with an `if __name__ == "__main__":` block, or from a separate file using `import`.

### Reading for This Week's Topics

| Topic | Where to read |
|-------|---------------|
| Defining functions, parameters, `return`, docstrings | [*Introducing Python* Ch. 10](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html) |
| `def` syntax, default values, the call mechanics | [docs.python.org -- Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) |

---

## Two Ways to Run a Function: `if __name__ == "__main__":` vs. `import`

This week's example introduced two different ways to actually *run* a function once it's defined. Both appear in this week's files, and the assignment asks you to use both, so it's worth being precise about what each one does and when to reach for it.

**Defining a function only creates it — it does not run it.** Writing `def filter_words(...):` tells Python "here is a recipe," but no code inside the function executes until something *calls* it with `filter_words(...)`.

### Option 1 — `if __name__ == "__main__":` in the same file

Open [`managing_complexity.py`](./managing_complexity.py). The function `filter_words` is defined at the top, and at the bottom of the *same file* there's a block:

```python
if __name__ == "__main__":
    outcome = filter_words("it was the best of times it was the worst of times", 3)
    print(outcome)
```

`__name__` is a special variable Python sets automatically for every file. When you run a file directly — `python3 managing_complexity.py` — Python sets `__name__` to `"__main__"` for *that* file, so the condition is `True` and the demo code runs. This is a convenient way to test a function in the same file where you wrote it, without needing a second file.

### Option 2 — `from xyz import zyx` in a separate file

Open [`that_other_program.py`](./that_other_program.py). It contains no function definition at all — instead, its first line is:

```python
from managing_complexity import filter_words
```

This tells Python: "go open `managing_complexity.py`, and bring the `filter_words` function into this file so I can call it here." 



### Why both exist

| | `if __name__ == "__main__":` | `from xyz import zyx` |
|---|---|---|
| Where the demo code lives | Same file as the function | A separate file |
| When the demo runs | Only when you run that file directly | Never automatically — you write new calls yourself |
| Typical use | Quick self-test while you're writing the function | Reusing a finished function in a different program |

A well-built function file can do both at once: it defines a function for others to `import`, *and* includes a small `if __name__ == "__main__":` self-test, without the two interfering with each other. That's exactly the shape `managing_complexity.py` has, and the shape your own files should have this week.

---

## Assigned Reading

Before working through the problems, read the following:

- [**Chapter 10 -- Functions**](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/ch10.html) (*Introducing Python, 3rd Edition*, Bill Lubanovic, on O'Reilly Learning) -- focus on: defining a function with `def`, parameters vs. arguments, `return`, default parameter values, and docstrings. The chapter goes much further (closures, decorators, generators, recursion) — none of that is required this week, but it's good to know it's there for later.
- [**docs.python.org -- Defining Functions**](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) -- the official tutorial's walkthrough of `def`, default argument values, and docstrings. Shorter and more terse than the textbook; use it as a quick-reference companion.
- [**docs.python.org -- String Methods**](https://docs.python.org/3/library/stdtypes.html#string-methods) -- the full reference list of built-in string methods. Problems 1 through 4 below each ask you to use a handful of specific methods from this page. No one is expected to memorize this list; the point is knowing it exists and being comfortable looking something up in it mid-problem.

Access to the O'Reilly chapter requires an account. You have one — use your LUC email to log in.

---

## Before You Begin: Working in the Terminal

This assignment is written and run entirely in the terminal using `vim` and `python3`. The workflow is identical to previous weeks. If you need a reminder, the full reference is in [`tools/vim_tutorial.md`](../tools/vim_tutorial.md).

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

Your files should live in your `comp170/week05/` folder. Before opening vim, confirm you are in the right place:

```
$ pwd                    <- shows where you are right now
$ cd ~/comp170/week05    <- adjust this path to match your setup
$ ls                     <- confirm you are in the right folder
```

---

## The Problems

Before starting, read [**docs.python.org -- String Methods**](https://docs.python.org/3/library/stdtypes.html#string-methods). It lists every built-in method a string has. Problems 1 through 4 each focus on a handful of those methods — what they do, why they exist, and a few concrete tasks to try with them.

---

### Problem 1 -- Searching a String

**Goal:** Understand the four search methods — `find()`, `index()`, `rfind()`, `rindex()` — and the two design questions that separate them: *do you search from the left or the right?* and *what happens when the search fails?*

Create a file called `problem1.py`. Use this sentence for all five tasks:

```python
sentence = "the quick brown fox jumps over the lazy dog the fox ran"
```

1. Use `.find()` to locate the **first** occurrence of `"fox"`. Print the index.
2. Use `.rfind()` to locate the **last** occurrence of `"fox"`. Print the index, and compare it to the result of task 1 — are they the same number or different? Write one sentence explaining why.
3. Use `.find()` to search for a word that is **not** in the sentence, such as `"elephant"`. Print the result — notice that it does not crash.
4. Use `.index()` to search for that same missing word, `"elephant"`. Run it and read the error Python gives you. Then, in a comment, explain in your own words how `.index()` behaves differently from `.find()` when a search fails.
5. Use `.rindex()` to find the position of the **last** occurrence of `"the"`.

**Why this matters:** `.find()` returns `-1` on failure, so it's safe to use inside an `if` check (`if sentence.find(word) != -1:`) without crashing your program — this is the same defensive instinct behind the input validation in [`managing_complexity.py`](./managing_complexity.py). `.index()` raises an error instead, which is useful when a missing substring really should stop the program rather than be silently ignored. `.rfind()` / `.rindex()` matter whenever the *last* match is the one you actually want — for example, finding a file's extension by locating the last `.` in its name, since a filename can contain other dots earlier on.

---

### Problem 2 -- Counting and Classifying

**Goal:** Use `.count()` to tally occurrences without writing your own loop, and use `.isalnum()` / `.isalpha()` to check what *kind* of characters a string contains.

Create a file called `problem2.py`.

**Counting.** Using the sentence from class —

```python
sentence = "The relentless summer heat in Chicago made even the sidewalks shimmer"
```

1. Use `.count()` to count how many times the lowercase word `"the"` appears. (The sentence also starts with `"The"`, capitalized — does `.count()` treat them as the same word? Predict first, then check.)
2. Use `.count()` to count how many times the single letter `"o"` appears anywhere in the sentence.

**Classifying.** Using this list of test strings:

```python
test_strings = ["hello", "hello123", "hello world", "123", "!!!"]
```

3. Loop over `test_strings` and, for each one, print the string alongside the result of calling `.isalnum()` on it. **Predict each result on paper before running.**
4. Loop over the same list again and print each string alongside `.isalpha()`. Compare your two columns of results — which strings does `.isalnum()` accept that `.isalpha()` rejects, and why?

**Why this matters:** `.count()` is the cumulative pattern from Week 4 (the running-total loop), except Python has already written the loop for you. `.isalnum()` and `.isalpha()` are content checks — they let you ask "is this actually a word?" or "is this actually a number?" *before* trusting a piece of text, the same spirit as the `if` validation checks in `managing_complexity.py`, just aimed at what's *inside* the string rather than its length.

---

### Problem 3 -- Cleaning Up Strings

**Goal:** Use `.strip()`, `.rstrip()`, and `.expandtabs()` to clean up whitespace that doesn't belong in a string.

Create a file called `problem3.py`.

1. Create `messy = "   COMP 170   "`. Print `messy` wrapped in quotes (e.g. `print("'" + messy + "'")`) so the spaces are visible, then print `.strip()` applied to it the same way. Confirm the spaces on **both** sides are gone.
2. Now print `.rstrip()` applied to `messy`, also wrapped in quotes. Compare it to the `.strip()` result from task 1 — which side's spaces survive? In one sentence, explain the difference between `.strip()` and `.rstrip()`.
3. Create `row = "Name\tScore\tGrade"` (note the `\t` tab characters). Print `row` as-is, then print `row.expandtabs()`, then print `row.expandtabs(4)`. Look at how the spacing changes between the three versions.

**Why this matters:** Real text — a line typed by a user, a row read from a file — is full of stray whitespace that has nothing to do with the actual content. `.strip()` is the standard first step before comparing or storing a string (two strings that *look* equal can fail an `==` check if one has trailing spaces the other doesn't). `.expandtabs()` matters whenever you're reading tab-separated data or trying to line up columns of text for display, since a raw `\t` doesn't reliably look the same in every terminal.

---

### Problem 4 -- Formatting and Replacing *(Challenge)*

**Goal:** Use `.center()` to lay out text and `.replace()` to edit it, then combine methods from Problems 1 through 3 into one pipeline.

Create a file called `problem4.py`.

1. Create `label = "COMP 170"`. Print `"|" + label.center(20) + "|"` so the padding is visible between the pipe characters. Then print the same thing using `label.center(20, "*")` — a custom fill character instead of spaces.
2. Create `sentence = "the lazy dog and the lazy cat"`. Print `sentence.replace("the", "THE")` — notice both occurrences change. Then print `sentence.replace("the", "THE", 1)` — the optional third argument limits how many replacements happen. Compare the two outputs and explain the difference in one sentence.
3. **Capstone — combine four methods in one short script:**
   - Start with `raw = "   Chicago\tsummer heat   "` (it has leading/trailing spaces *and* a tab).
   - Clean it up with `.strip()` and `.expandtabs()`.
   - Use `.find()` to locate the word `"summer"` in the cleaned string and print its index.
   - Use `.count()` to count how many times the letter `"e"` appears in the cleaned string.
   - Finally, print a banner line: the word `"REPORT"` passed through `.center(30, "-")`.

**Why this matters:** `.center()` is the standard way to build readable, aligned text — banners, table headers, simple menus. `.replace()` is the most direct way to edit a string's content, and it reinforces something you already saw with `.upper()`: strings don't change in place, `.replace()` *returns a new string* every time. The capstone task is the real point: in an actual program, you rarely use one string method in isolation — you clean a string, search it, measure it, and format it, all in a short sequence. That sequence is exactly what Problems 1 through 4 just gave you, one piece at a time.

---

### Problem 5 -- Reflection on Week 4

**Goal:** Compare your Week 4 solutions with the posted solutions and explain the choices each version makes.

The posted solutions are in [`week04-solutions.py`](./week04-solutions.py). Open that file and your own Week 4 `problem1.py` through `problem4.py` side by side. For each question, look at the relevant section of the posted solution before answering.

Create a file called `problem5.py`. Write your answers as comments:

```python
# Reflection -- Week 4 Solutions Review
#
# Q1. Problem 1 -- indexing
#     scores[5] and scores[len(scores) - 1] produced the same value because
#     the list has 6 items, so the last valid index (5) equals len(scores) - 1.
#     If the list had 7 items instead, would scores[5] and
#     scores[len(scores) - 1] still match? Explain which index each
#     expression would point to.
#
# Q2. Problem 2 -- total / N vs. total // N
#     The posted solution computes average = total / N, using regular
#     (float) division. Try changing it to total // N (integer division)
#     for the temps list and run it. What value do you get, and how does
#     it differ from the posted solution's 80.71428571428571? In one
#     sentence, explain why // is the wrong tool here.
#
# Q3. Problem 3 -- why start at temps[0] instead of 0
#     The posted solution initializes max_so_far = temps[0] before the
#     loop, rather than max_so_far = 0. Describe a list of temperatures
#     (you can make one up) where starting at 0 would produce the wrong
#     answer, and explain why starting at temps[0] avoids that problem.
#
# Q4. Problem 4 -- the optional average variation
#     The posted solution's optional variation computes the average of
#     scores = [92, 78, 85, 90, 67, 88, 95, 72, 81, 64] (81.2), then counts
#     how many scores exceed it (5). Did you attempt this variation in
#     your own problem4.py? If so, did you get the same two numbers? If
#     you didn't attempt it, trace through the posted solution's two loops
#     by hand and confirm 81.2 and 5 are correct.
#
# Q5. Your choice
#     Pick one problem (1-4) where your own code took a noticeably
#     different approach than the posted solution, even if both produced
#     correct output. Describe the difference and say which approach you
#     now prefer and why.
```

A short, honest answer is better than a long vague one. Two or three sentences per question is enough; one clear sentence beats three foggy ones.

---

---

## How to Submit

Upload your work on **Sakai** under the assignment for **Week 05**.

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
