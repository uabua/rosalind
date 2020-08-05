"""
My solution to Rosalind problem 'Calculating Expected Offspring'

ID: IEV
Title: Calculating Expected Offspring
URL: http://rosalind.info/problems/iev/
"""

# 1. P(AA-AA) = 1 (AA, AA, AA, AA) = 4/4
# 2. P(AA-Aa) = 1 (AA, AA, Aa, Aa) = 4/4
# 3. P(AA-aa) = 1 (Aa, Aa, Aa, Aa) = 4/4
# 4. P(Aa-Aa) = 0.75 (AA, Aa, Aa, aa) = 3/4
# 5. P(Aa-aa) = 0.5 (Aa, Aa, aa, aa) = 2/4
# 6. P(aa-aa) = 0 (aa, aa, aa, aa) = 0/4
probabilities = [1, 1, 1, 0.75, 0.5, 0]

def get_expected_offspring(couples_string):
    """
    Counts the expected number of offspring displaying the dominant phenotype in the next generation, 
    under the assumption that every couple has exactly two offspring.

    Args:
        couples_string {str}: number of couples in a population possessing each genotype pairing for a given factor

    Returns:
        float: expected offspring
    """

    couples = map(int, couples_string.split())
    return sum([2 * probability * couple for probability, couple in zip(probabilities, couples)])
        