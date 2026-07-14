# COMP 170 — Week 8 Solutions
# Topics: guard clauses with if statements, bank withdrawal/deposit,
# testing functions that report errors by printing, reflection on
# Week 7 solutions


# ===========================================================================
# Problem 1 — Bank Withdrawal
# ===========================================================================
#
# Inputs: amount (how much cash to withdraw), balance (what's in the
#         account right now)
# Output: the updated balance after the withdrawal is deducted
#
# Two ways amount can be invalid, checked in this order:
#   1. amount is not a multiple of $20 — this is invalid on its own,
#      no matter what balance is, since a real ATM can't dispense it.
#   2. amount is more than balance — this can only be checked once we
#      already know amount is a "real" withdrawal amount, which is why
#      it comes second.
# Each invalid case prints an error message and reports balance
# unchanged, instead of crashing the program. new_balance starts out
# equal to balance and is only changed once both checks pass, so
# there is exactly one return statement, at the very end.
#
# NOTE: in general, a function that returns a value should not also
# print — printing is the caller's job, since a function that prints
# internally can't be reused somewhere the message isn't wanted (or is
# wanted in a different form). We break that rule here on purpose, so
# the error/warning text shows up automatically wherever these
# functions are called, without every call site having to check the
# result and print its own message. Treat this as a teaching shortcut,
# not a pattern to copy in general.

print("--- Problem 1 ---")


def withdraw(amount, balance):
    new_balance = balance
    # guard clause: ATMs only dispense $20 bills, so anything that isn't
    # a multiple of $20 is invalid before we even look at balance
    if amount % 20 != 0:
        print("Error: amount must be a multiple of $20")
    # guard clause: can't withdraw money that isn't there
    elif amount > balance:
        print("Error: withdrawal amount exceeds balance")
    # both checks passed — deduct amount from the new balance
    else:
        new_balance = balance - amount
    return new_balance


print(withdraw(60, 200))    # 140
print(withdraw(50, 200))    # prints error, then 200 (balance unchanged)
print(withdraw(300, 200))   # prints error, then 200 (balance unchanged)


# ===========================================================================
# Problem 2 — Bank Deposit
# ===========================================================================
#
# Inputs: amount (how much cash to deposit), balance (what's in the
#         account right now)
# Output: the updated balance after the deposit is added
#
# Two ways amount can be invalid, checked in this order:
#   1. amount is not greater than $0 — a deposit of nothing (or less
#      than nothing) never makes sense, regardless of anything else.
#   2. amount has more than two decimal digits — there's no such thing
#      as a third of a cent, so anything finer than cents is invalid.
# Each invalid case prints an error message and reports balance
# unchanged. If both checks pass, amount >= $10,000 prints a separate
# warning (the deposit still goes through) before the deposit is
# added. new_balance starts out equal to balance and is only changed
# once both checks pass, so there is exactly one return statement,
# at the very end.
#
# NOTE: same exception as in Problem 1 above — a function that returns
# a value normally shouldn't also print. We do it here only so the
# error/warning message appears automatically at every call site,
# for illustrative purposes.

print("\n--- Problem 2 ---")


def deposit(amount, balance):
    new_balance = balance
    # guard clause: can't deposit nothing or a negative amount
    if amount <= 0:
        print("Error: deposit amount must be greater than $0")
    # guard clause: amount must be valid dollars and cents only.
    # Multiplying by 100 turns a valid amount into a whole number of
    # cents; round() undoes tiny floating-point error, and comparing
    # against the un-rounded value catches anything with a fractional
    # cent, like 42.503.
    elif round(amount * 100) != amount * 100:
        print("Error: deposit amount must be valid dollars and cents")
    # both checks passed — add amount to the new balance
    else:
        # not an error — the deposit still happens, just with a warning
        if amount >= 10000:
            print("Warning: deposits of $10,000 or more are reported to the IRS")
        new_balance = balance + amount
    return new_balance


print(deposit(150, 200))     # 350
print(deposit(12000, 200))   # prints warning, then 12200
print(deposit(-50, 200))     # prints error, then 200 (balance unchanged)
print(deposit(42.503, 200))  # prints error, then 200 (balance unchanged)


# ===========================================================================
# Problem 3 — Testing withdraw() and deposit()
# ===========================================================================
#
# Naive if/else style: call the function, then compare the actual
# result against what was expected and print PASS or FAIL. No
# try/except is needed here — withdraw() and deposit() never crash,
# they print their own error message and return the unchanged balance,
# so an invalid case is checked the same way a valid one is: by
# looking at the returned balance.

print("\n--- Problem 3 ---")

print("Testing withdraw():")

# 1. A normal, valid withdrawal
result = withdraw(60, 200)
if result == 140:
    print("PASS: withdraw(60, 200) ->", result)
else:
    print("FAIL: withdraw(60, 200) ->", result, "expected 140")

# 2. A withdrawal that exactly empties the balance
result = withdraw(200, 200)
if result == 0:
    print("PASS: withdraw(200, 200) ->", result)
else:
    print("FAIL: withdraw(200, 200) ->", result, "expected 0")

# 3. An amount that is not a multiple of $20 — expect an error message
#    above and balance returned unchanged
result = withdraw(50, 200)
if result == 200:
    print("PASS: withdraw(50, 200) correctly left balance unchanged")
else:
    print("FAIL: withdraw(50, 200) ->", result, "expected 200")

# 4. An amount greater than balance — expect an error message above
#    and balance returned unchanged
result = withdraw(300, 200)
if result == 200:
    print("PASS: withdraw(300, 200) correctly left balance unchanged")
else:
    print("FAIL: withdraw(300, 200) ->", result, "expected 200")

# 5. Edge case: amount is $0, a multiple of $20 that withdraws nothing
result = withdraw(0, 200)
if result == 200:
    print("PASS: withdraw(0, 200) ->", result)
else:
    print("FAIL: withdraw(0, 200) ->", result, "expected 200")

print("\nTesting deposit():")

# 1. A normal, valid deposit
result = deposit(150, 200)
if result == 350:
    print("PASS: deposit(150, 200) ->", result)
else:
    print("FAIL: deposit(150, 200) ->", result, "expected 350")

# 2. An amount that is not valid dollars and cents (or <= 0) — expect
#    an error message above and balance returned unchanged
result = deposit(42.503, 200)
if result == 200:
    print("PASS: deposit(42.503, 200) correctly left balance unchanged")
else:
    print("FAIL: deposit(42.503, 200) ->", result, "expected 200")

# 3. An amount of $10,000 or more — warning prints AND deposit succeeds
result = deposit(12000, 200)
if result == 12200:
    print("PASS: deposit(12000, 200) ->", result, "(warning should appear above)")
else:
    print("FAIL: deposit(12000, 200) ->", result, "expected 12200")


# ===========================================================================
# Problem 4 — Reflection on Week 7 Solutions
# ===========================================================================
#
# Q1. Not stopping early
#
#     positions() keeps scanning all the way to the end of the string
#     even after it finds a match, because it needs every position, not
#     just the first. My own pseudocode for finding the first occurrence
#     did stop immediately on a match — the difference here is that the
#     loop condition can never depend on "found yet," since finding one
#     match is not a reason to quit.
#
# Q2. The match flag in find_substring
#
#     Flipping match to False the instant one character fails to compare
#     saves work because there's no point checking the rest of target
#     once a single letter is already wrong — that starting position is
#     already ruled out, so the inner loop can stop and move the outer
#     loop to the next starting position instead of wasting comparisons.
#
# Q3. One return, at the end
#
#     My own pseudocode returned as soon as a match was found in the
#     middle of the function. It still produces the correct answer —
#     returning early and using a found flag to fall through to one
#     final return are logically equivalent — but the found-flag version
#     keeps all the "how did this loop end" logic in one place, at the
#     bottom, instead of scattered across multiple return statements.
#
# Q4. Connecting to this week
#
#     withdraw() and deposit() report an invalid case by printing an
#     error message and returning the balance unchanged, rather than
#     returning a sentinel like -1. That matters because balance is a
#     dollar amount, and a returned -1 could easily be mistaken for a
#     real (if odd) balance instead of a signal that something went
#     wrong. -1 worked fine as a sentinel for find_substring() because
#     positions are never negative, so -1 can never be confused with a
#     real answer — that isn't true here, since -1 dollars could look
#     like a legitimate, if unusual, balance.
#
# Q5. Your choice
#
#     My pseudocode for find_substring compared the whole target using
#     slicing (text[start:start+len(target)] == target) instead of a
#     character-by-character inner loop with a match flag. The posted
#     solution's version surprised me by being more explicit about
#     exactly where a mismatch happens, which makes it easier to see why
#     the inner loop can stop early — my slicing version hides that
#     detail inside Python's own string comparison.
