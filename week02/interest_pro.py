# Compound interest calculator — refactored from a single block into three methods.
# A method is a named, reusable block of code that performs a specific task.
# Each method owns exactly one responsibility: compute, read, or display.
# This is called separation of concerns; it keeps each piece easy to read, test, and change.

def compute_future_value(principal, interest_rate, term):
  # Standard compound interest formula: the principal grows by a factor of
  # (1 + rate) each year, applied 'term' times via exponentiation.
  # This method only does math — it never asks for input or prints anything.
  total = principal * (1 + interest_rate) ** term
  # return sends the computed value back to the caller without printing it.
  # The caller (main program or another method) decides what to do with it.
  return total

def read_inputs():
  # Isolating input here means if we ever want to read from a file or a GUI
  # instead of the keyboard, this is the only method we need to change.
  principal = int(input("Principal amount: "))
  interest_rate = float(input("Interest rate: "))
  term = int(input("Term in years: "))
  # return can send back multiple values at once as a tuple.
  # The caller can unpack them into separate variables: p, r, t = read_inputs()
  return principal, interest_rate, term

def show_results(total, principal, interest_rate, term):
  # All formatting decisions live here so compute_future_value stays pure math.
  print("-----------------")
  print("Principal amount:", principal)
  print("   Interest rate:", interest_rate)
  print("Term of maturity:", term)
  print(" Compound amount:", total)


# The main program collapses to three calls — one per concern.
# Think of each method like ordering a drink: you name it and trust the barista.
p, r, t = read_inputs()
tot = compute_future_value(p, r, t)
show_results(tot, p, r, t)
