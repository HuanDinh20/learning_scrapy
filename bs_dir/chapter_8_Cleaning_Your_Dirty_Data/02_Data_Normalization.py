"""
Data normalization is the process of ensuring that strings that are linguistic or logically equivalent to each other
such as the phone numbers (555) 123-4567 and 555.123.4567, are dis‐
played, or at least compared, as equivalent.

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string


def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation + string.whitespace)
                for word in sentence]
    sentence = [word for word in sentence if len(word) > 1
                or (word.lower() == 'a') or word.lower() == 'i']
    return sentence


def cleanInput(content):
    content = re.sub(r'/n|[[\d+\]]', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]


def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content) - n + 1):
        output.append(content[i:i + 1])
    return output


def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = []
    for sentence in content:
        ngrams.extend(getNgramsFromSentence(sentence, n))
    return ngrams


content = "Python features a dynamic type system and automatic memory management. " \
          "It supports multiple programming paradigms..."
print(cleanInput(content))

