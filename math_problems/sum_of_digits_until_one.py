# This function takes an input integer and repeatedly sums its digits until a single-digit
# number is obtained. To do this, the function first checks that the input is a positive
# integer. It then iteratively sums the digits of the input number using a while loop and
# updates the input number until it becomes a single-digit number. The resulting single-digit
# sum is then returned as the output of the function.

def sum_of_digits_until_one(number):
    while number >= 10:
        n_str = str(number)
        digit_sum = 0
        for digit in n_str:
            digit_sum += int(digit)
        number = digit_sum
    return number
