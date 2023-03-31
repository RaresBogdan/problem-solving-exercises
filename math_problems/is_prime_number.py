# This function determines whether an input integer is a prime number, which is a number
# greater than 1 that is only divisible by 1 and itself. The function returns True if the
# input number is a prime number, and False otherwise. The function uses a for loop to check
# if the input number is divisible by any integer between 2 and half the input number, and
# returns False if such a divisor is found. If the loop completes without finding a divisor,
# the function returns True, indicating that the input number is a prime number.

def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False
    return True
