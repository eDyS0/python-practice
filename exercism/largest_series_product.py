from operator import mul
from functools import reduce


def slices(number, n):
    if n > len(number) or n < 1:
        raise ValueError("Error. Length argument doesn't fit the series")

    for index in range(len(number) + 1 - n):
        substring = []
        substring_index = index
        while len(substring) < n:
            substring.append(int(number[substring_index]))
            substring_index += 1
        yield substring


def largest_product(number, n):
    """ 05/07/17
    Given a string of digits, calculate the largest product for a contiguous
    substring of digits of length n.
    Used a previously made function, slices, in order to get all
    the substrings easily.

    number: string of digits
    n: length of the substring of digits
    return: largest product
    """

    if n > len(number):
        raise ValueError("n cannot be longer than number's length")
    if n == 0:
        return 1
    if not number.isdigit():
        raise ValueError("Only digits are accepted for the number string")
    if n < 0:
        raise ValueError("n cannot be equal or inferior to 0")

    slic = slices(number, n)
    result = 0
    for s in slic:
        result = max(result, reduce(mul, s, 1))
    return result
