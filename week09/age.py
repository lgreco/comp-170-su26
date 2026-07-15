def get_year():
    while True:
        try:
            return int(input("Year born? "))
        except ValueError: # add logic to enforce 1901 < input < 2025 and no more than 10 trials
            print("Please enter something reasonable.")

def main():
    year = get_year()
    print(f"You are {2026-year} years old")

if __name__ == "__main__":
    main()
