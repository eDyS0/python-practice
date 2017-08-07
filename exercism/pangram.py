def is_pangram(sentence):
    letters = set()
    (letters.add(letter.lower()) for letter in sentence if letter.isalpha() and letter not in letters)


    return True if len(letters) == 26 else False