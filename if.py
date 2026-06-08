
n = int(input("Give me a positive integer number. "))

remainder_after_divide_by_2 = n - 2 * (n // 2)

if remainder_after_divide_by_2 == 0:
    print("The number is even")
else:
    print("The number is odd")
