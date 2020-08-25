"""
ID: TRAN
Title: Transitions and Transversions
URL: http://rosalind.info/problems/tran/
"""

def fasta_file_parser(fasta_file_path):
    """
    Parses Fasta files.
    
    Args:
        fasta_file_path {str}: path of Fasta file
    
    Returns:
        dict: list of dnas
    """
    with open(fasta_file_path, 'r') as fasta_file:
        dataset = fasta_file.readlines()

    dnas = {}
    
    for line in dataset:
        if line.startswith(">"):
            id = line[1:-1]
            dnas[id] = ""
        else:
            dnas[id] += line.strip()

    return list(dnas.values())

# after parsing fasta file, we have only two dnas
# dnas = fasta_file_parser("path")
# first_dna = dnas[0]
# second_dna = dnas[1]

def transition_transversion_ratio(first_dna, second_dna):
    """
    Calculates the transition/transversion ratio.

    Args:
        first_dna {str}: DNA string
        second_dna {str}: DNA string

    Returns:
        float: the transition/transversion ratio 
    """
    transition = 0
    transversion = 0
    
    for index in range(len(first_dna)):
        if (first_dna[index] in 'AG' and second_dna[index] in 'CT') or (first_dna[index] in 'CT' and second_dna[index] in 'AG'):
            transversion += 1
        elif first_dna[index] == second_dna[index]:
            continue
        else:
            transition += 1

    return transition/transversion

