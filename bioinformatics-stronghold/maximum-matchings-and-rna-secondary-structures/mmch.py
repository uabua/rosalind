"""
ID: MMCH
Title: Maximum Matchings and RNA Secondary Structures
URL: http://rosalind.info/problems/mmch/
"""

from math import factorial

def max_matchings(rna):
    """
    Calculates the total possible number of maximum matchings of basepair edges(A-u, C-G).

    Args:
        rna {str}: RNA string

    Returns:
        int: the total possible number of maximum matchings
    """
    a, u, g, c = map(rna.count, ["A", "U", "G", "C"])
    
    # please notice, that I used floor (integer) division because of rosalind answer format recognition
    # I mean, they used python2 (in python2 result of int/int is int)
    au_perm = factorial(max(a, u)) // factorial(max(a, u) - min(a, u))
    gc_perm = factorial(max(g, c)) // factorial(max(g, c) - min(g, c))
    
    return au_perm * gc_perm

