def sieve(n):
    '''
    This program uses the Sieve of Eratosthenes to find all the primes from 2 
    up to a given number.
    n: number
    return: list of all the prime from 2 up to n
    '''
    
    result = {}
    for i in range(2, n+1):
        result[i] = 0
    for i in range(2, n+1):
        for j in range(2*i, n+1, i):
            if j % i == 0:
                result[j] = 1
    return [i for i in result if result[i] == 0]