"""
ID: PROT
Title: Translating RNA into Protein
URL: http://rosalind.info/problems/prot/
"""

#RNA codon table
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
