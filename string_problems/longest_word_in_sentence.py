# This function takes in a single argument, which is expected to be a string called "sentence".
# The function removes any punctuation from the sentence and splits it into a list of words.
# The function then finds the longest word(s) in the sentence, and returns either the longest word if there is only one,
# or a message stating that there are multiple longest words if there are ties.
# If the input argument is not a string, or if it is an empty string or consists only of whitespace characters,
# the function raises an error. If the input argument is a string consisting only of punctuation marks,
# the function also raises an error.
import string


def longest_word(sentence):
    if not isinstance(sentence, str):
        raise TypeError("Input argument must be a string")

    if not sentence or not sentence.strip():
        raise ValueError("Input string cannot be empty")

    for punctuation in string.punctuation:
        sentence = sentence.replace(punctuation, "")

    clean_sentence = sentence.split()
    length_dict = {}

    for word in clean_sentence:
        length = len(word)
        if length in length_dict:
            length_dict[length].append(word)
        else:
            length_dict[length] = [word]

    if not length_dict:
        raise ValueError("Sentence must be formed out of words, not punctuation marks")

    longest_length = max(length_dict.keys())
    longest_words = length_dict[longest_length]

    if len(longest_words) == 1:
        return longest_words[0]
    return f"There are multiple same length words: {', '.join(longest_words)}"
