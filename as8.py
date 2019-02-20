import nltk
from nltk.tokenize import word_tokenize
sentence = word_tokenize('MSD was the key player of todays match')
nltk.pos_tag(sentence)