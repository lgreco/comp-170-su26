import math

from mathemagics import solve_quadratic


def check(description: str, actual, expected) -> None:
    """Compare actual and expected values, printing PASS or FAIL."""
    if actual == expected:
        print(f"PASS: {description}")
    else:
        print(f"FAIL: {description} -- expected {expected}, got {actual}")


def close_enough(a: float, b: float, tolerance: float = 1e-9) -> bool:
    """Return True if two floats are close enough to be considered equal."""
    return abs(a - b) < tolerance


def check_close(description: str, actual: float, expected: float) -> None:
    """Compare actual and expected floats within a small tolerance."""
    if close_enough(actual, expected):
        print(f"PASS: {description}")
    else:
        print(f"FAIL: {description} -- expected {expected}, got {actual}")


def test_a_zero_b_zero_c_zero():
    x1, x2 = solve_quadratic(0, 0, 0)
    check("a=0, b=0, c=0 -> x1 is NaN", math.isnan(x1), True)
    check("a=0, b=0, c=0 -> x2 is NaN", math.isnan(x2), True)


def test_a_zero_b_zero_c_nonzero():
    x1, x2 = solve_quadratic(0, 0, 5)
    check("a=0, b=0, c=5 -> x1 is NaN", math.isnan(x1), True)
    check("a=0, b=0, c=5 -> x2 is NaN", math.isnan(x2), True)


def test_a_zero_linear_equation():
    # 2x + 4 = 0 -> x = -2
    x1, x2 = solve_quadratic(0, 2, 4)
    check_close("2x + 4 = 0 -> x1 = -2", x1, -2)
    check_close("2x + 4 = 0 -> x2 = -2", x2, -2)


def test_a_zero_linear_equation_negative_c():
    # 3x - 9 = 0 -> x = 3
    x1, x2 = solve_quadratic(0, 3, -9)
    check_close("3x - 9 = 0 -> x1 = 3", x1, 3)
    check_close("3x - 9 = 0 -> x2 = 3", x2, 3)


def test_trivial_quadratic():
    # x^2 = 0 -> x = 0, 0
    x1, x2 = solve_quadratic(1, 0, 0)
    check_close("x^2 = 0 -> x1 = 0", x1, 0)
    check_close("x^2 = 0 -> x2 = 0", x2, 0)


def test_b_zero_real_roots():
    # x^2 - 4 = 0 -> x = 2, -2
    x1, x2 = solve_quadratic(1, 0, -4)
    check_close("x^2 - 4 = 0 -> x1 = 2", x1, 2)
    check_close("x^2 - 4 = 0 -> x2 = -2", x2, -2)


def test_b_zero_complex_roots():
    # x^2 + 4 = 0 -> x = 2i, -2i
    x1, x2 = solve_quadratic(1, 0, 4)
    check_close("x^2 + 4 = 0 -> x1 real part = 0", x1[0], 0)
    check_close("x^2 + 4 = 0 -> x1 imaginary part = 2", x1[1], 2)
    check_close("x^2 + 4 = 0 -> x2 real part = 0", x2[0], 0)
    check_close("x^2 + 4 = 0 -> x2 imaginary part = -2", x2[1], -2)


def test_two_distinct_real_roots():
    # x^2 - 3x + 2 = 0 -> x = 2, 1
    x1, x2 = solve_quadratic(1, -3, 2)
    check_close("x^2 - 3x + 2 = 0 -> x1 = 2", x1, 2)
    check_close("x^2 - 3x + 2 = 0 -> x2 = 1", x2, 1)


def test_repeated_real_root():
    # x^2 + 2x + 1 = 0 -> x = -1, -1
    x1, x2 = solve_quadratic(1, 2, 1)
    check_close("x^2 + 2x + 1 = 0 -> x1 = -1", x1, -1)
    check_close("x^2 + 2x + 1 = 0 -> x2 = -1", x2, -1)


def test_complex_roots_with_nonzero_real_part():
    # x^2 + 2x + 5 = 0 -> x = -1 + 2i, -1 - 2i
    x1, x2 = solve_quadratic(1, 2, 5)
    check_close("x^2 + 2x + 5 = 0 -> x1 real part = -1", x1[0], -1)
    check_close("x^2 + 2x + 5 = 0 -> x1 imaginary part = 2", x1[1], 2)
    check_close("x^2 + 2x + 5 = 0 -> x2 real part = -1", x2[0], -1)
    check_close("x^2 + 2x + 5 = 0 -> x2 imaginary part = -2", x2[1], -2)


def test_negative_a():
    # -x^2 + 3x - 2 = 0 -> x = 1, 2
    x1, x2 = solve_quadratic(-1, 3, -2)
    low, high = sorted([x1, x2])
    check_close("-x^2 + 3x - 2 = 0 -> smaller root = 1", low, 1)
    check_close("-x^2 + 3x - 2 = 0 -> larger root = 2", high, 2)


if __name__ == "__main__":
    test_a_zero_b_zero_c_zero()
    test_a_zero_b_zero_c_nonzero()
    test_a_zero_linear_equation()
    test_a_zero_linear_equation_negative_c()
    test_trivial_quadratic()
    test_b_zero_real_roots()
    test_b_zero_complex_roots()
    test_two_distinct_real_roots()
    test_repeated_real_root()
    test_complex_roots_with_nonzero_real_part()
    test_negative_a()
