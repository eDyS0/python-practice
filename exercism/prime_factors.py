def prime_factors(natural_nb):
    """
    prime_factors.py
    Compute the prime factors of a given natural number.
    returns a list of the prime factors of the given number
    """

    nb = 2
    prime_factors_list = []
    while nb * nb <= natural_nb:
        if natural_nb % nb:
            nb += 1
        else:
            natural_nb = natural_nb // nb
            prime_factors_list.append(nb)
    if natural_nb > 1:
        prime_factors_list.append(natural_nb)
    return prime_factors_list
