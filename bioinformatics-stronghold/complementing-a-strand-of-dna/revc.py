"""
My solution to Rosalind problem 'Complementing a Strand of DNA'

ID: REVC
Title: Complementing a Strand of DNA
URL: http://rosalind.info/problems/revc/
"""

def complement_strand(dna_string):
    """
    Finds the reverse complement of a dna_string.
    
    Args:
        dna_string {str}: DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T')
    
    Returns:
        str: the reverse complement string of a dna_string
    """
    reverse_complement = ""

    for character in dna_string[::-1]:
        if character == "A":
            reverse_complement += "T"
        elif character == "T":
            reverse_complement += "A"
        elif character == "C":
            reverse_complement += "G"
        elif character == "G":
            reverse_complement += "C"

    return reverse_complement


