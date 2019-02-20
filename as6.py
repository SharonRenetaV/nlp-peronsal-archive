from nltk.tokenize import
RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokenizer.tokenize('Alas! the Dog has dead.')
