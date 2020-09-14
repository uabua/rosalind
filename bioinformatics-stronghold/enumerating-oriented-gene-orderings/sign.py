"""
ID: SIGN
Title: Enumerating Oriented Gene Orderings
URL: http://rosalind.info/problems/sign/
"""

from itertools import product

def signed_permutations(num):
    """
    Finds all signed permutations of length num.

    Args:
        num {int}: positive integer

    Returns:
        list: list of all signed permutations
    """
    iterables = [n for n in range(-num, num+1) if n != 0]
    signed_perms = []

    for p in product(iterables, repeat=num):
        if len(set(abs(n) for n in p)) == num:
            signed_perms.append(p)

    return signed_perms

def print_signed_permutation(num):
    """
    Prints the total number of signed permutations of length num, followed by a list of all such permutations.

    Args:
        num {int}: positive integer

    Returns:
        None
    """
    signed_perms = signed_permutations(num)

    print(len(signed_perms))
    for p in signed_perms:
        print(" ".join(map(str, p)))

