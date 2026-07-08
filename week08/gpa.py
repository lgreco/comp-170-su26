
# A procedure to enter a new grade

def enter_grade(letter: str, gpa: float):
    """Takes a letter A,B,C,D, or F,
    and converts it to a numeric grade.
    """
    # normalize input so lowercase letters (e.g. 'a') are accepted too
    letter = letter.upper()
    # guard clause: reject anything that isn't a valid letter grade
    if letter not in 'ABCDF':
        raise ValueError('Oops, you must enter A, B, C, D, or F')
    # guard clause: a GPA can never be negative
    if gpa < 0:
        raise ValueError('Oops, current GPA cannot be negative')
    # default numeric grade; stays 0 for an 'F'
    grade = 0
    # each branch checked independently (not elif) - only one will match
    # since letter was already validated to be exactly one of ABCDF
    if letter == 'A':
        grade = 4.0
    if letter == 'B':
        grade = 3.0
    if letter == 'C':
        grade = 2.0
    if letter == 'D':
        grade = 1.0

    # take the existing GPA and update it
    # simple average of the old GPA and the new grade
    gpa = (gpa+grade)/2

    return gpa
