# This function takes in a single argument, which is expected to be a string called "word".
# The function checks that the input argument is a non-empty string, and then reverses the string by iterating over each character
# in the string and adding it to the beginning of a new string.
# If the input argument is not a string, or if it is an empty string or consists only of whitespace characters,
# the function raises an error.

def reverse_string(word):
    if not isinstance(word, str):
        raise TypeError("Input argument must be a string")

    if not word or not word.strip():
        raise ValueError("Input string cannot be empty")

    reversed_string = ""

    for i in word:
        reversed_string = i.lower() + reversed_string

    return reversed_string
