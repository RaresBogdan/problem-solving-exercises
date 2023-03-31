# This function takes an input integer and calculates the sum of its digits. To do this,
# the function first checks that the input is an integer with more than one digit. If it
# passes this check, the function iterates over the digits of the input number and adds
# them up. The resulting sum is then returned as the output of the function.

def sum_of_digits(number):
    if isinstance(number, int) and len(str(number)) == 1:
        raise TypeError("Input integer must have more than one digit.")
    addition_of_digits = 0
    for digit in str(number):
        addition_of_digits += int(digit)
    return addition_of_digits
