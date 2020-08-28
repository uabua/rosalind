"""
ID: MPRT
Title: Finding a Protein Motif
URL: http://rosalind.info/problems/mprt/
"""

import requests
import re

URL = "http://www.uniprot.org/uniprot/{}.fasta"
MOTIF = re.compile(r"(?=(N[^P][ST][^P]))")

def get_locations(uniprot_id):
    """
    Finds locations in the protein string where the motif can be found.

    Args:
        uniprot_id {str}: UniProt Protein Database access ID

    Returns:
        {list}: list of locations
    """
    response = requests.get(URL.format(uniprot_id))
    protein = "".join(response.text.split('\n')[1:])

    return [symbol.start() + 1 for symbol in MOTIF.finditer(protein)]

def print_data(uniprot_ids):
    """
    For each protein possessing the N-glycosylation motif, prints given access ID followed 
    by a list of locations in the protein string where the motif can be found.

    Args:
        uniprot_ids {list}: list of UniProt Protein Database access IDs

    Returns:
        None
    """
    for id in uniprot_ids:
        locations = [str(location) for location in get_locations(id)] 
        # with map(str, get_locations(id)), I had empty string when motif was not in protein

        if locations:
            print(id)
            print(" ".join(locations))

def read_file(file_path):
    """
    Reads input file.

    Args:
        file_path {str}: path of input file

    Returns:
        list: content of the file
    """
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n') 
 
