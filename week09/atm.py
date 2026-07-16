def withdraw(amount, balance):
    new_balance = balance
    # guard clause: ATMs only dispense $20 bills, so anything that isn't
    # a multiple of $20 is invalid before we even look at balance
    if amount % 20 != 0:
        raise ValueError("not 20")
    # guard clause: can't withdraw money that isn't there
    elif amount > balance:
        raise ValueError("not enough")
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
    tries = 0
    succeeded = False
    while tries < max_tries:
        tries = tries + 1
        try:
            amount = int(input("How much you wish to withdraw? "))
            balance = withdraw(amount, balance)
            print("Success")
            succeeded = True
            break
        except ValueError as message:
            print(f"Something's wrong: {message}")
            print("Try again")
    if not succeeded:
        print("Sorry, you're out of tries. Please visit a teller.")
    return balance


def main():
    print("--- Problem 1 ---")
    balance = 1000
    attempt_withdrawal(balance)


if __name__ == "__main__":
    main()
