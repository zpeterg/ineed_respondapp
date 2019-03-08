from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# port_stemmer = PorterStemmer()

def cleanIt(tup):
    rtn = ()
    for word in tup:
        # clean up the word
        word = word.strip().lower()
        # Add it to the list if it's not a 'stop word'
        if word not in stopwords.words('english') and word not in rtn:
            rtn += (wordnet_lemmatizer.lemmatize(word),)
            # rtn += (port_stemmer.stem(word),)
    return rtn

