from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
pss= PorterStemmer()
sentence = ["drivers drived the car fast"]
words=word_tokenize(sentence)
for w in words:
    print (w,"        "),pss.stem(w))