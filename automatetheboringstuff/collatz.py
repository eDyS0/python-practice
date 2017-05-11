#! python3
# collatz.py - Collatz Sequence (idea from automatetheboringstuffwithpython)
# Usage: python collatz.py <number>

import sys
def collatz(number):
    if number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1
    elif number % 2 == 0:
        print(number // 2)
        return number // 2

if len(sys.argv) != 2 or sys.argv[1].isnumeric() == False:
    print('Usage: python collatz.py <number>', end = '')
    exit()
    
if int(sys.argv[1]) > 0:
    nb = int(sys.argv[1])
    while nb != 1:
        nb = collatz(nb)
