def compute_future_value(principal, interest_rate, term):
  total = principal * (1 + interest_rate) ** term
  return total

def read_inputs():
  # good comment
   # good comment
    # good comment
# good comment
  principal = int(input("Principal amount: "))
  interest_rate = float(input("Interest rate: "))
  term = int(input("Term in years: "))
  return principal, interest_rate, term

def show_results(total, principal, interest_rate, term):
  print("-----------------")
  print("Principal amount:", principal)
  print("   Interest rate:", interest_rate)
  print("Term of maturity:", term)
  print(" Compound amount:", total)


p, r, t = read_inputs()
tot = compute_future_value(p, r, t)
show_results(tot, p, r, t)


