"""
ID: GRPH
Title: Overlap Graphs
URL: http://rosalind.info/problems/grph/
"""

def fasta_file_parser(fasta_file_path):
    """
    Parses Fasta files.
    
    Args:
        fasta_file_path {str}: path of Fasta file
    
    Returns:
        dict: dict of dnas
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

    return dnas

def print_adjacency_list(dnas, match_length=3):
    """
    Prints the adjacency list corresponding to match_length.

    Args:
        dnas {dict}: dict of dnas
        match_length {int, optional}: length of match. Defaults to 3.

    Returns:
        None
    """
    for k, v in dnas.items():
        for key, value in dnas.items():
            if (k != key) and (v[-3:] == value[:3]):
                print(k, key)

