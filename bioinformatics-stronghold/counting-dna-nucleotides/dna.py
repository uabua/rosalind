"""
My solution to Rosalind problem 'Counting DNA Nucleotides'

ID: DNA
Title: Counting DNA Nucleotides
URL: http://rosalind.info/problems/dna/
"""

def nucleotides_counter(dna_string):
    """
    Counts DNA nucleotides in a given dna_string.
    
    Args:
        dna_string {str}: DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T')
    
    Returns:
        str: four integers (separated by spaces) counting the respective number of times that the symbols 
        'A', 'C', 'G', and 'T' occur in dna_string
    """
    adenine = dna_string.count("A")
    cytosine = dna_string.count("C")
    guanine = dna_string.count("G")
    thymine = dna_string.count("T")

    return f"{adenine} {cytosine} {guanine} {thymine}"
