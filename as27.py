from nltk.parse.corenlp import CoreNLPDependencyParser
dep_parser = CoreNLPDependencyParser
parse, = dep_parser.raw_parse('the fast white tigerjumps over the selfish fox.')
print(parse.to_conll(4))