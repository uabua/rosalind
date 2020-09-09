"""
ID: LEXV
Title: Ordering Strings of Varying Length Lexicographically
URL: http://rosalind.info/problems/lexv/
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
    products = []

    for p in product(alphabet.replace(" ", ""), repeat=length):
        for index in range(1, length+1):
            if p[:index] not in products:
                products.append(p[:index])
    
    for p in products:
        print("".join(p))

