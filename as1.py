from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
word_stop = set(stopwords.words('english'))
sample_words = ['i ate a cake']
word_tokens = word_tokenize(sample_words)
filtered_sentence=[w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for w in word_tokens:
     if word not in word_stop:
         filtered_sentence.append(w)
print (word_tokens)
print (filtered_sentence)