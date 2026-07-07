import math
import unittest

from mathemagics import solve_quadratic


class TestSolveQuadratic(unittest.TestCase):

    def test_a_zero_b_zero_c_zero(self):
        # 0 = 0: no equation, no solution -> (NaN, NaN)
        x1, x2 = solve_quadratic(0, 0, 0)
        self.assertTrue(math.isnan(x1))
        self.assertTrue(math.isnan(x2))

    def test_a_zero_b_zero_c_nonzero(self):
        # 5 = 0: contradiction, no solution -> (NaN, NaN)
        x1, x2 = solve_quadratic(0, 0, 5)
        self.assertTrue(math.isnan(x1))
        self.assertTrue(math.isnan(x2))

    def test_a_zero_linear_equation(self):
        # 2x + 4 = 0 -> x = -2
        x1, x2 = solve_quadratic(0, 2, 4)
        self.assertAlmostEqual(x1, -2)
        self.assertAlmostEqual(x2, -2)

    def test_a_zero_linear_equation_negative_c(self):
        # 3x - 9 = 0 -> x = 3
        x1, x2 = solve_quadratic(0, 3, -9)
        self.assertAlmostEqual(x1, 3)
        self.assertAlmostEqual(x2, 3)

    def test_trivial_quadratic(self):
        # x^2 = 0 -> x = 0, 0
        x1, x2 = solve_quadratic(1, 0, 0)
        self.assertAlmostEqual(x1, 0)
        self.assertAlmostEqual(x2, 0)

    def test_b_zero_real_roots(self):
        # x^2 - 4 = 0 -> x = 2, -2
        x1, x2 = solve_quadratic(1, 0, -4)
        self.assertAlmostEqual(x1, 2)
        self.assertAlmostEqual(x2, -2)

    def test_b_zero_complex_roots(self):
        # x^2 + 4 = 0 -> x = 2i, -2i
        x1, x2 = solve_quadratic(1, 0, 4)
        self.assertAlmostEqual(x1[0], 0)
        self.assertAlmostEqual(x1[1], 2)
        self.assertAlmostEqual(x2[0], 0)
        self.assertAlmostEqual(x2[1], -2)

    def test_two_distinct_real_roots(self):
        # x^2 - 3x + 2 = 0 -> x = 2, 1
        x1, x2 = solve_quadratic(1, -3, 2)
        self.assertAlmostEqual(x1, 2)
        self.assertAlmostEqual(x2, 1)

    def test_repeated_real_root(self):
        # x^2 + 2x + 1 = 0 -> x = -1, -1
        x1, x2 = solve_quadratic(1, 2, 1)
        self.assertAlmostEqual(x1, -1)
        self.assertAlmostEqual(x2, -1)

    def test_complex_roots_with_nonzero_real_part(self):
        # x^2 + 2x + 5 = 0 -> x = -1 + 2i, -1 - 2i
        x1, x2 = solve_quadratic(1, 2, 5)
        self.assertAlmostEqual(x1[0], -1)
        self.assertAlmostEqual(x1[1], 2)
        self.assertAlmostEqual(x2[0], -1)
        self.assertAlmostEqual(x2[1], -2)

    def test_negative_a(self):
        # -x^2 + 3x - 2 = 0 -> x = 1, 2
        x1, x2 = solve_quadratic(-1, 3, -2)
        low, high = sorted([x1, x2])
        self.assertAlmostEqual(low, 1)
        self.assertAlmostEqual(high, 2)


if __name__ == "__main__":
    unittest.main()
