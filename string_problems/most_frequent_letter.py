# This function takes a string as input and returns the most frequent letter(s) in it
# It raises a TypeError if the input is not a string or if it is an empty string or
# a string with only whitespace characters
# It removes all punctuation marks from the input string
# It converts the input string to lowercase to avoid case sensitivity
# It creates a dictionary with keys being letters in the input string and values
# being the frequency of each letter in the string
# It finds the maximum frequency of letters in the string and returns the most frequent letter(s)
import string


def most_frequent_letter(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    if not word or not word.split():
        raise TypeError("Input string cannot be empty")

    for punctuation in string.punctuation:
        word = word.replace(punctuation, "")

    lowercase_word = word.strip().lower()
    letter_dic = {}

    for letter in lowercase_word:
        if letter in letter_dic:
            letter_dic[letter] += 1
        else:
            letter_dic[letter] = 1

    max_freq = max(letter_dic.values())
    frequent_letters = [letter for letter, freq in letter_dic.items() if freq == max_freq]

    if len(frequent_letters) == 1:
        return f"The most frequent letter is {frequent_letters[0]}"
    else:
        return f"There are multiple most frequent letters: {', '.join(frequent_letters)}"