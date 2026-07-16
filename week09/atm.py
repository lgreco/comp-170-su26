def withdraw(amount, balance):
    # start from the assumption that nothing changes; new_balance only
    # gets overwritten once we know the withdrawal is actually valid
    new_balance = balance
    # guard clause: ATMs only dispense $20 bills, so anything that isn't
    # a multiple of $20 is invalid before we even look at balance
    if amount % 20 != 0:
        raise ValueError("not 20")
    # guard clause: can't withdraw money that isn't there. This has to
    # be elif, not a second separate `if`: with two separate ifs,
    # nothing would stop the code from falling through to the `else`
    # below and attempting the withdrawal even after the first check
    # already printed/raised an error. elif (and the else that follows
    # it) guarantees exactly one of these three branches runs, never
    # more than one.
    elif amount > balance:
        raise ValueError("not enough")
    # both guard clauses passed -- this is the only branch that
    # actually changes new_balance
    else:
        new_balance = balance - amount
    return new_balance


def attempt_withdrawal(balance, max_tries=5):
    """Ask for a withdrawal amount, retrying on bad input.

    Keeps asking up to max_tries times, so a user who never enters
    something valid doesn't get stuck in a loop forever. Each attempt
    is wrapped in a try/except that catches two different problems at
    once: int() failing on non-numeric text, and withdraw() raising a
    ValueError because the amount is invalid. If every try fails, we
    give up gently instead of crashing or looping forever.
    """
    # tries counts attempts so far; succeeded records whether one of
    # them actually worked, since the loop can end two different ways
    # (a successful withdrawal, or running out of tries)
    tries = 0
    succeeded = False
    while tries < max_tries:
        tries = tries + 1
        try:
            # int(input(...)) lives inside the try along with
            # withdraw() itself, because it can raise its own
            # ValueError (e.g. someone types "fifty") -- one except
            # below catches either failure, whichever line caused it
            amount = int(input("How much you wish to withdraw? "))
            balance = withdraw(amount, balance)
            print("Success")
            succeeded = True
            # stop asking -- the loop's job is done as soon as one
            # attempt works
            break
        except ValueError as message:
            # withdraw() never crashes the program; the raise is
            # caught right here, its message printed, and the loop
            # goes around again instead of stopping
            print(f"Something's wrong: {message}")
            print("Try again")
    # the loop can only exit two ways: succeeded became True (break),
    # or tries reached max_tries with every attempt failing
    if not succeeded:
        print("Sorry, you're out of tries. Please visit a teller.")
    return balance


def main():
    print("--- Problem 1 ---")
    balance = 1000
    attempt_withdrawal(balance)


if __name__ == "__main__":
    main()
