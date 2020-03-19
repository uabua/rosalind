"""
My solution to Rosalind problem 'Counting Point Mutations'

ID: HAMM
Title: Counting Point Mutations
URL: http://rosalind.info/problems/hamm/
"""

def calculate_hamming_distance(first_dna_string, second_dna_string):
    """
    Calculates the Hamming distance between first_dna_string and second_dna_string.
    
    Args:
        first_dna_string {str}: DNA string
        second_dna_string {str}: DNA string
    
    Returns:
        int: the Humming distance
    """
    hamming_distance = 0

    for index in range(len(first_dna_string)):
        if first_dna_string[index] != second_dna_string[index]:
            hamming_distance += 1
    
    return hamming_distance
