#install textblob, nltk

from textblob import TextBlob
b = TextBlob('bonjour')
b.dedect_language()