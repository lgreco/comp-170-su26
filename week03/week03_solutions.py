# COMP 170 — Week 3 Solutions
# Topics: string repetition, for loops, range(), shapes, import math

import math   # needed only for Problem 4; Python won't use it until then


# ===========================================================================
# Problem 1 — Predicting String Repetition
# ===========================================================================
#
# The * operator on a string means REPEAT, not multiply.
# 'ha' * 3  ->  'hahaha'   (the string 'ha' printed 3 times in a row)
#
# Prediction before running each line is written in the comment beside it.

print("--- Problem 1 ---")

print('*' * 1)                          # *
print('*' * 5)                          # *****
print('*' * 0)                          # (empty string — zero repetitions)
print('-' * 20)                         # --------------------
print('ha' * 4)                         # hahahaha
print('Na' * 8 + ' Batman!')            # NaNaNaNaNaNaNaNa Batman!
print(3 * 'ab')                         # ababab  (number can go on either side)
print('=' * 10 + ' SCORE ' + '=' * 10) # ========== SCORE ==========

# Q1: '*' * 0  produces an empty string. Zero repetitions of anything is nothing.
# Q2: Python evaluates * before +, so both '='*10 blocks are built first,
#     then joined with ' SCORE ' by the two + operators.
# Q3: 3 * 'ab' and 'ab' * 3 always give the same result.
#     The order of operands never matters for string repetition.


# ===========================================================================
# Problem 2 — Drawing a Staircase
# ===========================================================================
#
# Pseudocode:
#   choose how many steps N
#   for each number i from 1 to N:
#       print i, then a space, then '*' repeated i times
#
# range(1, N+1) gives the sequence 1, 2, 3, ... N.
# Without the +1 the loop would stop one step too early (range stops
# *before* its second argument, so range(1, N) would end at N-1).

print("\n--- Problem 2 ---")

N = 5

for i in range(1, N + 1):
    # print(i, ...) automatically inserts a space between its arguments,
    # so we get the step label and the stars separated without extra work.
    print(i, '*' * i)


# ===========================================================================
# Problem 3 — Right-Aligned Triangle
# ===========================================================================
#
# Each row i needs:
#   (N - i) leading spaces   ← gets smaller as i grows
#   i stars                  ← gets larger as i grows
#
# The two strings are joined with + before printing, so there is no gap
# between the spaces and the stars.
#
# Row  i   spaces (N-i)   stars (i)
# ---  --  ------------   ---------
#  1    1       4             1
#  2    2       3             2
#  3    3       2             3
#  4    4       1             4
#  5    5       0             5

print("\n--- Problem 3 ---")

N = 5

for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)


# ===========================================================================
# Problem 4 — A Filled Circle  (Challenge)
# ===========================================================================
#
# A circle of radius r satisfies  x² + y² = r².
# Any point where x² + y² ≤ r² is inside the circle.
#
# For each row (each value of y), the widest x still inside the circle is:
#     x_max = sqrt(r² - y²)
# That row then prints  2*x_max + 1  stars, centered with leading spaces.
#
# Two adjustments are needed to make it look right in a terminal:
#
# 1. DISCRETIZATION: the terminal is a grid of whole-number positions, so
#    x_max must be rounded to an integer.  int(x_max + 0.5) rounds to nearest.
#
# 2. ASPECT RATIO: a terminal character is roughly twice as tall as it is wide.
#    Looping y from -r to r produces 2r+1 rows, which looks like a tall oval.
#    Fix: loop y over a compressed range (-r//2 to r//2) and scale it back up
#    by 2 before plugging into the formula.  This halves the row count while
#    keeping the width the same, so the shape looks roughly circular.

print("\n--- Problem 4 ---")

r = 8

for y in range(-r // 2, r // 2 + 1):
    y_scaled = y * 2                                    # undo vertical compression
    x_max = int(math.sqrt(r * r - y_scaled * y_scaled) + 0.5)
    print(' ' * (r - x_max) + '*' * (2 * x_max + 1))
