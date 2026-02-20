"""
Source code to determine the type of triangle based on side lengths
"""

def define_triangle (a,b,c):
    """Returns the type of triangle given three sides."""
    if (a <= 0 or b <= 0 or c <= 0):
        return "Not a triangle"
    if (a == b and b == c):
        return "Equilateral"
    if (a == b or b == c or a == c):
        return "Isosceles"
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return "Right Triangle"
    if (a != b and b != c and a != c):
        return "Scalene"
    return "Not a triangle"
