import nltk
from nameparser.parser import HumanName
def get_human_names(text)
tokens = nltk.tokenize.word_tokenize(text)
pos = nltk.pos_tag(tokens)
sentence = nltk.ne_chunk(pos,binary = false)
person_list = []
name = ""
for subtree in sentence.subtrees(filter = lambda t: t.node =='PERSON')
    for leaf in subtree.leaves():
        person.append(leaf[0])
    if len(person) > 1:
        name += part + ''
    if name[: 1] not in person_list
        person_list.append(name[: -1])
    name = ''
person = []
return(person_list)