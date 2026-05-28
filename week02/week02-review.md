# COMP 170 — Week 2 Review Notes

These notes reinforce what we covered in Week 2. Read them alongside the class materials and the relevant chapters in Lubanovic's *Introducing Python* (3rd ed.), available free to you at [O'Reilly Learning](https://learning.oreilly.com/library/view/introducing-python-3rd/9781098174392/) using your LUC email.

---

## 1. Two Ways to Run Python

Week 1 focused on writing Python files and running them with `python3 filename.py`. This week we also used Python **interactively** — by typing just `python3` at the shell prompt to open the interpreter:

```
$ python3
>>> 2 + 2
4
>>> "2" + "2"
'22'
>>> 
```

The `>>>` prompt means Python is waiting for you to type a line of code and will evaluate it immediately. This is useful for trying things out and checking your thinking without creating a file. When you are done, type `exit()` or press `Ctrl-D`.

Lubanovic covers both modes in Chapter 1 ("The Python Interactive Interpreter" and "Python Files"). His rule of thumb: use the interactive interpreter to test small snippets; use a `.py` file for anything you want to keep.

---

## 2. Numbers vs. Strings: Type Matters

One of the first things we explored interactively was why `2 + 2` and `"2" + "2"` give different results. The answer is **type**. Every value in Python has a type, and the type determines what the operators do.

| Type | Python name | Example values |
|---|---|---|
| Integer | `int` | `42`, `-7`, `0` |
| Floating-point | `float` | `3.14`, `0.045`, `100.0` |
| String | `str` | `"hello"`, `'COMP 170'` |

When `+` sees two strings, it concatenates them. When it sees two numbers, it adds them. This is not a quirk — it is a feature called **operator overloading**: the same symbol means different things depending on the types involved.

Lubanovic's Chapter 2 ("Types and Variables") explains why Python distinguishes types at all: every value in memory is stored as raw bits, and the type tells Python how to interpret those bits. Chapter 3 ("Numbers") covers the numeric types in detail.

---

## 3. Arithmetic Operators

We used all of these in the compound interest program. Know them:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `1000 + 45` | `1045` |
| `-` | Subtraction | `1045 - 45` | `1000` |
| `*` | Multiplication | `1000 * 2` | `2000` |
| `/` | Division (float result) | `7 / 2` | `3.5` |
| `//` | Integer (truncating) division | `7 // 2` | `3` |
| `%` | Modulo (remainder) | `7 % 2` | `1` |
| `**` | Exponentiation | `1000 * (1.045 ** 10)` | `~1552.97` |

The one that surprised people most was `/` vs `//`. In Python 3, a single `/` *always* gives a float result, even when both operands are integers (`9 / 3` gives `3.0`, not `3`). Use `//` when you specifically want the whole-number part. Lubanovic's Table 3-1 lists all integer operators with examples.

**Operator precedence** matters. In the compound interest formula `principal * (1 + rate) ** term`, the parentheses force the addition before the exponentiation. Without them, `**` would bind more tightly than `*`, giving a wrong result. When in doubt, add parentheses — they make the intent visible to anyone reading the code. Lubanovic discusses this in the "Precedence" section of Chapter 3.

---

## 4. Variables and Type Conversion

We used `int()` and `float()` to convert the strings that `input()` returns into numbers:

```python
principal = int(input("Principal amount: "))
interest_rate = float(input("Interest rate: "))
term = int(input("Term in years: "))
```

`input()` always returns a string — whatever the user types. Trying to do arithmetic on a string causes a `TypeError`. The conversion methods fix this:

- `int("1000")` → `1000`
- `float("0.045")` → `0.045`
- `int(3.99)` → `3` (truncates, does not round)

Lubanovic covers variable assignment and type in Chapter 2, and `int()` and `float()` type conversions in Chapter 3. One important note from that chapter: `int()` will raise a `ValueError` if you pass it a string it cannot convert — `int("hello")` fails. This is Python telling you the conversion is impossible, not just returning zero silently.

---

## 5. The Compound Interest Formula

We built up the formula step by step:

- After year 1: `1000 * 1.045`
- After year 2: `1000 * 1.045 * 1.045` = `1000 * (1.045) ** 2`
- After *n* years: `1000 * (1 + 0.045) ** n`

The general form:

```python
total = principal * (1 + interest_rate) ** term
```

This is the version in both `interest.py` and `interest_pro.py`. The `**` operator handles the repeated multiplication cleanly; you do not need a loop.

---

## 6. Formatted Output with f-strings

The original program used `print("Principal amount:", principal)`. This works, but we also introduced **f-strings**, which embed expressions directly inside a string:

```python
print(f"Principal: ${principal:,.2f}")
```

The `f` before the opening quote marks an f-string. Inside `{}` you put any Python expression. The `:,.2f` after the variable name is a **format specifier**: commas for thousands separators, two decimal places, displayed as a fixed-point number. F-strings keep formatting details next to the values they format, which makes the code easier to read.

---

## 7. Methods: Named, Reusable Pieces of Code

The biggest idea of Week 2 was **methods** — the mechanism for giving a name to a chunk of code so you can call it by name instead of writing the same code again.

We discussed the history: the same concept has been called a *procedure* (1950s), *subroutine* (Fortran), and today most commonly a *method*. The word changes; the idea does not.

### Defining a method

```python
def compute_future_value(principal, interest_rate, term):
    total = principal * (1 + interest_rate) ** term
    return total
```

- `def` is the keyword that starts a method definition
- The name (`compute_future_value`) identifies the method
- The names in parentheses (`principal`, `interest_rate`, `term`) are **parameters** — the inputs the method expects
- `return` sends a value back to whoever called the method
- Everything indented under `def` belongs to the method

### Calling a method

```python
tot = compute_future_value(p, r, t)
```

This passes the values of `p`, `r`, and `t` to the method's parameters and stores the returned result in `tot`.

Lubanovic introduces this concept briefly in Chapter 1 (noting that `print()` and `bool()` are built-in methods with a name, arguments, and a return value), and treats them fully in Chapter 10. The key anatomy he identifies matches what we used: a name, zero or more comma-separated input **arguments** surrounded by parentheses, and a **return value**.

---

## 8. Separation of Concerns

The reason to break the program into methods is not just to avoid repetition. It is to separate three distinct jobs:

| Concern | Method | What it does |
|---|---|---|
| Input | `read_inputs()` | Asks the user for values, returns them |
| Logic | `compute_future_value(...)` | Does the math, returns the result |
| Output | `show_results(...)` | Formats and prints everything |

The payoff: each method has exactly one job. `compute_future_value` never touches the keyboard or the screen — it only does arithmetic. If you later want to read values from a file instead of the keyboard, you change only `read_inputs`. If you want to format the output differently, you change only `show_results`. The math stays untouched either way.

Compare the one-block `interest.py` with the three-method `interest_pro.py`. The main program in the refactored version shrinks to three lines:

```python
p, r, t = read_inputs()
tot = compute_future_value(p, r, t)
show_results(tot, p, r, t)
```

Each line names what it does. The program reads almost like a sentence.

Lubanovic frames the same idea in Chapter 1 with his recipe and knitting-pattern analogy: a program is a sequence of operations that can reference other named sequences. A method is exactly that named sub-sequence.

---

## 9. Comments and Indentation

### Comments

A comment begins with `#` and runs to the end of the line. Python ignores it entirely. Write comments to explain *why* the code does something — not just to restate what the code says:

```python
# Standard compound interest formula: principal grows by (1 + rate) each year,
# applied 'term' times via exponentiation.
total = principal * (1 + interest_rate) ** term
```

The formula line is self-evident. The comment earns its place by naming what the formula is and why exponentiation is the right tool.

### Indentation and scope

Python uses indentation to define **scope** — which lines belong inside a method (or, later, inside a loop or conditional). Every line inside a method must be indented consistently:

```python
def read_inputs():
    principal = int(input("Principal amount: "))   # inside the method
    interest_rate = float(input("Interest rate: ")) # inside the method
    return principal, interest_rate, term           # inside the method

p, r, t = read_inputs()   # outside the method — not indented
```

If a line is indented differently from its neighbors, Python raises an `IndentationError`. Use four spaces per level (do not mix tabs and spaces). Most editors handle this for you once configured correctly.

---

## 10. Returning Multiple Values

`read_inputs` returns three values at once:

```python
return principal, interest_rate, term
```

Python bundles them into a **tuple** (an ordered, immutable sequence). The caller can **unpack** the tuple in a single assignment:

```python
p, r, t = read_inputs()
```

The number of variables on the left must match the number of values returned. This pattern — return multiple values, unpack on one line — appears constantly in Python programs. Lubanovic covers tuples in Chapter 8.

---

## Exercises

Work through these using the Bash + vim + `python3` workflow: edit, save, run, repeat.

---

### Exercise 1 — Interactive exploration

Open the Python interactive interpreter (`python3` at the shell). Try each of the following and predict the result *before* pressing Enter:

```python
>>> 10 / 3
>>> 10 // 3
>>> 10 % 3
>>> 2 ** 8
>>> int(3.9)
>>> float("2.5")
>>> int("hello")
```

For the last one: read the error message. What kind of error is it? What does it tell you?

---

### Exercise 2 — Type detective

Create `types2.py` and run the following:

```python
print(type(1000))
print(type(1000.0))
print(type("1000"))
print(type(int("1000")))
print(type(1000 / 10))
print(type(1000 // 10))
```

Questions:
1. Which two lines print the same type?
2. What is the type of `1000 / 10` — and why?
3. What does `int("1000")` prove about `type()` and `int()`?

---

### Exercise 3 — Operator precedence

Predict the output of each line, then verify in the interpreter:

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)       # exponentiation is right-associative
print((2 ** 3) ** 2)
print(10 - 4 - 2)
print(10 - (4 - 2))
```

The third and fourth lines may surprise you. Try to explain what Python does with `2 ** 3 ** 2` before looking it up.

---

### Exercise 4 — Rewrite with a method

Start with this one-block program:

```python
celsius = float(input("Temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(celsius, "°C is", fahrenheit, "°F")
```

Rewrite it as three methods following the same pattern as `interest_pro.py`:
- `read_input()` — asks for the Celsius temperature and returns it
- `convert(celsius)` — computes and returns the Fahrenheit equivalent
- `show_result(celsius, fahrenheit)` — prints the result

The main program should be three lines.

---

### Exercise 5 — f-strings

Take the output line from Exercise 4's `show_result` method and rewrite it as an f-string that:
- Shows the Celsius value with one decimal place
- Shows the Fahrenheit value with one decimal place

Sample output for an input of `100`:
```
100.0 °C is 212.0 °F
```

---

## Quick Reference Card

### Python — Week 2

```python
# Arithmetic
7 / 2          # 3.5  (always float)
7 // 2         # 3    (integer, truncates)
7 % 2          # 1    (remainder)
2 ** 10        # 1024 (exponentiation)

# Type conversion
int("42")      # 42
float("3.14")  # 3.14
int(3.99)      # 3  (truncates)

# f-strings
f"Value: {x:.2f}"          # two decimal places
f"Amount: ${total:,.2f}"   # commas + two decimal places

# Defining a method
def name(param1, param2):
    result = param1 + param2
    return result

# Calling a method
answer = name(10, 5)

# Returning multiple values
def get_pair():
    return 1, 2

a, b = get_pair()   # unpack tuple

# Comments
# Explain WHY, not what the code says
```

### Bash — still in use

```
python3               start interactive interpreter
python3 file.py       run a script
exit()  or Ctrl-D     leave the interpreter
```
