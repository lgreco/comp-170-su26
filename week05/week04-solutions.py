# COMP 170 — Week 4 Solutions
# Topics: list indexing, len(), the cumulative algorithm (sum/average),
# tracking a running maximum, counting with a condition


# ===========================================================================
# Problem 1 — Reading a List
# ===========================================================================
#
# Prediction before running each line is written in the comment beside it.

print("--- Problem 1 ---")

scores = [92, 78, 85, 90, 67, 88]

print(scores[0])                    # 92  (first item, index 0)
print(scores[1])                    # 78
print(scores[5])                    # 88  (last item, index 5)
print(len(scores))                  # 6   (six items in the list)
print(scores[len(scores) - 1])      # 88  (len(scores)-1 = 5, same as scores[5])
print(scores[0] + scores[1])        # 170 (92 + 78)

# Q1: scores[5] and scores[len(scores) - 1] match because the list has 6
#     items, so the last valid index is 6 - 1 = 5 — the same number written
#     literally in scores[5]. If the list had 7 items instead, the last
#     index would be 6, so scores[5] would point at the SECOND-to-last
#     item while scores[len(scores) - 1] still points at the true last
#     item — they would no longer match.
#
# Q2: print(scores[6]) raises "IndexError: list index out of range".
#     The list only has valid indices 0 through 5; there is no position 6.
#
# Q3: scores[0] + scores[1] adds two integers, so the result (170) is also
#     an integer — Python does not convert it to a float just because two
#     values came out of a list.


# ===========================================================================
# Problem 2 — Sum and Average
# ===========================================================================
#
# Cumulative algorithm: start a running total at 0, add one item per loop
# pass, then divide by how many items there were.

print("\n--- Problem 2 ---")

temps = [72, 68, 85, 91, 77, 83, 89]
N = len(temps)
total = 0

for i in range(N):
    total = total + temps[i]

average = total / N
print("Total:", total)        # Total: 565
print("Average:", average)    # Average: 80.71428571428571


# ===========================================================================
# Problem 3 — Finding the Maximum
# ===========================================================================
#
# Running-maximum pattern: assume the first item is the best one seen so
# far, then update that assumption only when a larger item turns up.

print("\n--- Problem 3 ---")

temps = [72, 68, 85, 91, 77, 83, 89]
max_so_far = temps[0]

for i in range(len(temps)):
    if temps[i] > max_so_far:
        max_so_far = temps[i]

print("Highest temperature:", max_so_far)   # Highest temperature: 91

# Edge case 1 — move 91 to position 0: [91, 72, 68, 85, 77, 83, 89]
# max_so_far starts at 91 (the true max), and no later value ever exceeds
# it, so max_so_far stays 91 for the rest of the loop. Still correct.
temps_edge1 = [91, 72, 68, 85, 77, 83, 89]
max_so_far = temps_edge1[0]
for i in range(len(temps_edge1)):
    if temps_edge1[i] > max_so_far:
        max_so_far = temps_edge1[i]
print("Edge case 1 (max moved to front):", max_so_far)   # 91

# Edge case 2 — every value identical: [80, 80, 80]
# max_so_far starts at 80. The condition is strictly greater than
# (temps[i] > max_so_far), so a tie never triggers an update — max_so_far
# correctly stays 80 instead of being needlessly reassigned to another 80.
temps_edge2 = [80, 80, 80]
max_so_far = temps_edge2[0]
for i in range(len(temps_edge2)):
    if temps_edge2[i] > max_so_far:
        max_so_far = temps_edge2[i]
print("Edge case 2 (all identical):", max_so_far)   # 80


# ===========================================================================
# Problem 4 — Counting Above a Threshold (Challenge)
# ===========================================================================
#
# Counting pattern: same shape as the sum loop in Problem 2, but add 1
# (instead of the item's value) each time the condition is true.

print("\n--- Problem 4 ---")

scores = [92, 78, 85, 90, 67, 88, 95, 72, 81, 64]
count = 0

for i in range(len(scores)):
    if scores[i] >= 80:
        count = count + 1

print("Scores at or above 80:", count)   # Scores at or above 80: 6

# Variation 1 — raise the threshold to 90
count_90 = 0
for i in range(len(scores)):
    if scores[i] >= 90:
        count_90 = count_90 + 1
print("Scores at or above 90:", count_90)   # Scores at or above 90: 3

# Variation 2 — count scores BELOW 70 instead. The only change needed is
# flipping >= 80 to < 70 inside the if condition.
count_below_70 = 0
for i in range(len(scores)):
    if scores[i] < 70:
        count_below_70 = count_below_70 + 1
print("Scores below 70:", count_below_70)   # Scores below 70: 2

# Variation 3 (optional) — compute the average first (Problem 2's pattern),
# then count how many scores exceed it (Problem 4's pattern), chained
# together.
total_scores = 0
for i in range(len(scores)):
    total_scores = total_scores + scores[i]
average_score = total_scores / len(scores)   # 812 / 10 = 81.2

count_above_avg = 0
for i in range(len(scores)):
    if scores[i] > average_score:
        count_above_avg = count_above_avg + 1
print("Average score:", average_score)              # Average score: 81.2
print("Scores above average:", count_above_avg)      # Scores above average: 5


# ===========================================================================
# Problem 5 — Reflection on Week 3
# ===========================================================================
#
# Q1. Is string + also commutative?
#     No. "ab" + "cd" gives "abcd", but "cd" + "ab" gives "cdab" — two
#     different strings. Unlike * (repetition), + (concatenation) cares
#     about order: the left operand always ends up first.
#
# Q2. Rewriting the staircase loop with range(N) instead of range(1, N+1):
#     range(N) makes i take the values 0, 1, 2, 3, 4 instead of 1..5.
#     To produce the same output, the loop body must add 1 everywhere the
#     step number is used:
#         for i in range(N):
#             print(i + 1, '*' * (i + 1))
#
# Q3. Why Problem 2 could use a comma but Problem 3 needed +:
#     print(i, '*' * i) hands print() two separate arguments (a number and
#     a string); print() automatically inserts one space between
#     arguments, which is exactly the "step number, then stars" look we
#     want. Problem 3 builds a single string where the spaces must sit
#     directly against the stars with no gap, so the two pieces have to be
#     glued with + before printing.
#     If Problem 3 used a comma instead — print(' ' * (N-i), '*' * i) —
#     print() would insert one extra space between the leading spaces and
#     the stars on every row. Because that extra space is the same on
#     every row, the triangle would still be right-aligned; it would just
#     be shifted one column further to the right than the + version.
#
# Q4. Tracing ' ' * (N - i) + '*' * i with N = 5:
#     i = 1: ' ' * 4 + '*' * 1 = '    *'      (4 spaces + 1 star = 5 chars)
#     i = 5: ' ' * 0 + '*' * 5 = '*****'      (0 spaces + 5 stars = 5 chars)
#     The total character count is (N - i) + i = N on every row, regardless
#     of i. That's exactly why the triangle's right edge lines up across
#     all rows — every row is the same total width, just with a different
#     space/star split.
#
# Q5. Rounding vs. truncating, r = 8, y = -2:
#     y_scaled = -4, so x_max = sqrt(64 - 16) = sqrt(48) ≈ 6.928.
#     int(6.928 + 0.5) = int(7.428) = 7  ->  2*7 + 1 = 15 stars
#     int(6.928)        = 6              ->  2*6 + 1 = 13 stars
#     Truncating (no + 0.5) always rounds down, so every row that should
#     round up comes out two stars narrower than it should — the circle
#     would look consistently flattened/undersized rather than smoothly
#     round.
