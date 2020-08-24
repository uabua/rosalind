"""
ID: LEXF
Title: Enumerating k-mers Lexicographically
URL: http://rosalind.info/problems/lexf/
"""

from itertools import product

def lexicographic_cartesian_product(alphabet, length):
    """
    Prints all strings that can be formed from the alphabet, ordered lexicographically.

    Args:
        alphabet {str}: collection of symbols defining an ordered alphabet
        length {int}: length of formed string

    Returns:
        None
    """
    for p in product(alphabet.replace(" ", ""), repeat=length):
        print("".join(p))

