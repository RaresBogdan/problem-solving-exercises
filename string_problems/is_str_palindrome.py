# The function "is_str_palindrome" takes in a single argument, which is expected to be a string.
# The function checks whether the input string is a valid non-empty string, and then removes
# any punctuation and spaces from the string, and converts it to lowercase.
# Finally, the function checks whether the cleaned-up string is a palindrome, meaning
# whether it is the same when read forward and backward. If the cleaned-up string is a
# palindrome, the function returns True, otherwise it returns False.
# If the input argument is not a string, or if it is an empty string or consists
# only of whitespace characters, the function raises an error.

def is_str_palindrome(word):
    if not isinstance(word, str):
        raise TypeError("Input argument must be a string")

    if not word or not word.split():
        raise ValueError("Input string cannot be empty")

    clean_word = ''.join(char for char in word if char not in string.punctuation)
    clean_word = clean_word.replace(" ", "").lower()
    reversed_word = ''.join(reversed(clean_word))

    return clean_word == reversed_word
