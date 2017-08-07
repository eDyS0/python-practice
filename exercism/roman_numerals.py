#!python3
# -*- coding: utf-8 -*-

"""
roman_neutrals.py on 25/07/2017
parameters: a 'normal' number
returns: the roman numeral conversion of the number
"""


def numeral(number):

    numerals = {
        'ones': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        'tens': ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        'hundreds': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        'thousands': ['', 'M', 'MM', 'MMM'],
    }

    nb_to_roman = []
    for idx in ['ones', 'tens', 'hundreds', 'thousands']:
        number, remainder = (number // 10, number % 10)
        nb_to_roman.append(numerals[idx][remainder])
    return ''.join(nb_to_roman[::-1])
