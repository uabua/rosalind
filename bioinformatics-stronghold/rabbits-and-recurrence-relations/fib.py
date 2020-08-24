"""
ID: FIB
Title: Rabbits and Recurrence Relations
URL: http://rosalind.info/problems/fib/
"""

def count_rabbits(month, pair):
    """
    Counts the total number of rabbit pairs that will be present after n(month) months, if we begin with 1 pair and 
    in each generation, every pair of reproduction-age rabbits produces a litter of k(pair) rabbit pairs 
    (instead of only 1 pair).
    
    Args:
        month {int}: number of months
        pair {int}: number of pairs
    
    Returns:
        int: total number of rabbit pairs
    """
    if month == 1 or month == 2:
        return 1
    else:
        return count_rabbits(month-1, pair) + count_rabbits(month-2, pair) * pair
