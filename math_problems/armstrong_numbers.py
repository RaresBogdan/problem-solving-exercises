# An Armstrong number is a number that is equal to the sum
# of its own digits raised to the power of the number of digits in the number.
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

# This function checks whether the given number is an Armstrong number by
# calculating the sum of the digits raised to the power of the number of digits
# and comparing it to the original number.

def is_armstrong_number(number):
    num_str = str(number)
    num_len = len(num_str)
    armstrong_sum = 0
    for digit in num_str:
        armstrong_sum += int(digit) ** num_len
    if armstrong_sum == number:
        return True
    else:
        return False
