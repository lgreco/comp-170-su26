def brute_force_factorial(n):
    # start at 1, since multiplying by 1 doesn't change the running product
    product = 1
    # multiply product by every whole number from 1 up to and including n
    for i in range(1, n+1):
        product = product * i
    return product

def basic_factorial(n):
    # base case: 0! is defined as 1, so when n is 0 we just return result unchanged
    result = 1
    if n > 0:
        # recursive case: n! = n * (n-1)!, so call this same function on n-1
        result = n * basic_factorial(n-1)
    return result

