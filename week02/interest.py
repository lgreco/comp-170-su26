principal = int(input("Principal amount: "))
interest_rate = float(input("Interest rate: "))
term = int(input("Term in years: "))

total = principal * (1+interest_rate) ** term

print("-----------------")
print("Principal amount:", principal)
print("   Interest rate:", interest_rate)
print("Term of maturity:", term)
print(" Compound amount:", total)
