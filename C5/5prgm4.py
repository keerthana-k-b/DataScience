print("Keerthana K B \n23MCA039")

from nltk import ngrams
sentence = 'I reside in India'
n=3
trigrams = ngrams(sentence.split(),n)
for grams in trigrams:
    print(grams)