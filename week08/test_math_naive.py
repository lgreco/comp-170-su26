import math

from mathemagics import solve_quadratic

# Test 1: a = 0, b = 0, c = 0 -> no equation, expect (NaN, NaN)
x1, x2 = solve_quadratic(0, 0, 0)
if math.isnan(x1) and math.isnan(x2):
    print("PASS: a=0, b=0, c=0 -> (NaN, NaN)")
else:
    print("FAIL: a=0, b=0, c=0 -> expected (NaN, NaN), got", (x1, x2))

# Test 2: a = 0, b = 0, c = 5 -> contradiction, expect (NaN, NaN)
x1, x2 = solve_quadratic(0, 0, 5)
if math.isnan(x1) and math.isnan(x2):
    print("PASS: a=0, b=0, c=5 -> (NaN, NaN)")
else:
    print("FAIL: a=0, b=0, c=5 -> expected (NaN, NaN), got", (x1, x2))

# Test 3: a = 0, linear equation, 2x + 4 = 0 -> x = -2
x1, x2 = solve_quadratic(0, 2, 4)
if abs(x1 - (-2)) < 1e-9 and abs(x2 - (-2)) < 1e-9:
    print("PASS: 2x + 4 = 0 -> x1 = x2 = -2")
else:
    print("FAIL: 2x + 4 = 0 -> expected (-2, -2), got", (x1, x2))

# Test 4: a = 0, linear equation, 3x - 9 = 0 -> x = 3
x1, x2 = solve_quadratic(0, 3, -9)
if abs(x1 - 3) < 1e-9 and abs(x2 - 3) < 1e-9:
    print("PASS: 3x - 9 = 0 -> x1 = x2 = 3")
else:
    print("FAIL: 3x - 9 = 0 -> expected (3, 3), got", (x1, x2))

# Test 5: trivial quadratic, x^2 = 0 -> x = 0, 0
x1, x2 = solve_quadratic(1, 0, 0)
if abs(x1 - 0) < 1e-9 and abs(x2 - 0) < 1e-9:
    print("PASS: x^2 = 0 -> x1 = x2 = 0")
else:
    print("FAIL: x^2 = 0 -> expected (0, 0), got", (x1, x2))

# Test 6: b = 0, real roots, x^2 - 4 = 0 -> x = 2, -2
x1, x2 = solve_quadratic(1, 0, -4)
if abs(x1 - 2) < 1e-9 and abs(x2 - (-2)) < 1e-9:
    print("PASS: x^2 - 4 = 0 -> x1 = 2, x2 = -2")
else:
    print("FAIL: x^2 - 4 = 0 -> expected (2, -2), got", (x1, x2))

# Test 7: b = 0, complex roots, x^2 + 4 = 0 -> x = 2i, -2i
x1, x2 = solve_quadratic(1, 0, 4)
if (abs(x1[0] - 0) < 1e-9 and abs(x1[1] - 2) < 1e-9
        and abs(x2[0] - 0) < 1e-9 and abs(x2[1] - (-2)) < 1e-9):
    print("PASS: x^2 + 4 = 0 -> x1 = (0, 2), x2 = (0, -2)")
else:
    print("FAIL: x^2 + 4 = 0 -> expected ((0, 2), (0, -2)), got", (x1, x2))

# Test 8: two distinct real roots, x^2 - 3x + 2 = 0 -> x = 2, 1
x1, x2 = solve_quadratic(1, -3, 2)
if abs(x1 - 2) < 1e-9 and abs(x2 - 1) < 1e-9:
    print("PASS: x^2 - 3x + 2 = 0 -> x1 = 2, x2 = 1")
else:
    print("FAIL: x^2 - 3x + 2 = 0 -> expected (2, 1), got", (x1, x2))

# Test 9: repeated real root, x^2 + 2x + 1 = 0 -> x = -1, -1
x1, x2 = solve_quadratic(1, 2, 1)
if abs(x1 - (-1)) < 1e-9 and abs(x2 - (-1)) < 1e-9:
    print("PASS: x^2 + 2x + 1 = 0 -> x1 = x2 = -1")
else:
    print("FAIL: x^2 + 2x + 1 = 0 -> expected (-1, -1), got", (x1, x2))

# Test 10: complex roots with nonzero real part, x^2 + 2x + 5 = 0 -> x = -1 + 2i, -1 - 2i
x1, x2 = solve_quadratic(1, 2, 5)
if (abs(x1[0] - (-1)) < 1e-9 and abs(x1[1] - 2) < 1e-9
        and abs(x2[0] - (-1)) < 1e-9 and abs(x2[1] - (-2)) < 1e-9):
    print("PASS: x^2 + 2x + 5 = 0 -> x1 = (-1, 2), x2 = (-1, -2)")
else:
    print("FAIL: x^2 + 2x + 5 = 0 -> expected ((-1, 2), (-1, -2)), got", (x1, x2))

# Test 11: negative a, -x^2 + 3x - 2 = 0 -> x = 1, 2 (order may vary)
x1, x2 = solve_quadratic(-1, 3, -2)
low = min(x1, x2)
high = max(x1, x2)
if abs(low - 1) < 1e-9 and abs(high - 2) < 1e-9:
    print("PASS: -x^2 + 3x - 2 = 0 -> roots are 1 and 2")
else:
    print("FAIL: -x^2 + 3x - 2 = 0 -> expected roots 1 and 2, got", (x1, x2))
