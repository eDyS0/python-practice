def decode(code):
    occurence = ''
    result = []
    for c in code:
        if c not in '1234567890':
            if len(occurence) == 0:
                result.append(c)
            else:
                result.append(c * int(occurence))
            occurence = ''
        else:
            occurence += c
    return ''.join(result)

def encode(code):
    if len(code) == 0:
        return ''
    codes = []
    for c in code:
        if not codes or codes[-1][1] != c:
            codes.append([1, c])
        else:
            codes[-1][0] += 1
    result = []
    for occurence, c in codes:
        if occurence > 1:
            result.append(str(occurence) + c)
        else:
            result.append(c)
    return ''.join(result)