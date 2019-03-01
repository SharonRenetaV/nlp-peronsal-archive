import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpusdir = 'newcorpus/'
newcorpus = PlaintextCorpusReader(corpusdir, '.*')