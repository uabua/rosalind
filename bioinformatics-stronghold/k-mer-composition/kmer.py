"""
ID: KMER
Title: k-Mer Composition
URL: http://rosalind.info/problems/kmer/
"""
import re
from itertools import product

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

def cartesian_product(iter_str, repetitions):
    """
    Finds the cartesian product from the given iterables(iter_str).

    Args:
        iter_str {str}: iterables
        repetitions {int}: number of repetitions

    Returns:
        list: the cartesian product
    """
    substrings = []

    for p in product("ACGT", repeat=repetitions):
        substrings.append("".join(p))

    return substrings

def print_k_mer_composition(dna, k):
    """
    Prints the k-mer composition of DNA string.

    Args:
        dna {str}: DNA string
        k {int}: length of substring

    Returns:
        None
    """
    for substring in cartesian_product("ACGT", k):
        print(len(re.findall(f'(?={substring})', dna)), end=' ')

# dna = fasta_file_parser("path")[0]
