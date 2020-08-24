"""
ID: IPRB
Title: Mendel's First Law
URL: http://rosalind.info/problems/iprb/
"""

def dominant_probability(homozygous_dominant, heterozygous, homozygous_recessive):
    """
    Calculates the probability that two randomly selected mating organisms will produce an 
    individual possessing a dominant allele (and thus displaying the dominant phenotype). 
    (number of organisms = homozygous_dominant + heterozygous + homozygous_recessive) 
    
    Args:
        homozygous_dominant {int}: number of homozygous dominant organisms
        heterozygous {int}: number of heterozygous organisms
        homozygous_recessive {int}: number of homozygous recessive organisms
    
    Returns:
        str: the probability that two randomly selected mating organisms will produce an 
        individual possessing a dominant allele
    """
    total = homozygous_dominant + heterozygous + homozygous_recessive

    probability_homozygous_dominant = homozygous_dominant / total
    probability_heterozygous = heterozygous / total
    probability_homozygous_recessive = homozygous_recessive / total


    probability = probability_homozygous_dominant # AA x anything
    probability += probability_heterozygous * (homozygous_dominant / (total - 1)) # Aa x AA
    probability += 0.75 * probability_heterozygous * ((heterozygous - 1) / (total -1)) # Aa x Aa
    probability += 2 * 0.5 * probability_heterozygous * (homozygous_recessive / (total -1)) # Aa x aa
    probability += probability_homozygous_recessive * (homozygous_dominant / (total - 1)) # aa x AA

    return "%.5f" % probability
