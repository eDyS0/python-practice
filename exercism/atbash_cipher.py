''' 03/07/17
Implementation of the Atbash cipher for the Latin alphabet.
code: the string to encode or decode

not too happy with my encode function - needs a rework
'''

import string

def encode(code):
    code = code.lower()
    result = [chr(ord(c) + (25 - (string.ascii_lowercase.index(c) * 2))) if c.isalpha() else c if c.isdigit() else ' ' for c in code]
    result = [c for c in result if c != ' ']
    for i in range(5, len(result) + 1, 6):
        result.insert(i, ' ')
    return(''.join(result))
    
def decode(code):
    return(''.join([chr(ord(c) + (25 - (string.ascii_lowercase.index(c) * 2))) if c.isalpha() else c if c.isdigit() else '' for c in code]))