# This function takes a positive integer and repeatedly sums its digits until a single-digit number is obtained.
# It uses a while loop to iteratively sum the digits of the input number until it becomes a single-digit number.
# The resulting single-digit sum is then returned as the output of the function.

def square_of_sum(number):
    nums = range(1, number+1)
    sum_of_nums = sum(nums)
    square = sum_of_nums ** 2
    return square


def sum_of_squares(number):
    sum_squares = 0
    for digit in range(1, number+1):
        sum_squares += digit ** 2
    return sum_squares


def difference_of_squares(number):
    square_of_sum_result = square_of_sum(number)
    sum_of_squares_result = sum_of_squares(number)
    difference = square_of_sum_result - sum_of_squares_result
    return difference

