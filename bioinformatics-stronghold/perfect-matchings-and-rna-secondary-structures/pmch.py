"""
ID: PMCH
Title: Perfect Matchings and RNA Secondary Structures
URL: http://rosalind.info/problems/pmch/
"""

from math import factorial

def total_perfect_matchins(rna):
    """
    Calculates the total possible number of perfect matchings of basepair edges(A-u, C-G).

    Args:
        rna {str}: RNA string

    Returns:
        int: the total number of perfect matchings
    """

    return factorial(rna.count("A")) * factorial(rna.count("G"))

