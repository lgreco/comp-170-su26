# A multiplication table using two nested loops.
#
# The outer loop picks a number 1 through 9 (the row); for each one,
# the inner loop runs through 1 through 9 again (the column) so every
# (row, column) pair gets visited exactly once -- 9 x 9 = 81 products
# in total.

for i in range(1, 10):
    for j in range(1, 10):
        # :5d reserves 5 character-wide columns so every product lines
        # up, no matter how many digits it has (1 vs. 81); end=""
        # keeps everything on the same line instead of starting a new
        # one after every single product.
        print(f"{i*j:5d}", end="")
    # one full row (all 9 columns) has been printed -- start a new
    # line before the outer loop moves to the next row
    print()
