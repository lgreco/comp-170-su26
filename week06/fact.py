def brute_force_factorial(n):
    product = 1
    for i in range(1, n+1):
        product = product * i
    return product

def basic_factorial(n):
    result = 1
    if n > 0:
        result = result * basic_factorial(n-1)
    return result

