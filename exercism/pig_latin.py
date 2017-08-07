def translate(word):
    vowel = 'aeiou'
    if word and word[0] in vowel:
        return word + 'ay'
    elif word[1] not in vowel:
        return word[2:] + word[:2] + 'ay'
    else:
        return word[1:] + word[:1] + 'ay'
