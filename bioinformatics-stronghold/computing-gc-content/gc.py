"""
ID: GC
Title: Computing GC Content
URL: http://rosalind.info/problems/gc/
"""

def compute_gc_content(dna_string):
    """
    computes GC-content of dna_string (the percentage of its bases that are either cytosine or guanine).
    
    Args:
        dna_string {str}: DNA string
    
    Returns:
        int: GC-content of dna_string
    """
    gc = dna_string.count("G") + dna_string.count("C")
    gc_content = gc * 100 / len(dna_string)

    return gc_content


def fasta_file_parser(fasta_file_path):
    """
    Parses Fasta files.
    
    Args:
        fasta_file_path {str}: path of Fasta file
    
    Returns:
        dict: dictionary with id, dna pairs 
    """
    with open(fasta_file_path, "r") as fasta_file:
        dataset = fasta_file.readlines()

    dnas = {}
    
    for line in dataset:
        if line.startswith(">"):
            id = line[1:]
            dnas[id] = ""
        else:
            dnas[id] += line.strip()

    return dnas


def highest_gc_content(dnas):
    """
    Finds the highest GC content and prints its id followed by this GC content.
    
    Args:
        dnas {dict}: dict with id, dna pairs
    
    Returns:
        None
    """
    gc_contents = {id: compute_gc_content(gc_content) for (id, gc_content) in dnas.items()}

    max_id = max(gc_contents, key=lambda id: gc_contents[id])

    print(max_id.replace("\n", ""))
    print("%.6f" % gc_contents[max_id])
