def distance(dna_1, dna_2):
    if len(dna_1) != len(dna_2):
        raise ValueError('The two sequences are not of equal lenghts.')
    return(sum(1 for i in range(len(dna_1)) if dna_1[i] != dna_2[i]))