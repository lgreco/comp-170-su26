# mathemagics

A tiny library for solving quadratic (and linear) equations of the form
`ax^2 + bx + c = 0`, including complex roots.

## Install

```bash
pip install mathemagics
```

## Usage

```python
from mathemagics import solve_quadratic

x1, x2 = solve_quadratic(1, -3, 2)
print(x1, x2)  # 2.0 1.0
```

### Return value

`solve_quadratic(a, b, c)` returns a tuple `(x1, x2)`:

- If `a == 0` and `b == 0`: no solution exists; returns `(nan, nan)`.
- If `a == 0` and `b != 0`: the equation is linear; `x1` and `x2` are equal.
- If `a != 0` and the discriminant is non-negative: `x1` and `x2` are real numbers.
- If `a != 0` and the discriminant is negative: `x1` and `x2` are complex roots,
  each represented as a `(real_part, imaginary_part)` tuple.

## License

MIT
