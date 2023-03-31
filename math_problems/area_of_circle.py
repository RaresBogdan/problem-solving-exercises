# This function computes the area of a circle given its diameter. The function
# raises a TypeError if the input diameter is not a positive number, either integer
# or float. Otherwise, the function computes the radius as half of the diameter,
# and returns the area of the circle using the formula A = pi * r^2, where pi is
# approximated to 3.14159265359.

def area_of_circle(diameter):

    if not isinstance(diameter, (int, float)) or diameter < 0:
        raise TypeError("Input must be a number that is greater than 0")
    return 3.14159265359 * (diameter / 2) ** 2