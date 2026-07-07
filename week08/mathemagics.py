def solve_quadratic(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0.

    Return a tuple (x1, x2) with the solutions as follows.

    If a = 0, the equation is linear. In this case, it has a single solution
    which is indicated with a tuple of identical values, x1=x2.

    If a = 0 and b = 0, the equation simple doesn't exist, or is a 
    trivial assignment, c = 0. In this case there are no x values to
    solve for; the method returns a pair of two NaN values. These are
    special artifacts indicating the absence of numerical information.
    (NaN: Not a Number)

    If a ≠ 0, then we have a quadratic equation even if b is 0 or c = 0.

    If a ≠ 0 and b = c = 0, then it's a trivial quadratic with solution (0,0).

    If a ≠ 0 and b = 0, then it's an equation of the form ax^2 = -c. 
    Its solutions are (√c, -√c) if c ≤ 0. If c > 0 the solutions are 
    (i√c, -i√c) where i is the imaginary unit such that i^2 = -1.
    """

    # Initialize the solutions to NaN values.
    # Each language has a different way of representing NaN values. 
    # In Python, we can use float('nan').
    x1 = float('nan')
    x2 = float('nan')   
    # Check if a is zero.
    if a == 0:
        # If a is zero, we have a linear equation as long as b is not zero.
        if b != 0:
            x1 = -c / b
            # Both solutions are the same for a linear equation.
            x2 = x1  
    else:
        # If a is not zero, we have a quadratic equation.
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            sqrt_discriminant = discriminant**0.5
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
        else:
            # If the discriminant is negative, we have complex solutions.
            # We will skip Python's built-in complex number support 
            # and instead represent each complex number as a tuple with the
            # (real part, imaginary part).
            real_part = -b / (2*a)
            imaginary_part = (-discriminant)**0.5 / (2*a)
            x1 = (real_part, imaginary_part)
            x2 = (real_part, -imaginary_part)
    # Done.
    return (x1, x2)