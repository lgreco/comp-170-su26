principal = int(input("Principal amount: "))
interest_rate = float(input("Interest rate: "))
term = int(input("Term in years: "))

total = principal * (1+interest_rate) ** term

print("A principal of ", principal, " at ", interest_rate, " after ", term, "years yields ", total)

# Nice formatting

print(f"A principal of ${principal:,d} at {100*interest_rate:.2f}% yields after {term} years, yields ${total:,.2f}")
