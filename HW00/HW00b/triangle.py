# Source code to determine the type of triangle based on side lengths

def defineTriangle (a,b,c):
    if (a <= 0 or b <= 0 or c <= 0):
        return "Not a triangle"
    elif (a <= 0 or b <= 0 or c <= 0):
        return "Not a triangle"
    if (a == b and b == c):
        return "Equilateral"
    elif (a == b or b == c or a == c):
        return "Isosceles"
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return "Right Triangle"
    elif (a != b and b != c and a != c):
        return "Scalene"
    else:
        return "Not a triangle"