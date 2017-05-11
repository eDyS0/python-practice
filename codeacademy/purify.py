"""
Define a function called purify that takes in a list of numbers,
removes all odd numbers in the list, and returns the result.
"""

def purify(numbers):
    purified_list = []
    for number in numbers:
        if number % 2 == 0:
            purified_list.append(number)
    return purified_list
