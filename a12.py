import nltk
s = "i can't do this now, because i'm so tired. @ 19 sd"
words = nltk.word_tokenize(s)
words=[word.lower() for word in words if word.isalpha()]
print (words)