# This function takes in a single argument, which is expected to be a list
# called "number_list" containing integer or float values.
# The function checks that the input argument is a non-empty list containing
# only integer or float values, and then returns the largest value in the list.
# If the input argument is not a list, or if it is an empty list, the function raises an error.
# If any of the items in the input list is not an integer or a float,the function also raises an error.

def largest_number(number_list):
    if not number_list:
        raise ValueError("Input list cannot be empty")

    if not isinstance(number_list, list):
        raise TypeError("Input must be a list")

    for item in number_list:
        if not isinstance(item, (int, float)):
            raise TypeError("Input list must contain integer or float values")

    return max(number_list)
