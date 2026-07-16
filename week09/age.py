def get_year(max_tries=10):
    """Ask for a birth year, retrying on bad or unreasonable input.

    Keeps asking until int() succeeds and the result falls in a
    believable range, or until max_tries attempts are used up.
    """
    tries = 0
    while tries < max_tries:
        tries = tries + 1
        try:
            # int() itself raises ValueError on non-numeric text, e.g.
            # "196Y" or a Roman numeral
            year = int(input("Year born? "))
            # a number that converts cleanly can still be unreasonable
            if year < 1901 or year > 2025:
                raise ValueError("year must be between 1901 and 2025")
            return year
        except ValueError:
            print("Please enter something reasonable.")
    # every try failed -- give up gently instead of looping forever
    print("Sorry, you're out of tries.")
    return None


def main():
    year = get_year()
    if year is not None:
        print(f"You are {2026 - year} years old")


if __name__ == "__main__":
    main()
