"""
ID: MRNA
Title: Inferring mRNA from Protein
URL: http://rosalind.info/problems/mrna/
"""

# RNA codon table
rna_codon_dict = {
    "F": ["UUU", "UUC"],
    "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
    "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
    "Y": ["UAU", "UAC"],
    "C": ["UGU", "UGC"],
    "W": ["UGG"],
    "P": ["CCU", "CCC", "CCA", "CCG"],
    "H": ["CAU", "CAC"],
    "Q": ["CAA", "CAG"],
    "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "I": ["AUU", "AUC", "AUA"],
    "M": ["AUG"],
    "T": ["ACU", "ACC", "ACA", "ACG"],
    "N": ["AAU", "AAC"],
    "K": ["AAA", "AAG"],
    "V": ["GUU", "GUC", "GUA", "GUG"],
    "A": ["GCU", "GCC", "GCA", "GCG"],
    "D": ["GAU", "GAC"],
    "E": ["GAA", "GAG"],
    "G": ["GGU", "GGC", "GGA", "GGG"],
    "Stop": ["UAA", "UAG", "UGA"] # stop codons
}

def get_total(protein):
    """
    Calculates the total number of different RNA strings from which the protein could have been translated, modulo 
    1000000.

    Args:
        protein {str}: protein string

    Returns:
        int: The total number of different RNA strings from which the protein could have been translated, modulo 
        1000000
    """
    total = 1

    for character in protein:
        total *= len(rna_codon_dict[character])

    return (total * 3) % 1000000 # times 3 because of 3 possible stop codons

        