"""
My solution to Rosalind problem 'Conditions and Loops'

ID: INI4
Title: Conditions and Loops
URL: http://rosalind.info/problems/ini4/
"""

def sum_of_odd_integers(start, end):
    """
    Counts the sum of all odd integers from start through end, inclusively.
    
    Args:
        start {int}: starting number in range
        end {int}: ending number in range
    
    Returns:
        int: the sum of all odd integers from start throigh end, inclisively
    """
    if start % 2 == 0:
        start += 1

    sum_of_numbers = 0

    for number in range(start, end+1, 2):
        sum_of_numbers += number

    return sum_of_numbers
    