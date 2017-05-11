#! python3
# commaCode.py - takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted
# before the last item. (idea from automatetheboringstuffwithpython)
# Usage: python commaCode.py [1, 2, 3]

def commacode(list):
    commaStr = ''
    for i in list:
        if list.index(i) == len(list) - 1:
            commaStr += 'and '
            commaStr += str(i)
            break
        commaStr += str(i)
        commaStr += ', '
    print(commaStr)
