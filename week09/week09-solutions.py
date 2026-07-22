# COMP 170 — Week 9 Solutions
# Topics: raise + try/except retry loops, multi-branch guard clauses,
# cash vs. cheque deposit rules

# Same teaching note as atm.py: these functions raise a ValueError on
# invalid input instead of printing and returning unchanged, because a
# raise is what a try/except retry loop needs to catch. Compare this to
# Week 8's withdraw()/deposit(), which printed instead of raising.


# ===========================================================================
# Problem 1 — Withdrawals with Limited Retries
# ===========================================================================
#
# withdraw() enforces the same two rules as Week 8, in the same order
# (the $20-multiple check doesn't depend on balance, so it goes first),
# but raises instead of printing. Because it raises, it never reaches a
# point where new_balance is returned unchanged — either both guard
# clauses pass and the function returns the new balance, or one of them
# raises and the function never returns at all. attempt_withdrawal()
# wraps a single call to withdraw() in a try/except inside a
# tries-counted loop: every raised ValueError is caught, reported, and
# followed by another chance, until either a withdrawal succeeds or
# max_tries is used up.

print("--- Problem 1 ---")


def withdraw(amount, balance):
    # guard clause: ATMs only dispense $20 bills, so anything that
    # isn't a multiple of $20 is invalid before we even look at balance
    if amount % 20 != 0:
        raise ValueError("amount must be a multiple of $20")
    # guard clause: can't withdraw money that isn't there
    if amount > balance:
        raise ValueError("withdrawal amount exceeds balance")
    # both checks passed
    return balance - amount


def attempt_withdrawal(balance, max_tries=3):
    tries = 0
    succeeded = False
    while tries < max_tries and not succeeded:
        tries = tries + 1
        try:
            amount = int(input("How much would you like to withdraw? "))
            balance = withdraw(amount, balance)
            print("Success! New balance:", balance)
            succeeded = True
        except ValueError as error:
            print("Something's wrong:", error)
            print("Try again.")
    if not succeeded:
        print("Sorry, you're out of tries.")
    return balance


# ===========================================================================
# Problem 2 — Cash vs. Cheque Deposits
# ===========================================================================
#
# deposit() takes on a third parameter, method, and checks it alongside
# amount. Order of checks: amount > 0 first (true regardless of
# method), then method itself (a bad method makes the remaining
# amount-shape checks meaningless), then the amount-shape check that
# depends on which method it is -- whole dollars only for cash, up to
# two decimal digits for cheque. The $10,000 warning is not a raise: a
# warning does not stop the deposit from happening, so it belongs after
# every guard clause has already passed, printed with a plain print()
# rather than raised.

print("\n--- Problem 2 ---")


def deposit(amount, balance, method):
    # guard clause: can't deposit nothing or a negative amount
    if amount <= 0:
        raise ValueError("deposit amount must be greater than $0")
    # guard clause: method must be one of the two the ATM understands
    if method not in ("cash", "cheque"):
        raise ValueError("method must be 'cash' or 'cheque'")
    # guard clause: cash can't include cents -- you can't hand an ATM
    # a fraction of a dollar bill the way you can write one on a cheque
    if method == "cash" and amount != int(amount):
        raise ValueError("cash deposits cannot include cents")
    # guard clause: cheques may include cents, but still only down to
    # the cent -- same round(amount * 100) trick as Week 8
    if method == "cheque" and round(amount * 100) != amount * 100:
        raise ValueError("cheque amount must be valid dollars and cents")
    # every guard clause passed -- not an error, so a plain print(),
    # and the deposit still goes through either way
    if amount >= 10000:
        print("Warning: deposits of $10,000 or more are reported to the IRS")
    return balance + amount


def attempt_deposit(balance, max_tries=3):
    tries = 0
    succeeded = False
    while tries < max_tries and not succeeded:
        tries = tries + 1
        try:
            method = input("Deposit method (cash/cheque)? ")
            amount = float(input("How much would you like to deposit? "))
            balance = deposit(amount, balance, method)
            print("Success! New balance:", balance)
            succeeded = True
        except ValueError as error:
            print("Something's wrong:", error)
            print("Try again.")
    if not succeeded:
        print("Sorry, you're out of tries.")
    return balance


def main():
    balance = 200
    balance = attempt_withdrawal(balance)
    balance = attempt_deposit(balance)


if __name__ == "__main__":
    main()
