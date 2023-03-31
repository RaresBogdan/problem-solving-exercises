# This function returns the maximum of three input values, which can be of any comparable
# type. The function uses nested ternary operators to compare the input values and return
# the largest of the three. The function assumes that the input values are comparable, and
# does not perform any type checking or error handling.

def find_max(a, b, c):
    return a if a > b and a > c else b if b > a and b > c else c
