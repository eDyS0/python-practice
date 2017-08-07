def to_rna(dna):
    rna_rules = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    new_rna = ''
    for c in dna:
        if c in rna_rules: new_rna += rna_rules[c]
        else: return('')
    return(new_rna)