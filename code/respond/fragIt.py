from nltk.tokenize import word_tokenize


def fragIt(sent):
    return tuple(word_tokenize(sent))

