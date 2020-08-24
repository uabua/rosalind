"""
ID: SUBS
Title: Finding a Motif in DNA
URL: http://rosalind.info/problems/subs/
"""

import re

def find_motif(first_dna_string, second_dna_string):
    """
    Finds indices(motif) of second_dna_string in first_dna_string and prints them. 
    This function uses 1-based numbering,
    
    Args:
        first_dna_string {str}: DNA string
        second_dna_string {str}: DNA string
    
    Returns:
        None
    """
    if second_dna_string in first_dna_string:
        indices = [substring.start() for substring in re.finditer(f'(?={second_dna_string})', first_dna_string)]

        for index in indices:
            print(index + 1, end=" ")
        print()
    else:
        print(f"{second_dna_string} is not a substring of {first_dna_string}.")




