gpa = 0

# A procedure to enter a new grade

def enter_grade(letter: str, gpa: float):
    """Takes a letter A,B,C,D, or F,
    and converts it to a numeric grade.
    """
    letter = letter.upper()
    if letter not in 'ABCDF':
        raise ValueError('Oops, you must enter A, B, C, D, or F')
    if gpa < 0:
        raise ValueError('Oops, current GPA cannot be negative')
    grade = 0
    if letter == 'A':
        grade = 4.0
    if letter == 'B':
        grade = 3.0
    if letter == 'C':
        grade = 2.0
    if letter == 'D':
        grade = 1.0

    # take the existing GPA and update it
    gpa = (gpa+grade)/2

    return gpa
