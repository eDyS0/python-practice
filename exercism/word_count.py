def word_count(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace('\n', ' ')
    sentence = sentence.replace('\t', ' ')
    for letter in sentence:
        if letter != ' ' and letter.isalnum() == False:
            if letter == ',' or letter == '_':
                sentence = sentence.replace(letter, ' ')
            else:
                sentence = sentence.replace(letter, '')
    list_of_words = {}
    for word in sentence.split(' '):
        if word.isalnum() and word in list_of_words:
            list_of_words[word] += 1
        if word.isalnum() and word not in list_of_words:
            list_of_words[word] = 1
    return(list_of_words)