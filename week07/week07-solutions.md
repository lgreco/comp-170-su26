# COMP 170 -- Week 7 Solutions

Topics: pseudocode for finding every occurrence of a character, and for finding a substring inside a longer string -- writing a plain-English, step-by-step description before any Python is written.

Each problem below follows the same shape: a short restatement of the goal, the pseudocode exactly as it would appear as comments in `problem1.py` / `problem2.py`, and a working Python function underneath so you can check the pseudocode against real behavior. (Problem 3, the reflection on the Week 6 solutions, is not included here -- that one is yours to write.)

---

## Problem 1 -- Finding Every Occurrence

**Goal:** find every position where a single letter appears in a string, returning a list of those positions. Report an empty list if the letter never appears.

```python
# Problem 1 -- Finding Every Occurrence
#
# Inputs: a single letter to search for, and a string to search within
# Output: a list containing every position where the letter appears,
#         in order from left to right; an empty list if it never
#         appears at all
#
# Steps:
#   1. Set up an empty list called matches -- this is where every
#      matching position gets collected as it is found.
#   2. Set the current position to 0.
#   3. While the current position is less than the length of the string:
#        a. Look at the character in the box at the current position.
#        b. If that character is the same as the letter we are
#           looking for, add the current position to matches. Unlike
#           finding the FIRST occurrence, do NOT stop here -- there
#           may be more matches further along the string.
#        c. Move to the next position (add 1), whether or not this
#           position matched.
#   4. Report matches. If no position ever matched, matches is still
#      the empty list it started as -- that is exactly the right way
#      to report "never found" here, since the output is always a
#      list, not a single number pretending to mean "not found."
```

Why the loop never stops early: Problem 1 in Week 6 (`find_char`) reports the position and returns the instant it finds a match, because it only wants the *first* one. This problem wants *every* one, so every position has to be checked, match or no match, all the way to the end of the string.

```python
def positions(letter: str, text: str) -> list:
    matches = []
    position = 0
    while position < len(text):
        if text[position] == letter:
            matches.append(position)
        position += 1
    return matches


if __name__ == "__main__":
    print(positions("a", "banana"))   # [1, 3, 5]
    print(positions("z", "banana"))   # []
```

---

## Problem 2 -- Finding a Substring

**Goal:** find the position where one string (the target) begins inside another string (the text). Report $-1$ if the target never appears inside the text at all.

```python
# Problem 2 -- Finding a Substring
#
# Inputs: the string being searched FOR (the target), and the string
#         being searched WITHIN (the text)
# Output: the position in text where target begins, or -1 if target
#         never appears anywhere inside text
#
# Steps:
#   1. Set the starting position to 0.
#   2. Set result to -1 -- this is what gets reported if target is
#      never found; it only changes once a real match is confirmed.
#   3. Set found to False -- this flag is what lets the outer loop
#      stop searching once a match has been confirmed, without ever
#      needing to report a value from the middle of the function.
#   4. While there is still enough room left in text for target to
#      possibly fit, starting at the current starting position, AND
#      found is still False (that is, while starting position + the
#      length of target is not more than the length of text, and no
#      match has been confirmed yet):
#        a. Assume, for now, that target matches starting here (set a
#           flag, match, to True).
#        b. Set an offset to 0 -- this walks through target itself,
#           one character at a time.
#        c. While the offset is less than the length of target AND the
#           match flag is still True:
#             i.   Compare the character in text at position
#                  (starting position + offset) to the character in
#                  target at position offset.
#             ii.  If they are different, set match to False --
#                  one mismatched character is enough to rule out
#                  this starting position, so there is no need to
#                  check the rest of target.
#             iii. Move to the next offset (add 1).
#        d. If match is still True once that inner check finishes,
#           every character of target matched, in order, starting
#           here. Set result to the starting position and set found
#           to True -- this ends the outer loop on its next check,
#           since there is no need to keep searching once a match is
#           confirmed.
#        e. Otherwise, move to the next starting position (add 1) and
#           repeat.
#   5. Report result. If the outer loop finished because found became
#      True, result holds the matching starting position. If it
#      finished because there was no more room left for target to
#      fit, found never became True, and result is still -1 -- exactly
#      the right way to report "never found."
#
# Special case: if target is longer than text, there is no starting
# position where it could ever fit -- the very first check in step 4
# already fails, so the loop body never runs even once, and result is
# reported as -1 immediately.
```

Why this needs two loops, not one: every method built so far compares one character at a time to one target character. Here, at each candidate starting position, a single comparison is not enough -- the *whole* target has to match, character by character, before that starting position counts as a match. That means a loop nested inside a loop: an outer loop that tries each starting position in text, and an inner loop that checks, character by character, whether target matches in full starting there.

This version also reports its answer from exactly one place. Instead of returning the instant a match is confirmed, it records the answer in `result` and flips a `found` flag, which the outer loop's own condition then uses to stop searching -- so there is only ever one `return`, at the very end, after both loops are done.

```python
def find_substring(target: str, text: str) -> int:
    start = 0
    result = -1
    found = False
    while start + len(target) <= len(text) and not found:
        match = True
        offset = 0
        while offset < len(target) and match:
            if text[start + offset] != target[offset]:
                match = False
            offset += 1
        if match:
            result = start
            found = True
        start += 1
    return result


if __name__ == "__main__":
    print(find_substring("cag", "Chicago"))            # 3
    print(find_substring("xyz", "Chicago"))             # -1
    print(find_substring("Chicagoland", "Chicago"))     # -1 (target longer than text)
```
