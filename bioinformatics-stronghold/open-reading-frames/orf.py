"""
ID: ORF
Title: Open Reading Frames
URL: http://rosalind.info/problems/orf/
"""

import re

# RNA codon table
rna_codon_dict = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "UAU": "Y", "UAC": "Y",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I",
    "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "UAA": "Stop", "UAG": "Stop", "UGA": "Stop"
}

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

def complement_strand(dna):
    """
    Finds the reverse complement of a dna.
    
    Args:
        dna {str}: DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T')
    
    Returns:
        str: the reverse complement string of a 
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

def codons(rna):
    """
    Splits rna into codons.

    Args:
        rna {str}: RNA string

    Returns:
        list: codons
    """
    return [rna[index:index+3] for index in range(0, len(rna), 3) if len(rna[index:index+3]) == 3]

def protein_from_orfs(dna):
    """
    Finds every distinct candidate protein string that can be translated from ORFs of dna.

    Args:
        dna {str}: DNA string

    Returns:
        set: candidate proteins
    """
    rna = dna.replace("T", "U")
    reverse_complement_rna = complement_strand(dna).replace("T", "U")

    candidate_proteins = set()
    
    for strand in [rna, reverse_complement_rna]:
        for index in [m.start() for m in re.finditer('AUG', strand)]:
           codons_list = codons(strand[index:])
           protein = ""

           if any(rna_codon_dict[codon] == "Stop" for codon in codons_list):
               for codon in codons_list:
                   symbol = rna_codon_dict[codon]

                   if symbol != "Stop":
                       protein += symbol
                   else:
                       candidate_proteins.add(protein)
                       break

    return candidate_proteins

def print_candidate_proteins(candidate_proteins):
    """
    Prints items of candidate_proteins.

    Args:
        candidate_proteins {set}: candidate proteins

    Returns:
        None
    """
    for protein in candidate_proteins:
        print(protein)
        
