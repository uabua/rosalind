"""
ID: SSEQ
Title: Finding a Spliced Motif
URL: http://rosalind.info/problems/sseq/
"""

def fasta_file_parser(fasta_file_path):
    """
    Parses Fasta files.
    
    Args:
        fasta_file_path {str}: path of Fasta file
    
    Returns:
        list: list of dnas
    """
    with open(fasta_file_path, 'r') as fasta_file:
        dataset = fasta_file.readlines()

    dnas = {}
    
    for line in dataset:
        if line.startswith(">"):
            id = line[1:]
            dnas[id] = ""
        else:
            dnas[id] += line.strip()

    return list(dnas.values())

# dnas = fasta_file_parser("path")
# dna = dnas[0]
# sub_dna = dnas[1]

def print_indices(dna, sub_dna):
    """
    Prints indices of dna in which the symbols of sub_dna appear as a subsequence of dna.

    Args:
        dna {str}: DNA string
        sub_dna {str}: DNA string

    Returns:
        None
    """
    char_index = 0

    for character in sub_dna:
        char_index = dna.index(character, char_index)
        char_index += 1
        
        print(char_index, end=" ")

