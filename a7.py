from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
swords = set(stopwords.words('english'))
f1 = open("text.txt")
line = f1.read()
words = line.split()
for r in words:
    if not r in swords:
        appendFile = open('filteredtext.txt','a')
        appendFile.write(" "+r)
        appendFile.close()