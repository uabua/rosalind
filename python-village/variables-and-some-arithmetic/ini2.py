"""
My solution to Rosalind problem 'Variables and Some Arithmetic'

ID: INI2
Title: Variables and Some Arithmetic
URL: http://rosalind.info/problems/ini2/
"""

def square_of_the_hypotenuse(first_leg, second_leg):
    """
    Calculates the square of the hypotenuse of the right triangle.

    Args:
        first_leg {int}: leg of the right triangle
        second_leg {int}: leg of the right triangle

    Returns:
        int: the square of the hypotenuse of the right triangle
    """
    return first_leg**2 + second_leg**2
