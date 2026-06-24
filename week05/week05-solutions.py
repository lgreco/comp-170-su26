# COMP 170 — Week 5 Solutions
# Topics: string search methods, counting/classifying, whitespace cleanup,
# formatting/replacing, reflection on Week 4 patterns


# ===========================================================================
# Problem 1 — Searching a String
# ===========================================================================
#
# Python strings have four built-in search methods. They differ along two
# axes:
#
#   1. Direction — does it find the FIRST match (left to right) or the LAST?
#      find() and index() scan left to right, so they return the first match.
#      rfind() and rindex() scan right to left, so they return the last match.
#
#   2. Failure behavior — what happens when the target is NOT in the string?
#      find() and rfind() return -1 (a sentinel value meaning "not found").
#      index() and rindex() raise a ValueError and crash the program.
#
# The -1 return from find() is safe to test in an if-statement:
#
#     if sentence.find("fox") != -1:
#         ... do something ...
#
# This is the same defensive instinct as the input-validation check in
# managing_complexity.py — guard against bad input before acting on it.

print("--- Problem 1 ---")

sentence = "the quick brown fox jumps over the lazy dog the fox ran"

# ---- Task 1: find() — first occurrence of "fox" ----
#
# find() returns the index (position) of the FIRST character of the first
# match. Positions are counted starting from 0, just like list indices.
#
#   "the quick brown fox ..."
#    0123456789012345678...
#                    ^ "fox" starts here (index 16)
#
first_fox = sentence.find("fox")
print("First 'fox' at index:", first_fox)     # 16

# ---- Task 2: rfind() — last occurrence of "fox" ----
#
# rfind() does the same scan, but starts from the RIGHT end of the string
# and works left. It stops at the LAST match it finds.
# The sentence is "...the fox ran", so this "fox" is near the end.
#
last_fox = sentence.rfind("fox")
print("Last  'fox' at index:", last_fox)      # 48

# Why are they different? Because "fox" appears TWICE in the sentence —
# once after "brown" and once near the end. find() found the earlier one
# (index 16); rfind() found the later one (index 48). If the word appeared
# only once, both methods would return the same index.

# ---- Task 3: find() for a missing word — safe, returns -1 ----
#
# "elephant" is not in the sentence at all. find() does not crash; it
# quietly returns -1 to signal "nothing found." This is why find() is the
# safer choice when you don't know whether the word exists.
#
missing = sentence.find("elephant")
print("'elephant' with find():", missing)     # -1  (no crash!)

# ---- Task 4: index() for the same missing word — raises ValueError ----
#
# index() behaves identically to find() when the word IS present.
# The difference only shows up on failure: instead of returning -1,
# index() raises a ValueError and halts the program.
#
# In a real script you would never call index() unless you are CERTAIN
# the word is there (or you wrap the call in a try/except block so you
# can handle the error gracefully). Here we use try/except to let the
# solutions file keep running while still showing you the error message.
#
try:
    sentence.index("elephant")
except ValueError as error:
    print("index() raised a ValueError:", error)
# ^ The error message is: substring not found

# How .index() differs from .find() when the target is missing:
#   .find()  → returns -1 silently; the program keeps running.
#   .index() → raises ValueError immediately; the program stops (or the
#              except block catches it). Use index() only when you are sure
#              the word is present and you want the crash to tell you
#              something went wrong — a deliberate "fail loudly" choice.

# ---- Task 5: rindex() — last occurrence of "the" ----
#
# "the" appears three times: at the very start, before "lazy", and before
# "fox" near the end. rindex() finds the last one.
#
last_the = sentence.rindex("the")
print("Last 'the' at index:", last_the)       # 44


# ===========================================================================
# Problem 2 — Counting and Classifying
# ===========================================================================
#
# .count(sub) scans the entire string and returns how many times the
# substring sub appears. It is essentially the cumulative-counting loop
# from Week 4, except Python has already written that loop for you.
#
# .isalnum() and .isalpha() are content-check methods — they look at every
# character in the string and answer a yes/no question:
#
#   .isalnum() → True if EVERY character is a letter OR a digit (no spaces,
#                no punctuation).
#   .isalpha() → True if EVERY character is a letter (digits excluded too).
#
# Both return False for an empty string.

print("\n--- Problem 2 ---")

sentence2 = "The relentless summer heat in Chicago made even the sidewalks shimmer"

# ---- Counting task 1: how many times does "the" (lowercase) appear? ----
#
# PREDICT FIRST: the sentence starts with "The" (capital T), and contains
# "the" once inside ("made even the sidewalks"). Does .count() treat them
# as the same word?
#
# Python strings are case-sensitive. "The" ≠ "the". So .count("the") only
# counts the lowercase version.
#
count_the = sentence2.count("the")
print('Count of "the" (lowercase):', count_the)   # 1
# "The" at the start is NOT counted. Only "the" before "sidewalks" is.

# ---- Counting task 2: how many times does the letter "o" appear? ----
#
# .count() works on single characters too — it treats them as substrings
# of length 1. Scan the sentence mentally: "Chicago" has one 'o'; no other
# word has one.
#
count_o = sentence2.count("o")
print('Count of "o":', count_o)                   # 1

# ---- Classifying task 3: .isalnum() on each test string ----
#
# We loop with an enhanced for-loop (for item in list) rather than a
# range-based loop, because we only need the VALUE of each string, not its
# index position. When the index isn't needed, the enhanced form is cleaner.
#
test_strings = ["hello", "hello123", "hello world", "123", "!!!"]

print("\n.isalnum() results:")
for item in test_strings:
    print(f"  '{item}' → {item.isalnum()}")

# Predicted results (think before running!):
#   "hello"       → True   (all letters → letters are alphanumeric)
#   "hello123"    → True   (letters and digits → all alphanumeric)
#   "hello world" → False  (the SPACE is not a letter or digit)
#   "123"         → True   (all digits → digits are alphanumeric)
#   "!!!"         → False  (punctuation is neither letter nor digit)

# ---- Classifying task 4: .isalpha() on the same list ----
#
print("\n.isalpha() results:")
for item in test_strings:
    print(f"  '{item}' → {item.isalpha()}")

# Predicted results:
#   "hello"       → True   (all letters)
#   "hello123"    → False  (digits are not letters)
#   "hello world" → False  (space is not a letter)
#   "123"         → False  (digits are not letters)
#   "!!!"         → False  (punctuation is not a letter)
#
# Comparing the two columns:
#   .isalnum() accepts "hello123" and "123" — strings that contain digits.
#   .isalpha() rejects them — only pure letters pass.
#
# WHY this distinction matters: if you want to check "is this a real word?"
# use .isalpha(). If you want to check "is this clean input with no symbols
# or spaces?", use .isalnum(). Both reject spaces and punctuation, but only
# .isalpha() also rejects digits.


# ===========================================================================
# Problem 3 — Cleaning Up Strings
# ===========================================================================
#
# Real-world text is messy. A user might type extra spaces before or after
# their input; a file might use tab characters to separate columns. These
# three methods deal with that kind of whitespace noise:
#
#   .strip()      — removes whitespace from BOTH the left and right ends.
#   .rstrip()     — removes whitespace from the RIGHT end only ("r" = right).
#   .lstrip()     — removes whitespace from the LEFT end only (not asked here).
#   .expandtabs() — replaces each \t tab character with enough spaces to
#                   reach the next tab stop (default tab-stop every 8 chars;
#                   pass a number to change the interval).
#
# None of these methods change the string in place. They return a NEW string.
# The original is untouched. (Strings are immutable in Python — you can never
# change a character inside an existing string object.)

print("\n--- Problem 3 ---")

messy = "   COMP 170   "

# ---- Task 1: .strip() removes spaces on both ends ----
#
# Wrapping in quotes with + makes the leading/trailing spaces visible.
# Without the wrapping quotes, print() silently hides them.
#
print("Original:", "'" + messy + "'")
print("strip()  :", "'" + messy.strip() + "'")
# Output:
#   Original: '   COMP 170   '
#   strip()  : 'COMP 170'
# All three leading spaces and all three trailing spaces are gone.

# ---- Task 2: .rstrip() removes spaces on the RIGHT end only ----
#
print("rstrip() :", "'" + messy.rstrip() + "'")
# Output:
#   rstrip() : '   COMP 170'
# The three LEADING spaces on the left survive; only the trailing spaces
# are stripped. The difference: .strip() cleans both sides; .rstrip() cleans
# only the right side, leaving the left side exactly as it was.

# ---- Task 3: .expandtabs() converts \t characters to spaces ----
#
# \t is the escape sequence for a TAB character — one character that tells
# the terminal "jump to the next tab stop." Tab stops are columns 0, 8, 16,
# 24, ... by default (every 8 characters). expandtabs() replaces each \t
# with however many spaces are needed to reach the next stop.
#
row = "Name\tScore\tGrade"

print("\nraw row  :", row)
print("tabs(8)  :", row.expandtabs())     # default tabsize = 8
print("tabs(4)  :", row.expandtabs(4))    # tabsize = 4

# How to read the spacing:
#   "Name" is 4 characters. The next tab stop at tabsize=8 is column 8,
#   so \t adds 4 spaces → "Name    " (8 chars total).
#   "Score" is 5 characters. Starting at column 8, the next stop is 16,
#   so \t adds 3 spaces → "Score   " (8 chars used).
#
#   With tabsize=4: "Name" ends at column 4, which IS a tab stop, so \t
#   jumps to column 8 (4 spaces added, same as before in this particular
#   case). The exact visual result depends on where each word ends relative
#   to the tab grid — run it and compare the two lines.
#
# WHY it matters: tab-separated data (spreadsheets exported as .tsv files,
# log lines, terminal output) uses \t to align columns. Without
# expandtabs(), a raw \t may render differently in different terminals.
# Converting to spaces gives you predictable, reliable alignment.


# ===========================================================================
# Problem 4 — Formatting and Replacing
# ===========================================================================
#
# .center(width) / .center(width, fillchar):
#   Pads the string with spaces (or a custom character) so the original text
#   ends up centered in a field of the given width. If the string is already
#   longer than width, it is returned unchanged.
#
# .replace(old, new) / .replace(old, new, count):
#   Returns a new string with every occurrence of old swapped for new.
#   The optional third argument limits how many replacements happen (left to
#   right). Like all string methods, .replace() does NOT modify the original.

print("\n--- Problem 4 ---")

# ---- Task 1: .center() with spaces, then with a fill character ----
#
label = "COMP 170"

# The pipe characters | are printed by us so the padding is clearly visible.
print("|" + label.center(20) + "|")       # spaces on both sides
print("|" + label.center(20, "*") + "|")  # * instead of spaces

# "COMP 170" is 8 characters. 20 - 8 = 12 characters of padding needed.
# 12 / 2 = 6 on each side.
#   |      COMP 170      |
#   |******COMP 170******|
# .center() is the standard way to build banners, table headers, and menus.

# ---- Task 2: .replace() with and without a count limit ----
#
sentence3 = "the lazy dog and the lazy cat"

# No limit — replace ALL occurrences:
print(sentence3.replace("the", "THE"))          # both "the" → "THE"

# Count = 1 — replace only the FIRST occurrence:
print(sentence3.replace("the", "THE", 1))       # only first "the" → "THE"

# The difference: without the count argument, .replace() scans the entire
# string and changes every match. With count=1, it stops after the first
# replacement. This matters when you want surgical edits — for example,
# fixing a typo only where it first appears, leaving intentional uses alone.

# ---- Task 3: Capstone — four methods in one pipeline ----
#
# This task shows what a realistic string-processing script looks like.
# In practice you rarely use a single method in isolation: you receive messy
# text, clean it, search it, measure it, and then format a report — exactly
# what the four steps below do.

raw = "   Chicago\tsummer heat   "

# Step A — clean the string
# .strip() removes leading and trailing spaces.
# .expandtabs() converts the \t between "Chicago" and "summer" to spaces.
# The two calls are chained: strip() returns a new string, and we
# immediately call expandtabs() on that result.
cleaned = raw.strip().expandtabs()
print("\nCleaned:", cleaned)           # "Chicago        summer heat"

# Step B — search: where does "summer" start in the cleaned string?
# .find() returns the index of the first character of the match.
pos_summer = cleaned.find("summer")
print("'summer' starts at index:", pos_summer)

# Step C — count: how many times does the letter "e" appear?
count_e = cleaned.count("e")
print("Count of 'e':", count_e)

# Step D — format a banner using .center()
# .center(30, "-") centers the word "REPORT" in a 30-character field,
# filling the padding with dash characters instead of spaces.
banner = "REPORT".center(30, "-")
print(banner)                          # ------------REPORT------------


# ===========================================================================
# Problem 5 — Reflection on Week 4
# ===========================================================================
#
# Q1. Problem 1 — indexing
#
#     scores[5] and scores[len(scores) - 1] produce the same value (88)
#     because the list has 6 items, so its last valid index is 6 - 1 = 5.
#     Writing scores[5] and scores[6 - 1] (= scores[5]) names the same slot.
#
#     If the list had 7 items instead:
#       scores[5]               → the SIXTH item (second-to-last), e.g. 88
#       scores[len(scores) - 1] → scores[7 - 1] = scores[6], the TRUE last item
#     They would point to different positions and could print different values.
#     The safe, general-purpose form is always scores[len(scores) - 1]
#     (or scores[-1] in Python shorthand) because it adapts to any list size.
#
# Q2. Problem 2 — total / N  vs.  total // N
#
#     Using total // N (integer division) on the temps list gives 80 instead
#     of 80.71428571428571. Integer division throws away the fractional part
#     entirely — it truncates toward zero rather than rounding. The true
#     average of those seven temperatures is ≈ 80.71, so // produces a number
#     that is simply wrong for this purpose. // is the right tool when you
#     need a whole-number result (for instance, the "quotient" part of a
#     division like "how many full rows fit?"), but averages almost always
#     need the decimal places, so / is correct here.
#
# Q3. Problem 3 — why start at temps[0] instead of 0
#
#     Initializing max_so_far = 0 works only when you know in advance that
#     every temperature is positive. Consider a list of winter readings:
#
#         temps_winter = [-15, -8, -22, -3]
#
#     Every value is below 0. With max_so_far = 0, no temperature in the list
#     is ever greater than 0, so the > condition in the loop never fires, and
#     max_so_far stays at 0. We would print 0 as the maximum — a temperature
#     that is not even in the list — instead of -3 (the correct answer).
#
#     Starting at temps[0] works for ANY list because it begins with an actual
#     value from the data. After the very first comparison, max_so_far already
#     holds a real candidate. The loop then only needs to improve on it, and
#     since every other value in the list is a real candidate too, the final
#     result is always the true maximum regardless of whether the values are
#     positive, negative, or mixed.
#
# Q4. Problem 4 — the optional average variation
#
#     Tracing through the posted solution step by step:
#
#     scores = [92, 78, 85, 90, 67, 88, 95, 72, 81, 64]
#
#     Loop 1 — compute the total (cumulative sum pattern from Problem 2):
#       total_scores = 0 + 92 + 78 + 85 + 90 + 67 + 88 + 95 + 72 + 81 + 64
#                    = 812
#       average_score = 812 / 10 = 81.2  ✓
#
#     Loop 2 — count how many scores are strictly greater than 81.2:
#       92 > 81.2? Yes  → count = 1
#       78 > 81.2? No
#       85 > 81.2? Yes  → count = 2
#       90 > 81.2? Yes  → count = 3
#       67 > 81.2? No
#       88 > 81.2? Yes  → count = 4
#       95 > 81.2? Yes  → count = 5
#       72 > 81.2? No
#       81 > 81.2? No   (81 < 81.2, so this does NOT count)
#       64 > 81.2? No
#       Final count = 5  ✓
#
#     Both numbers (81.2 and 5) are confirmed correct by hand-tracing.
#
# Q5. Your choice — one approach that differed from the posted solution
#
#     In Problem 2, a common student approach counts with range(N) and
#     adds temps[i] to the total inside the loop — matching the posted
#     solution exactly. An alternative students sometimes write is using
#     Python's built-in sum():
#
#         total = sum(temps)
#         average = total / len(temps)
#
#     Both produce the identical answer (565 and 80.714...). The range-based
#     loop is the right approach to practice at this stage of the course
#     because it makes the mechanics explicit: you can see the running total
#     accumulating one step at a time, which is the "cumulative algorithm"
#     pattern worth internalizing. sum() is a convenience that hides the
#     loop; it's fine once the underlying pattern is understood, but reaching
#     for it too early can leave the pattern unlearned.
