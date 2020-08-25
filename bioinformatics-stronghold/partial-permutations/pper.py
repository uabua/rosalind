"""
ID: PPER
Title: Partial Permutations
URL: http://rosalind.info/problems/pper/
"""

from math import factorial

def total_partial_permutations(n,k):
    """
    Calculates the total number of partial permutations P(n, k), modulo 1000000.

    Args:
        n {int}: positive integer
        k {int}: positive integer

    Returns:
        float: the total number of partial permutations P(n, k), modulo 1000000
    """
    return (factorial(n) / factorial(n-k)) % 1000000 # because in statistics P(n, k)=n!/(n-k)!

