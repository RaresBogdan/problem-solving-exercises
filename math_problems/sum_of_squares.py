# This function takes an input integer and calculates the sum of the squares of all integers
# from 0 to the input number (inclusive). To do this, the function initializes a variable to
# store the running sum, and then iterates over a range from 0 to the input number. During each
# iteration, the function squares the current integer and adds it to the running sum. Finally,
# the function returns the resulting sum as its output.

def sum_of_squares(number):
    number_sum = 0
    for i in range(number + 1):
        number_sum += int(i) ** 2
    return number_sum
