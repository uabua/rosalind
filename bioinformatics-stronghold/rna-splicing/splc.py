"""
ID: SPLC
Title: RNA Splicing
URL: http://rosalind.info/problems/splc/
"""

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

# after parsing fasta file, we know that first is a dna string and others are introns
# dnas = fasta_file_parser("path")
# dna = dnas[0]
# introns = dnas[1:]

def splicing(dna, introns):
    """
    Deletes introns in dna. 

    Args:
        dna {str}: DNA string
        introns {list}: list of introns

    Returns:
        str: spliced dna
    """
    for intron in introns:
        dna = dna.replace(intron, '')

    return dna

def dna_to_rna(dna_string):
    """
    Transcribes dna_string to rna_string.
    
    Args:
        dna_string {str}: DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T')
    
    Returns:
        str: rna_string where 'T' is replaced by 'U'
    """
    rna_string = dna_string.replace("T", "U")

    return rna_string

def rna_to_protein(rna_string):
    """
    Translates rna_string into protein.
    
    Args:
        rna_string {str}: RNA string
    
    Returns:
        str: the protein sting if rna_string is valid, warning message if rna_string is not valid
    """
    codons = [rna_string[index:index+3] for index in range(0, len(rna_string), 3)]

    protein_string = ""

    for codon in codons:
        symbol = rna_codon_dict[codon]

        if symbol != "Stop":
            protein_string += symbol
        elif symbol == "Stop":
            return protein_string
        else:
            return "RNA string is not correct!"

