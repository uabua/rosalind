"""
ID: PROB
Title: Introduction to Random Strings
URL: http://rosalind.info/problems/prob/
"""

from math import log10

def random_probabilities(dna, probs):
    """
    Generates probabilities, where each probability represent the common logarithm of the probability that a random string 
    constructed with the GC-content found in probabilities string will match dna exactly.

    Args:
        dna {str}: dna
        probs {str}: probabilities

    Returns:
        str: string of random probabilities
    """
    probs = map(float, probs.split())
    random_probs = []

    for prob in probs:
        gc = prob / 2
        at = (1 - prob) / 2

        probability = 1

        for nucleobase in dna:
            if nucleobase in "CG":
                probability *= gc
            else:
                probability *= at
        
        random_probs.append(str(log10(probability)))
    
    return " ".join(random_probs)