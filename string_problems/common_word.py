# This function takes in a single argument, which is expected to be a string called "phrase".
# The function checks that the input argument is a non-empty string, and then
# finds the most common word(s) in the string.
# If there is only one most common word, that word is returned. If there are multiple most common
# words, they are returned in a formatted string.
# If all the words in the input string have the same frequency, the function returns a string indicating that fact.
# The function also handles punctuation by removing it from the input string.
import string


def common_word(phrase):
    if not isinstance(phrase, str):
        raise TypeError("Input argument must be a string")

    if not phrase or not phrase.split():
        raise ValueError("Input string cannot be empty")

    for punctuation in string.punctuation:
        phrase = phrase.replace(punctuation, "")

    words = phrase.split()
    lowercase_words = []
    for word in words:
        lowercase_words.append(word.lower())

    freq = {}
    for word in lowercase_words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    if not freq:
        raise ValueError("Sentence must be formed out of words, not punctuation marks")

    max_freq = max(freq.values())
    common_words = [word for word, freq in freq.items() if freq == max_freq]

    if len(common_words) == len(freq):
        return "All the words in the string have the same frequency"

    if len(common_words) == 1:
        return common_words[0]

    return f"There are multiple most common words: {', '.join(common_words)}"
