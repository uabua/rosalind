"""
ID: CONS
Title: Consensus and Profile
URL: http://rosalind.info/problems/cons/
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

def count_nucleobases(dnas, nucleobase):
    """
    Counts the occurrence of specific nucleobases based on the index in all dnas.

    Args:
        dnas {list}: list of dnas
        nucleobase {str}: nucleobase (A, C, G or T)

    Returns:
        str: total number of occurences of specific nucleobases based on the index in all dnas.
    """
    total_nucleobase = nucleobase + ": "

    for index in range(len(dnas[0])):
        total = 0

        for dna in dnas:
            if dna[index] == nucleobase:
                total += 1
        total_nucleobase += str(total) + " "

    return total_nucleobase

def print_consensus(dnas):
    """
    Generates and prints consensus string.

    Args:
        dnas {list}: list of dnas

    Returns:
        None
    """
    max_nucleobase = []
    
    for index in range(len(dnas[0])):
        max_nucleobase.append(find_max_nucleobase(dnas, index))

    consensus_string = ""

    for nucleobase in max_nucleobase:
        if nucleobase == 0:
            consensus_string += "A"
        if nucleobase == 1:
            consensus_string += "C"
        if nucleobase == 2:
            consensus_string += "G"
        if nucleobase == 3:
            consensus_string += "T"

    print(consensus_string)

def find_max_nucleobase(dnas, index):
    """
    Finds the most frequent nucleobase based on the index in all dnas. 

    Args:
        dnas {list}: list of dnas
        index {int}: index of nucleobase

    Returns:
        str: the most frequent nucleobase based on the index in all dnas
    """
    total_nucleobases = [0, 0, 0, 0]

    for dna in dnas:
        if dna[index] == "A":
            total_nucleobases[0] += 1
        if dna[index] == "C":
            total_nucleobases[1] += 1
        if dna[index] == "G":
            total_nucleobases[2] += 1
        if dna[index] == "T":
            total_nucleobases[3] += 1

    return total_nucleobases.index(max(total_nucleobases))

def print_profile_matrix(dnas):
    """
    Prints profile matrix.

    Args:
        dnas {list}: list of dnas

    Returns:
        None
    """
    for nucleobase in 'ACGT':
        print(count_nucleobases(dnas, nucleobase).strip())
