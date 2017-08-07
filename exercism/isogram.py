def is_isogram(word):
    for c in word:
        if c.isalpha() and word.lower().count(c) > 1:
            return(False)
    return(True)