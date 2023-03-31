# This function calculates the total number of grains of wheat on a chessboard
# where the number of grains on each square is doubled from the previous square.
# The 'square' function calculates the number of grains on a particular square, raising
# a 'ValueError' if the input is not between 1 and 64.
# The 'total' function then calls the 'square' function for
# each square and adds up the resulting number of grains, returning
# the total number of grains on the chessboard.

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grains = 1
    for i in range(1, number):
        grains += grains
    return grains


def total():
    total_grains = 0
    for i in range(1, 65):
        total_grains += square(i)
    return total_grains
