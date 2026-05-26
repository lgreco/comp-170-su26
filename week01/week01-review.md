# COMP 170 — Week 1 Review Notes

These notes reinforce what we covered in Week 1. Read them alongside your class materials, and follow the links when you want a deeper explanation or a different angle on the same idea.

---

## 1. The Shell: Your Primary Interface to the Computer

When you open a terminal, you are talking to a **shell** — a program that reads the commands you type, passes them to the operating system, and prints the result. The shell is the most direct way to control your computer. GUIs (icons, menus, windows) are built on top of the same underlying system; the shell exposes that system directly.

On macOS and Linux, the most common shell is **Bash** (Bourne Again Shell). When you see the `$` prompt, Bash is waiting for a command.

The relationship looks like this:

```
You  →  Terminal  →  Shell (Bash)  →  Operating System  →  Hardware
```

Every command you type is a small program. When you type `ls`, Bash finds the `ls` program, runs it, and prints its output. You are programming from the moment you type your first command.

**Good starting points:**
- [Learning the Shell — linuxcommand.org](https://linuxcommand.org/lc3_learning_the_shell.php) — a clear, free introduction written for beginners; covers everything in this section
- [The Unix Shell — Software Carpentry](https://swcarpentry.github.io/shell-novice/) — a structured lesson with exercises, widely used in university courses (you may skip the setup part)
- [The Missing Semester of Your CS Education: The Shell — MIT](https://missing.csail.mit.edu/2020/course-shell/) — a concise lecture with video, aimed at first-year CS students

---

## 2. Essential Bash Commands

| Command | What it does |
|---|---|
| `pwd` | **P**rint **w**orking **d**irectory — shows where you are in the filesystem |
| `ls` | **L**i**s**t files and folders in the current directory |
| `ls -l` | List files with details (size, permissions, date modified) |
| `mkdir name` | **M**a**k**e a new **dir**ectory named `name` |
| `cd name` | **C**hange **d**irectory — move into the folder named `name` |
| `cd ..` | Move up one level (to the parent directory) |
| `cd ~` | Move to your home directory, no matter where you are |
| `python3 file.py` | Run the Python script `file.py` with the Python 3 interpreter |
| ``vim` file.py` | Open `file.py` in the `vim` editor (creates it if it doesn't exist) |

**Tips:**
- Commands are case-sensitive. `ls` works; `LS` does not.
- The prompt shows where you are. After `cd comp170`, you might see `comp170 $` or a full path like `/Users/yourname/comp170 $`.
- Press the **up arrow** to cycle through previous commands.

---

## 3. Navigating the Filesystem: `.` and `..`

The filesystem is a tree of folders (directories). At any moment, you are inside one of them — your **current directory**.

Two special shortcuts exist in every directory:

| Shortcut | Meaning |
|---|---|
| `.` | The **current** directory (where you are right now) |
| `..` | The **parent** directory (one level up) |

Examples:
```
$ pwd
/Users/alice/comp170

$ cd ..
$ pwd
/Users/alice

$ cd comp170
$ pwd
/Users/alice/comp170
```

You will see `.` used when running scripts: `python3 ./hello.py` explicitly means "run `hello.py` in the current directory." Both `python3 hello.py` and `python3 ./hello.py` work; the `./` makes the location explicit.

`..` can be chained: `cd ../..` goes up two levels at once.

---

## 4. File Extensions

A **file extension** is the suffix after the last dot in a filename. It signals the file's format:

| Extension | Meaning |
|---|---|
| `.py` | Python source code |
| `.txt` | Plain text |
| `.md` | Markdown (formatted plain text) |
| `.html` | Web page |
| `.csv` | Comma-separated values (spreadsheet data) |

Extensions are a convention, not a rule enforced by the OS. The computer does not care if you name a Python file `hello.txt` — but the terminal, your editor, and other programmers will be confused. Use `.py` for Python files, always.

---

## 5. Running Python from the Shell

Python is an **interpreter**: a program that reads your code and executes it line by line. You invoke it from Bash like this:

```
$ python3 hello.py
```

Breaking this down:
- `python3` — the Python 3 interpreter (use `python3`, not `python`, to be explicit)
- `hello.py` — the script to run; the interpreter reads this file and executes it

The script must exist in your current directory (or you must provide a path to it). Always `cd` to the right folder first, then run.

**Official reference:** [Using the Python Interpreter — docs.python.org](https://docs.python.org/3/tutorial/interpreter.html)

---

## 6. `vim` Quick Reference

`vim` is a terminal-based text editor available on virtually every Unix system. Its defining feature is **modes**: in Normal mode, keys are commands; in Insert mode, keys type text.

```
Open a file:   vim hello.py
Enter Insert:  i
Return to Normal: Esc
Save:          :w
Quit:          :q
Save and quit: :wq
Quit without saving: :q!
```

When in doubt, press `Esc`. It always returns you to Normal mode and never causes harm.

**Interactive practice:**
- [Open`vim` — interactive `vim` tutorial in the browser](https://www.open`vim`.com/) — no installation needed; practice the basics live
- [`vim`tutor](https://`vim`school.netlify.app/introduction/`vim`tutor/) — also available by typing ``vim`tutor` in your terminal; a guided 30-minute walkthrough built into most systems

---

## 7. Data Types in Python

Every value in Python has a **type** — a category that determines what the value is and what you can do with it.

### The three types you will use most in COMP 170:

**`str` — string**
A sequence of characters. Always wrapped in quotes (single or double).
```python
"Hello, World!"
'Chicago'
"COMP 170"
```

**`int` — integer**
A whole number (no decimal point).
```python
42
-7
0
```

**`float` — floating-point number**
A number with a decimal point.
```python
3.14
-0.5
100.0
```

### How Python handles expressions depends on type

```python
print("chi" + "cago")    # "chi" and "cago" are both str → concatenation → chicago
print(4 - 5)             # 4 and 5 are both int → subtraction → -1
print(10 / 3)            # two ints with / → float result → 3.3333333333333335
print(10 // 3)           # integer division (floor) → 3
```

Notice: `+` means something different for strings (join them) than for numbers (add them). The **type** of the values determines the behavior of the operator.

### Checking the type of a value

```python
print(type("hello"))     # <class 'str'>
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
```

**Further reading:**
- [Python Data Types — Real Python](https://realpython.com/python-data-types/) — clear introductory walkthrough with examples
- [Variables, Expressions, and Statements — Think Python (Downey)](https://greenteapress.com/thinkpython2/html/thinkpython2002.html) — free open textbook; Chapter 2 covers types, values, and expressions at exactly this level

---

## 8. Exercises

Work through these in order. Each builds on the previous. Use the Bash + `vim` + python3 workflow: edit, save, run, repeat.

---

### Exercise 1 — Hello, World (baseline)

Create a file called `hello.py` in your `comp170/` folder containing:

```python
print("Hello, World!")
```

Run it:
```
$ python3 hello.py
Hello, World!
```

**Goal:** Confirm your environment is working. If you see `Hello, World!`, everything is set up correctly.

---

### Exercise 2 — Make it yours

Edit `hello.py` to print your own name instead of `World`. Run it and confirm the output.

Then add a second `print` statement so the program outputs two lines — for example:
```
Hello, Alice!
Welcome to COMP 170.
```

---

### Exercise 3 — String concatenation

Create a new file `strings.py` and try these print statements one at a time. **Before running each line, predict what the output will be.**

```python
print("chi" + "cago")
print("Hello" + ", " + "World!")
print("comp" + "170")
print("ha" * 3)
```

Questions to answer for yourself after running:
1. What does `+` do when both values are strings?
2. What does `*` do when one value is a string and the other is an integer?
3. What happens if you try `print("hello" + 5)`? Try it and read the error message carefully.

---

### Exercise 4 — Arithmetic

Create `math.py` and try each of the following. Again, predict before running.

```python
print(4 - 5)
print(10 + 3)
print(7 * 6)
print(10 / 4)
print(10 // 4)
print(10 % 3)
```

Questions:
1. What is the difference between `/` and `//`?
2. What does `%` do? (This is the **modulo** operator — it returns the remainder.)
3. What does Python output for `4 - 5`? Is a negative result surprising?

---

### Exercise 5 — Types matter

Create `types.py` and run the following:

```python
print(type("hello"))
print(type(42))
print(type(3.14))
print(type("42"))
print(type(3 + 4))
print(type(3 + 4.0))
```

Questions:
1. `"42"` and `42` look similar but are not. What is the difference?
2. What type does Python produce when you add an `int` and a `float`?

---

### Exercise 6 — Putting it together

Create `intro.py`. The program should:
- Store your name in a variable
- Store your major in a variable
- Print at least three lines of output using those variables
- Include at least one arithmetic expression in the output (for example, the number of days until the end of the semester, or the result of any calculation you choose)

Sample output (yours will differ):
```
Name: Alice
Major: Computer Science
Days left in the semester: 42
```

---

## Quick Reference Card

### Bash
```
pwd              where am I?
ls               what's here?
ls -l            what's here, with details?
mkdir name       create a folder
cd name          go into a folder
cd ..            go up one level
cd ~             go home
python3 file.py  run a Python script
`vim` file.py      open a file in `vim`
```

### `vim`
```
i       start typing (Insert mode)
Esc     stop typing (Normal mode)
:w      save
:q      quit
:wq     save and quit
:q!     quit without saving
```

### Python — Week 1
```python
print("text")          print a string
print(expression)      print a number or result
print("a" + "b")       concatenate strings → ab
print(4 - 5)           arithmetic → -1
name = "Alice"         create a variable
print(name)            use a variable
type(value)            find out what type a value is
```
