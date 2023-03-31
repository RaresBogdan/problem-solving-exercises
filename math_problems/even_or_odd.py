# This function takes an input integer and determines whether it is even or odd. An even
# number is a number that is divisible by 2 without a remainder, while an odd number is
# not divisible by 2 without a remainder. If the input number is even, the function returns
# the message "The number you have chosen is even". If the input number is odd, the function
# returns the message "The number you have chosen is odd".

def even_or_odd(number):
    if number % 2 == 0:
        return "The number you have chosen is even"
    else:
        return "The number you have chosen is odd"
