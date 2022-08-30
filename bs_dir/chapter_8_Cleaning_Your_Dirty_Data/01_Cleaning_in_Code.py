"""
Just as you write code to handle overt exceptions, you should practice defensive cod‐
ing to handle the unexpected.
In linguistics, an n-gram is a sequence of n words used in text or speech. When doing
natural language analysis, it can often be handy to break up a piece of text by looking
for commonly used n-grams, or recurring sets of words that are often used together.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getNgrams(content, n):
    content = content.split(' ')
    output = []
    for i in range(len(content) - n + 1):
        output.append(content[i:i + n])
    return output


html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')

content = bs.find('div', {'id': 'mw-content-text'}).get_text()
n_grams = getNgrams(content, 2)

print(n_grams)
print('2-grams count is:', len(n_grams))

"""
without cleaning data, the output sometime looklike 
['Terminology\nSUDOC', '(France)\n1\n\n\n.\n\n\n\n\n\nRetrieved'], ['(France)\n1\n\n\n.\n\n\n\n\n\nRetrieved', 'from']
Using regular expressions to remove escape characters (such as \n) and filtering to
remove any Unicode characters,
"""
import re


def getNgramsClean(content, n):
    content = re.sub(r'\n|[[\d+\]]', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    content = content.split(' ')
    content = [word for word in content if word != '']
    output = []
    for i in range(len(content) - n + 1):
        output.append(content[i:i + n])
    return output


content = bs.find('div', {'id': 'mw-content-text'}).get_text()
n_grams = getNgramsClean(content, 2)
print(' = = = = = ' * 20)
print(n_grams)
print('Cleaner things')
print('2-grams count is:', len(n_grams))
print(' = = == ' * 20)
