# COMP 170 — Last Assignment

This is the final assignment of the course. It pulls together the last thing we talked about in class — reading a book straight from the internet and counting its words with a dictionary — with one small piece of cleanup we never got to: removing punctuation before counting. It also asks you to step back and reflect honestly on your semester.

---

## Reading a File from a URL

So far, every file we've read ([`SimpleFileOps.py`](../week10/SimpleFileOps.py) in week10, [`file_processing.py`](../week11/file_processing.py) in week11) has lived on our own computer. But a file doesn't have to be local — a web address (URL) points at a file too, sitting on someone else's computer, and Python can read it almost the same way.

The only new tool we need is `urllib.request`, part of the Python standard library — no installation required, and it's the **only** import this assignment needs.

```python
import urllib.request


def read_url(url: str) -> None:
    """Read a text file from a URL and print it, one line at a time."""
    with urllib.request.urlopen(url) as response:
        for raw_line in response:
            line = raw_line.decode("utf-8")
            print(line.rstrip("\n"))


if __name__ == "__main__":
    book_url = "https://www.gutenberg.org/files/98/98-0.txt"
    read_url(book_url)
```

A few things to notice, since this looks similar to reading a local file but isn't quite the same:

- `urllib.request.urlopen(url)` opens a connection to the URL and gives back a response object you can loop over line by line, the same way `f` behaves in `for line in f:` when `f` is a local file.
- Each `raw_line` comes back as **bytes**, not a string — that's the `b'...'` you'd see if you printed it directly. `.decode("utf-8")` converts it into the ordinary string type we've used all along. This is the one genuinely new step; everything else is `.rstrip()` and `print()`, exactly like week10.
- `with ... as response:` closes the connection automatically when the block ends, the same job `.close()` does for local files — except here Python does it for us.
- Reading line by line (instead of, say, `response.read()` all at once) means we're never holding the whole book in memory at the same moment — the same reasoning from the last class of the term about why we read Gutenberg books this way.

Use this scaffold as the starting point for the problem below. Swap in whatever URL the problem asks for.

---

## A Brief Tutorial: Removing Punctuation, the Simple Way

Once we start counting words from a real book, punctuation gets in the way immediately: `"times,"` and `"times"` are the same word to us, but two different strings to Python, because the comma is part of the string.

You do **not** need regular expressions (`re`) for this — they're a powerful tool for a much harder version of this problem, and pulling them in here would be using a sledgehammer on a thumbtack. The plain-Python way uses only what we already know: a string of characters to remove, and `.replace()`.

```python
PUNCTUATION = ".,!?;:\"'()[]{}-–—"


def strip_punctuation(word: str) -> str:
    """Return word with common punctuation characters removed."""
    for mark in PUNCTUATION:
        word = word.replace(mark, "")
    return word


print(strip_punctuation("times,"))   # times
print(strip_punctuation("\"best\"")) # best
print(strip_punctuation("it's"))     # its
```

How it works, one piece at a time:

- `PUNCTUATION` is just a string — a hardcoded list of the punctuation marks we want gone. You can add or remove characters from it depending on what a particular text needs (some books use curly quotes `“` `”` instead of straight ones, for example).
- The `for mark in PUNCTUATION:` loop walks through that string one character at a time — the same enhanced `for` loop from week05, just looping over a string instead of a list.
- `word.replace(mark, "")` returns a **new** string with every occurrence of `mark` deleted (replaced with the empty string). Because strings are immutable, we reassign the result back to `word` each time through the loop, so by the end every punctuation mark in `PUNCTUATION` has been stripped out.
- This is not perfect — `"it's"` becomes `"its"`, which quietly changes the word (and its length — worth remembering below, where length is exactly what we're filtering on) — but it's simple, it's honest about its limits, and it's enough for counting word frequencies at the level this course covers. A more careful version is exactly the kind of thing worth exploring in self-study.

---

## A Quick Introduction to Python Dictionaries

We used dictionaries in the last week of class to replace the two-synchronized-lists approach, but here is the idea in one place, following the explanation in Lubanovic's *Introducing Python* (Ch. 9, "Dictionaries and Sets").

A list looks things up by **position** — `words[0]` means "the first word, whatever it is." A dictionary looks things up by **key** — `frequency["THE"]` means "whatever count is paired with the word `THE`," no matter where that pairing sits inside the dictionary. Each entry is a `key: value` pair, the same way a student ID (key) points at one specific student's record (value), rather than "the fifth student in the room."

```python
frequency = {}                      # an empty dictionary

frequency["THE"] = 1                # add a new key, paired with the value 1
frequency["THE"] = frequency["THE"] + 1   # look up THE's value, then update it

print(frequency["THE"])             # 2
print("THE" in frequency)           # True  -- checks for a key, not a value
print("ZEBRA" in frequency)         # False -- ZEBRA was never added as a key
```

A few things worth calling out:

- `{}` creates an empty dictionary, the same way `[]` creates an empty list.
- `dict[key] = value` both **adds** a new pair (if the key isn't there yet) and **updates** an existing one (if it is) — there's no separate "add" method to remember, unlike `.append()` for lists.
- `key in dict` checks whether `key` exists as one of the dictionary's keys, and returns `True`/`False` — the same `in` we've used to check whether a letter is inside a string.
- Trying to read a key that was never added (`frequency["ZEBRA"]` before it exists) raises a `KeyError`. That's why counting code almost always checks `in` first:

```python
if word in frequency:
    frequency[word] = frequency[word] + 1   # already seen -- bump the count
else:
    frequency[word] = 1                     # first time seeing this word
```

- `.items()` lets you loop over every key and value together, which is how we'll turn a dictionary into something we can sort:

```python
for word, count in frequency.items():
    print(word, "->", count)
```

That's the entire dictionary vocabulary this assignment needs. If you want the fuller picture — dictionary methods we didn't cover, and the related `set` type — Lubanovic's chapter is a good next stop.

---

## The Problems

### Problem 1 — Most and Least Frequent Five-Letter Words

**Goal:** Write a program, `word_count_url.py`, that reads a public-domain book directly from Project Gutenberg by URL, cleans each word of punctuation, counts every word with a dictionary, and reports the **10 most frequent** and **10 least frequent five-letter words** in the book.
I recommend Charles Dicken's *Tale of Two Cities*, but any book will do.

**Requirements:**

- Use the `read_url`-style scaffold above to open and read the book line by line. `import urllib.request` should be the only import in your file.
- Use a URL to a plain-text book on Project Gutenberg (for example, `https://www.gutenberg.org/files/98/98-0.txt` for *A Tale of Two Cities*, the book we used in class).
- For each line, split it into words with `.split()`.
- Convert each word to uppercase before counting, so `"It"` and `"it"` count as the same word — the same normalization step from week11.
- Strip punctuation from each word using `strip_punctuation()` before counting it. Do this **before** checking the word's length, since a stray comma or quotation mark would otherwise throw the count off by one character.
- Use a single dictionary, `frequency`, mapping each cleaned word to how many times it appears — no synchronized lists.
- Once the whole book has been counted, build a second collection containing only the entries from `frequency` whose word is **exactly 5 letters long** (`len(word) == 5`). A plain loop is enough:

```python
five_letter = []
for word, count in frequency.items():
    if len(word) == 5:
        five_letter.append((word, count))
```

- From `five_letter`, print:
  - the total number of unique five-letter words,
  - the 10 most frequent five-letter words and their counts, in descending order by count,
  - the 10 least frequent five-letter words and their counts, in ascending order by count.
- If there is a tie for the 10th spot in either list, it's fine to break the tie however Python's `.sort()` naturally does — you don't need to handle ties specially.

Organize your solution with a `main()` function and an `if __name__ == "__main__":` guard, the same as every program since week05.

**Example output shape** (your words and numbers will differ):

```
$ python3 word_count_url.py
Unique 5-letter words: 612
Most frequent 5-letter words:
WHICH: 412
THEIR: 298
THERE: 265
...
Least frequent 5-letter words:
ABYSS: 1
CHINK: 1
GLASS: 1
...
```

Hint: sorting a list of `(word, count)` tuples by count is new. One simple way, using only what we've covered:

```python
five_letter.sort(key=lambda pair: pair[1])          # ascending -- least frequent first
least_frequent = five_letter[:10]

five_letter.sort(key=lambda pair: pair[1], reverse=True)   # descending -- most frequent first
most_frequent = five_letter[:10]
```

`lambda pair: pair[1]` is a small unnamed function that tells `.sort()` to compare tuples by their second element — the count — instead of the word itself. You haven't written a `lambda` before; treat it here as a shorthand for "sort by count," and feel free to look up `sort()`'s `key` argument if you want the fuller explanation.

---

### Problem 2 — A Reflection on Your Semester

**Goal:** Step back from the code and reflect honestly on your semester in COMP 170. This is not a summary of what we covered — it's an honest self-assessment, and it asks you to propose your own final grade with a justification.

**Write a plain text file**, `reflection.txt` (not a `.py` file — this is prose, not code), addressing all of the following:

- **Attendance.** How many classes did you attend this term, as best you can recall? Was your attendance a help or a hindrance to how well you learned the material?
- **Participation.** Did you ask questions, work through problems out loud, help classmates, or otherwise engage during class? Or did you mostly observe?
- **Code quality.** Looking back at the posted solutions across the term, how closely did your own submissions match them in approach and correctness? Where did you consistently struggle, and where did you consistently do well?
- **Your proposed final grade.** Based on the three points above, propose the letter grade you believe you earned this semester, and justify it in your own words.

Keep in mind the grading floor set by attendance, and be honest with yourself about where you fall:

- **5 to 9 absences** preclude an **A**, unless those absences are excused by the university police.
- **10 or more absences** preclude a **passing grade**, regardless of code quality or participation.

**Requirements:**

- Maximum **300 words**. Being concise and specific is worth more than being long — say what actually happened, not what sounds good.
- Submit as a plain `.txt` file, not a `.py`, `.docx`, or `.pdf` file.

---

## How to Submit

Upload your work on **Sakai** under the assignment for the **Final Assignment**, following the same rules as every prior assignment this term.

Submit these files:

```
word_count_url.py
reflection.txt
```

`word_count_url.py` must be a Python file — no screenshots, no PDFs. `reflection.txt` must be a plain text file — no `.docx`, no `.pdf`. Confirm with `ls` that both files exist before you upload.

---

## How Your Work Is Evaluated

**Submission credit.** Submitting an assignment earns you 1 point; not submitting earns 0. This is not a score for quality — it simply records that you completed the work on time.

**No late work, no extensions.** We discuss solutions in class immediately after the deadline, and solutions are posted at the same time. Because the answers are public from that moment on, late submissions cannot be accepted and deadlines cannot be extended.

**Self-evaluation.** After solutions are posted, you evaluate your own work. Using the posted solutions and Leo's written instructions as a guide, you decide what you understood, what you got wrong, and what you need to practice to avoid the same mistakes in the future. Making mistakes is how learning happens. Not repeating them is the evidence that it did.
