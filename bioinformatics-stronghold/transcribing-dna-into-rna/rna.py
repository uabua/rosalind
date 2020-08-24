"""
ID: RNA
Title: Transcribing DNA into RNA
URL: http://rosalind.info/problems/rna/
"""

def dna_to_rna(dna_string):
    """
    Transcribes dna_string to rna_string.
    
    Args:
        dna_string {str}: DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T')
    
    Returns:
        str: rna_string where 'T' is replaced by 'U'
    """
    rna_string = dna_string.replace("T", "U")

    return rna_string
