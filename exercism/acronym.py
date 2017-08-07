def abbreviate(sentence):
    """ 03/07/17
    Convert a phrase to its acronym.

    sentence: the phrase to convert
    returns the acronym
    """
    for c in sentence:
        if not c.isalpha():
            sentence = sentence.replace(c, ' ')
    return ''.join(i[0].upper() for i in sentence.split())
