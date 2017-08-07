"""
Given a number determine whether or not it is valid per the Luhn formula.

Program is still incomplete (doesn't work for 2 testcases)
"""

import re


class Luhn(object):
    def __init__(self, stg):
        self.number = stg.replace(' ', '')

    def is_valid(self):
        if len(self.number) < 2:
            return False
        if re.match("^[\d]*$", self.number):
            result = [int(n) * 2 if int(n) < 5 else (int(n) * 2) - 9 for n in self.number[::2]]
            if len(self.number) % 2 != 0:
                result.append(int(self.number[len(self.number) - 1:]))
            print("091"[::2])
            if (sum(result) + sum([int(n) for n in self.number[1::2]])) % 10 == 0:
                return True
            else:
                return False
        else:
            return False
