"""
ID: CAT
Title: Catalan Numbers and RNA Secondary Structures
URL: http://rosalind.info/problems/cat/
"""

cache = {"": 1, "AU": 1, "UA": 1, "GC": 1, "CG": 1,
         "A": 0, "U": 0, "G": 0, "C": 0,
        "AG": 0, "AC": 0, "AA": 0, 
        "UG": 0, "UC": 0, "UU": 0,
        "GA": 0, "GU": 0, "GG": 0,
        "CA": 0, "CU": 0, "CC": 0
        }

def total_noncrossing_matchings(rna):
    """
    Calculates the total number of noncrossing perfect matchings of basepair edges in the bonding graph of RNA 
    string, modulo 1,000,000.

    Args:
        rna {str}: RNA string

    Returns:
        int: the total number of noncrossing perfect matchings of basepair edges in the bonding graph of RNA string, 
        modulo 1,000,000.
    """
    if rna not in cache: 
        noncrossing_matchings = []

        for index in range(1, len(rna), 2):
            noncrossing_matchings.append(total_noncrossing_matchings(rna[1:index]) * cache[rna[0]+rna[index]] 
            * total_noncrossing_matchings(rna[index+1:]))

        cache[rna] = sum(noncrossing_matchings)
    return cache[rna] % 1000000

