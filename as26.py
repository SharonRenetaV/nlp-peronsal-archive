import grammar_check
tool = grammar_check.LanguageTool('en-GB')
sentence = 'i is playing'
matches = tool.check(sentence)
len(matches)
grammar_check.correct(text, matches)
