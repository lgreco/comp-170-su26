
from math import sqrt

def solve_quadratic_equation(a: float, b: float, c: float):
    """Solves the basic quadratic equation:
       a*x^2 + b*x + c = 0
    The solutions to this equation is

    x1, x2 = (-b±(sqrt(b^2-4ac)/2a)

    The equation has solutions only when the quantity
    b^2-4ac >= 0. Otherwise the square root of b^2-4ac
    does not exist. This quantity is called the discriminant
    of the equation.
    """

    # Compute the discriminant 
    discriminant = b*b - 4*a*c

    # Proceed only with valid discriminant
    if discriminant >= 0:
        # Solve the equation
        x1 = (-b-sqrt(discriminant))/(2*a)
        x2 = (-b+sqrt(discriminant))/(2*a)
        print (x1, x2)
    else:
        # Reject
        print("Sorry, no real solutions for this equation.")
        print("Unless you went to a Greek kindergarden.")

if __name__ == "__main__":
    solve_quadratic_equation(1,2,3) # x^2 + 2x + 3 = 0
    solve_quadratic_equation(1,2,-3) # x^2 + 2x -3 = 0
