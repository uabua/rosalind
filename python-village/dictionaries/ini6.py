"""
My solution to Rosalind problem 'Dictionaries'

ID: INI6
Title: Dictionaries
URL: http://rosalind.info/problems/ini6/
"""

from collections import Counter

def unique_word_counter(sentence): # words are case-sensitive
    """
    Counts and then prints occurrences of each word in sentence, where words are separated by spaces. Words are case-sensitive. 

    Args:
        sentence {str}: sentence, where words ase seperated by spaces

    Returns:
        None
    """
    words = sentence.split()

    words_occurrences = Counter(words)

    for key, value in words_occurrences.items():
        print(key, value)
