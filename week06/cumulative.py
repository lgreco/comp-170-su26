# Some data to process

daily_temps = [ 70, 71, 68, 73, 73, 78, 82 ]

# Function to compute average

# The parameter is named "data", not "daily_temps", on purpose: a function
# is written once but can be called on *any* list a caller passes in. Inside
# the function we only know it as "data" -- a generic name for "whatever
# list got passed here". The caller decides what real-world list that is
# (here, daily_temps) when it calls arithmetic_average(daily_temps). This is
# parameter naming abstraction: the function's logic shouldn't be tied to
# one specific variable name from the rest of the program.
def arithmetic_average(data):
    # running total, built up one value at a time (the cumulative pattern)
    sum = 0
    # value is the loop's own name for "the current item from data";
    # it's local to this loop, just like data is local to this function
    for value in data:
        sum = sum + value
    # arithmetic mean: sum of all values divided by how many values there are
    return sum / len(data)

def geometric_average(data):
    # running product, built up one value at a time -- same cumulative
    # pattern as above, but multiplying instead of adding
    product = 1
    for value in data:
        product = product * value
    # geometric mean: the nth root of the product of n values
    return product ** (1 / len(data))
