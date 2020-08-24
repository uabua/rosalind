"""
ID: LCSM
Title: Finding a Shared Motif
URL: http://rosalind.info/problems/lcsm/
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

def get_shared_motif(dnas):
    """
    Finds one of the longest shared motifs in dnas.

    Args:
        dnas {list}: list of dnas

    Returns:
        str: one of the longest shared motifs
    """
    shared_motif = ''
    sample = dnas[0]
    sample_length = len(sample)

    for i in range(sample_length):
        for j in range(sample_length-i+1):
            if j > len(shared_motif) and all(sample[i:i+j] in dna for dna in dnas):
                shared_motif = sample[i:i+j]

    return shared_motif

