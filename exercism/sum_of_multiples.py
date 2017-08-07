def sum_of_multiples(n, multiples):
    ''' 03/07/17
    Given a number, find the sum of all the multiples of particular numbers up to
    but not including that number.
    
    n: number
    multiples: list of multiples, i.e [3, 5]
    return: sum of every multiples of the numbers contained in the list
    '''
 
    result = {i for i in range(n) for j in multiples if i % j == 0}
    return(sum(result))