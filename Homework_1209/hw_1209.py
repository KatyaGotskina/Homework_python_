"""Counting the percentage of lines with more capital letters."""


def str_procent(slova: str):
    """
    Takes a string of words and counts the percentage of words with more capital letters.

    Args:
        slova: str - string of words

    Returns: float - percentage of substrings with more capitals letter.
    """
    list_words = slova.split()
    count1 = 0

    for word in list_words:
        hiigh = 0
        for letter in word:
            if letter.isupper():
                hiigh += 1
        if hiigh / len(word) > 0.5:
            count1 += 1

    return round(count1 / len(list_words) * 100, 2)
