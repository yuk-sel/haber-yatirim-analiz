import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()


def kok_bul(metin):
    metin=metin.lower()
    kelimeler= word_tokenize(metin)
    kokler= [stemmer.stem(kelime) for kelime in kelimeler]
    return kokler


'''metin = "Russia's attacks caused damage in several regions"
print(kok_bul(metin))'''

