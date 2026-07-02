# COMP 170 — Week 6 Solutions

Topics: pseudocode for `str.find()`, `str.upper()`, and `str.isalpha()` — writing a plain-English, step-by-step description before any Python is written.

Each problem below follows the same shape: a short restatement of the goal, the pseudocode exactly as it would appear as comments in `problem1.py` / `problem2.py` / `problem3.py`, and a working Python function underneath so you can check the pseudocode against real behavior. (Problem 4, the reflection on the Week 5 solutions, is not included here — that one is yours to write.)

---

## Problem 1 — Finding a Character

**Goal:** find the position of the first occurrence of a single character in a string, mirroring `str.find()`. Report $-1$ if the character never appears.

```python
# Problem 1 — Finding a Character
#
# Inputs: a string to search, and a single character to look for
# Output: the position of the first box containing that character,
#         or -1 if the character never appears
#
# Steps:
#   1. Set the current position to 0.
#   2. While the current position is less than the length of the string:
#        a. Look at the character in the box at the current position.
#        b. If that character is the same as the character we are
#           looking for, report the current position and stop —
#           we found the FIRST match, so there is no need to keep going.
#        c. Otherwise, move to the next position (add 1).
#   3. If the loop finishes without ever reporting a position, that
#      means every box was checked and none matched. Report -1.
```

Why the search stops the instant it finds a match: the goal is the *first* occurrence, and positions are examined left to right, one box at a time, so the first match encountered is guaranteed to be the leftmost one.

```python
def find_char(text: str, target: str) -> int:
    position = 0
    while position < len(text):
        if text[position] == target:
            return position
        position += 1
    return -1


if __name__ == "__main__":
    print(find_char("Chicago", "i"))   # 2
    print(find_char("Chicago", "z"))   # -1
```

---

## Problem 2 — Converting to Uppercase

**Goal:** build a new string in which every letter has been converted to uppercase, mirroring `str.upper()`.

```python
# Problem 2 — Converting to Uppercase
#
# Inputs: a string
# Output: a new string, with every lowercase letter converted to
#         uppercase and every other character left unchanged
#
# Steps:
#   1. Set new_string to an empty string — this is where the result
#      is built up, one character at a time.
#   2. Set the current position to 0.
#   3. While the current position is less than the length of the string:
#        a. Look at the character in the box at the current position.
#        b. Find that character's ASCII value.
#        c. If the ASCII value falls between 97 ('a') and 122 ('z'),
#           the character is a lowercase letter: subtract 32 from its
#           ASCII value and convert that number back into a character.
#           This is the character to use.
#        d. Otherwise (the character is already uppercase, or it is a
#           digit, a space, or punctuation), use the character exactly
#           as it is — do not change it.
#        e. Add whichever character was chosen to the end of new_string.
#        f. Move to the next position (add 1).
#   4. Report new_string.
```

Characters that are already uppercase, digits, spaces, and punctuation all take the same path in step (d): the $97$–$122$ test fails for all of them, so they pass through unchanged. Only lowercase letters get the $-32$ adjustment.

```python
def to_upper(text: str) -> str:
    new_string = ""
    position = 0
    while position < len(text):
        character = text[position]
        code = ord(character)
        if 97 <= code <= 122:
            character = chr(code - 32)
        new_string += character
        position += 1
    return new_string


if __name__ == "__main__":
    print(to_upper("Chicago"))       # CHICAGO
    print(to_upper("Room 170!"))     # ROOM 170!
```

---

## Problem 3 — Is This String a Word?

**Goal:** decide whether every character in a string is a letter, mirroring `str.isalpha()`.

```python
# Problem 3 — Is This String a Word?
#
# Inputs: a string
# Output: True if every character in the string is a letter and the
#         string is not empty; False otherwise
#
# Steps:
#   1. If the string has length 0 (no boxes at all), report False
#      immediately and stop — there are no letters to check, so it
#      cannot be a word.
#   2. Set the current position to 0.
#   3. While the current position is less than the length of the string:
#        a. Look at the character in the box at the current position.
#        b. Find that character's ASCII value.
#        c. Decide whether it is a letter: the value must fall between
#           65 ('A') and 90 ('Z'), OR between 97 ('a') and 122 ('z').
#        d. If it is NOT a letter by that test, report False and stop
#           immediately — one non-letter is enough to disqualify the
#           whole string, so there is no need to check the rest.
#        e. Otherwise, move to the next position (add 1).
#   4. If the loop finishes without ever reporting False, every
#      character passed the letter test. Report True.
```

The empty-string check has to come first and separately, because an empty string would otherwise sail through the `while` loop (it never runs, since $0$ is not less than the length $0$) and incorrectly report `True` by default.

```python
def is_word(text: str) -> bool:
    if len(text) == 0:
        return False
    position = 0
    while position < len(text):
        code = ord(text[position])
        is_letter = (65 <= code <= 90) or (97 <= code <= 122)
        if not is_letter:
            return False
        position += 1
    return True


if __name__ == "__main__":
    print(is_word("Hello"))      # True
    print(is_word("hELlo"))      # True
    print(is_word("qqwwwee"))    # True
    print(is_word("HELL0"))      # False — '0' is a digit, not a letter
    print(is_word("good bye"))   # False — the space is not a letter
    print(is_word(""))           # False — empty string
```
