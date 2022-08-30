"""
In Chapter 8, you looked at breaking up text content into n-grams, or sets of phrases
that are n words in length. At a basic level, this can be used to determine which sets of
words and phrases tend to be most commonly used in a section of text. In addition, it
can be used to create natural-sounding data summaries by going back to the original
text and extracting sentences around some of these most popular phrases.

"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter


def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation + string.whitespace) for word in sentence]
    # I have a pen, i and a is a word with len == 1
    sentence = [word for word in sentence if len(word) > 1
                or (word.lower() == 'a') or (word.lower() == 'i')]
    return sentence


def cleanInput(content):
    content = content.upper()
    # delete \n pattern
    content = re.sub('\n', '', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('.')
    return [cleanSentence(sentence) for sentence in sentences]


def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content) - n + 1):
        output.append(content[i:i + n])
    return output


def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram in
                     getNgramsFromSentence(sentence, 2)]
        ngrams_list.extend(newNgrams)
        ngrams.update(newNgrams)
    return ngrams


content = str(
    urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = getNgrams(content, 2)
print(ngrams)

"""
Of these 2-grams, “the constitution” seems like a reasonably popular subject in the
speech, but “of the,” “in the,” and “to the” don’t seem especially noteworthy. How can
you automatically get rid of unwanted words in an accurate way?
"""


def isCommon(ngram):
    commonWords = ['THE', 'BE', 'AND', 'OF', 'A', 'IN', 'TO', 'HAVE', 'IT', 'I',
                   'THAT', 'FOR', 'YOU', 'HE', 'WITH', 'ON', 'DO', 'SAY', 'THIS', 'THEY',
                   'IS', 'AN', 'AT', 'BUT', 'WE', 'HIS', 'FROM', 'THAT', 'NOT', 'BY',
                   'SHE', 'OR', 'AS', 'WHAT', 'GO', 'THEIR', 'CAN', 'WHO', 'GET', 'IF',
                   'WOULD', 'HER', 'ALL', 'MY', 'MAKE', 'ABOUT', 'KNOW', 'WILL', 'AS',
                   'UP', 'ONE', 'TIME', 'HAS', 'BEEN', 'THERE', 'YEAR', 'SO', 'THINK',
                   'WHEN', 'WHICH', 'THEM', 'SOME', 'ME', 'PEOPLE', 'TAKE', 'OUT', 'INTO',
                   'JUST', 'SEE', 'HIM', 'YOUR', 'COME', 'COULD', 'NOW', 'THAN', 'LIKE',
                   'OTHER', 'HOW', 'THEN', 'ITS', 'OUR', 'TWO', 'MORE', 'THESE', 'WANT',
                   'WAY', 'LOOK', 'FIRST', 'ALSO', 'NEW', 'BECAUSE', 'DAY', 'MORE', 'USE',
                   'NO', 'MAN', 'FIND', 'HERE', 'THING', 'GIVE', 'MANY', 'WELL']
    for word in ngram:
        if word in commonWords:
            return True
    return False


print(isCommon(ngrams))
