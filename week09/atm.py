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
    if amount % 20 != 0:
        raise ValueError("not 20")
    elif amount > balance:
        raise ValueError("not enough")
    else: 
        new_balance = balance - amount
    return new_balance


tries = 0

while True and tries < 5:
    tries = tries + 1
    try:
        amount = int(input("How much you wish to withdraw? "))
        balance = withdraw(amount, 1000)
        print("Success")
        break
    except ValueError as message:
        print(f"Something's wrong: {message}")
        print("Try again")
