"""
ID: PERM
Title: Enumerating Gene Orders
URL: http://rosalind.info/problems/perm/
"""

from math import factorial
from itertools import permutations

def print_permutation(num):
    """
    Prints the total number of permutations of length num, followed by a list of all such permutations.

    Args:
        num {int}: positive integer

    Returns:
        None
    """
    print(factorial(num))

    for permutation in permutations(range(1, num+1)):
        print(" ".join(map(str, permutation)))
    
