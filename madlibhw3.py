# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk
import random
from nltk.tokenize import sent_tokenize, word_tokenize

#get text2
sense = nltk.corpus.gutenberg.words('austen-sense.txt')[:150]

#taken from madlib_generatorP3.py
#puts spaces where they should be
def spaced(word):
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word

print("START*******\n\n")

#tags words with pos abbreviations
pos = nltk.pos_tag(sense)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PRP$":"a possessive pronoun"}
subprobs= {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1, "PRP$":.1}

final = []

#taken from madlib_generatorP3.py
#replaces words with inputted words
for (word, tag) in pos:
	if tag not in subprobs or random.random() > subprobs[tag]:
		final.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final.append(spaced(new_word))

#prints original text, followed by madlibbed text
print("\n\nEND*******")
print ("".join(spaced(w) for w in sense))
print ("\n", "".join(final))


