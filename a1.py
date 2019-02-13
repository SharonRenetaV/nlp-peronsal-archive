from nltk.corpus import stopwords
word_stop = set(stopwords.words('english'))
sample_words = ['i' 'ate' 'a' 'cake']
for words in sample_words:
     if word not in word_stop:
          print (word)