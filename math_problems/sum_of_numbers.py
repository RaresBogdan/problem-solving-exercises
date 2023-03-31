# The sum_of_numbers function takes a non-negative integer number as input and
# calculates the sum of all the numbers from 0 up to number, inclusive.
# For example, if the input is 4, the function calculates the sum of 0 + 1 + 2 + 3 + 4, which is 10.
# The function returns this sum as an integer.

def sum_of_numbers(number):
    sum_of_num = 0
    for i in range(number + 1):
        sum_of_num += i
    return sum_of_num
