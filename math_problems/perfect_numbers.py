# This function classifies a given positive integer as perfect, abundant, or deficient
# based on the sum of its proper divisors. A perfect number has a sum equal to the number
# itself, an abundant number has a sum greater than the number, and a deficient number
# has a sum less than the number. The function raises a ValueError for non-positive inputs.

def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisible_numbers = []
    for i in range(1, number):
        if number % i == 0 and i != number:
            divisible_numbers.append(i)

    if sum(divisible_numbers) == number:
        return "perfect"
    elif sum(divisible_numbers) > number:
        return "abundant"
    else:
        return "deficient"
