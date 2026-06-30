
i = 0
while i < 1_000_000_000:
    # print(i)
    if (i % 10_000) == 0:
        print(".", end="")
    i = i + 1
