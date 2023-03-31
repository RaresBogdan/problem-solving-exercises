# This function takes an input integer and checks if it is a perfect square, i.e., if it is
# equal to the square of an integer. To do this, the function calculates the square root of
# the input number using the `sqrt` function from the `math` module. If the square root is an
# integer, then the input number is a perfect square and the function returns `True`.
# Otherwise, the function returns `False`.
import math


def is_perfect_square(num):
    root = math.sqrt(num)
    return root.is_integer()
