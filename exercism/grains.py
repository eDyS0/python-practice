#!python3
# -*- coding: utf-8 -*-

"""
grains.py on 25/07/2017
refacto'd the code to be more pythonic :€ (also removed useless Exception and used ValueError)
"""


def on_square(nb):
    if nb < 1 or nb > 64:
        raise ValueError('number has to be between 1 and 64')
    return 2 ** (nb - 1)


def total_after(nb):
    if nb < 1 or nb > 64:
        raise ValueError('number has to be between 1 and 64')
    return sum([on_square(n) for n in range(1, nb + 1)])
