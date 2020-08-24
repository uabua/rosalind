"""
ID: INI3
Title: Strings and Lists
URL: http://rosalind.info/problems/ini3/
"""

def special_slice(string, first_index, second_index, third_index, fourth_index):
    """
    Slices string from indices first_index through second_index and third_index through fourth_index (with space in between), 
    
    Args: 
        string {str}: a string of length at most 200 letters.
        first_index {int}: first index
        seond_index {int}: second index
        third_index {int}: third index
        fourth_indes {int}: fourth index
    
    Returns:
        str: special slice of given string
    """ 
    slice = f"{string[first_index:second_index+1]} {string[third_index:fourth_index+1]}"

    return slice
