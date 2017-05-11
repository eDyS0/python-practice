"""
censory.py
Write a function called censor that takes two strings,
text and word, as input.
It should return the text with the word you chose replaced with asterisks.
"""

def censor(text, word):
    split_str = text.split()
    censor_list = []
    for words in split_str:
        if words == word:
            censor_list.append(len(word) * "*")
        else:
            censor_list.append(words)
    return " ".join(censor_list)
