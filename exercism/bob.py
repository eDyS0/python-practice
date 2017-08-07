def hey(sentence):
    sentence = sentence.rstrip()
    if sentence.isupper():
        return("Whoa, chill out!")
    if sentence.endswith('?'):
        return("Sure.")
    if not sentence:
        return("Fine. Be that way!")
    return("Whatever.")