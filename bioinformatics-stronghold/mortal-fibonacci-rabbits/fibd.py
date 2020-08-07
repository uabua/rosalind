"""
My solution to Rosalind problem 'Mortal Fibonacci Rabbits'

ID: FIBD
Title: Mortal Fibonacci Rabbits
URL: http://rosalind.info/problems/fibd/
"""

def total_wabbits(months, lifespan):
    """
    Caunts the total number of pairs of rabbits that will remain after the specific(months) month
     if all rabbits live for some(lifespan) months.

    Args:
        months {int}: number of months
        lifespan {int}: lifespan in months

    Returns:
        int: The total number of pairs of rabbits.
    """
    previous = [1] + (lifespan - 1) * [0]

    for month in range(2, months + 1):
        next = sum(previous[1:])
        previous = [next] + previous[:-1]

    return sum(previous)

