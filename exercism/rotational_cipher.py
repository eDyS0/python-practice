def rotate(text, key):
    s = ''
    for c in text:
        if c.islower():
            ascii_value = ord(c) + key
            if ascii_value > ord('z'):
                ascii_value -= 26
            s += chr(ascii_value)
        elif c.isupper():
            ascii_value = ord(c) + key
            if ascii_value > ord('Z'):
                ascii_value -= 26
            s += chr(ascii_value)
        else:
            s += c
    return(s)