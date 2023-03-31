# This function computes the factorial of a non-negative integer, which is the
# product of all positive integers up to and including the input number. The
# function raises a TypeError if the input is not a non-negative integer. Otherwise,
# the function initializes the result to 1 and multiplies it successively by all
# positive integers up to and including the input number using a for loop. Finally,
# the function returns the computed result.

def factorial_of_number(number):
    if not isinstance(number, int) or number < 0:
        raise TypeError("Input must be a non-negative integer.")
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
