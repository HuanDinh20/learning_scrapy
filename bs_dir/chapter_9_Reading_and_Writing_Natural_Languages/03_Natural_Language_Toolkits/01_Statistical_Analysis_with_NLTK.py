"""
NLTK is greate for generating statical information forword count, word frequency,  word diversity in sections of text
"""
from nltk import word_tokenize
from nltk import Text
from nltk.book import text6
from nltk import FreqDist

tokens = word_tokenize('Here is some not very interesting text')
text = Text(tokens)
print(tokens)
print(text)

print(FreqDist(text6).most_common(10))
print(FreqDist(text6)['Grail'])


"""
. You can create, search, and list 2-grams, 3-grams,...
extremely easily:
"""
from nltk import bigrams
bigram = bigrams(text6)
bigramDist = FreqDist(bigram)
print(bigramDist[('Sir', 'Robin')])


from nltk import ngrams

fourgrams  = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
fourgramsDist[('father', 'smelt', 'of', 'elderberries')]
