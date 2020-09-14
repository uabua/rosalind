"""
ID: REVP
Title: Locating Restriction Sites
URL: http://rosalind.info/problems/revp/
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

def get_reverse_complement(dna):
    """
     Finds the reverse complement of a dna.

    Args:
        dna {str}: DNA string

    Returns:
        str: the reverse complement of a dna
    """
    reverse_complement = ""

    for character in dna[::-1]:
        if character == "A":
            reverse_complement += "T"
        elif character == "T":
            reverse_complement += "A"
        elif character == "C":
            reverse_complement += "G"
        elif character == "G":
            reverse_complement += "C"

    return reverse_complement

def print_position_and_length(dna):
    """
    Prints the position and length of every reverse palindrome in the dna having length between 4 and 12.

    Args:
        dna {str}: DNA string

    Returns:
        None
    """
    for i in range(len(dna)):
        for k in range(4, 13):
            if i + k <= len(dna):
                substr = dna[i:i+k]
                substr_reverse_complement = get_reverse_complement(substr)
            
                if substr == substr_reverse_complement:
                    print(i+1, k)

