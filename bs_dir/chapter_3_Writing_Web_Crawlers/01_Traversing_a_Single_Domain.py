import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import datetime
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

"""
If you examine
the links that point to article pages (as opposed to other internal pages), you’ll see that
they all have three things in common:
• They reside within the div with the id set to bodyContent.
• The URLs do not contain colons.
• The URLs begin with /wiki/.
"""
for link in bs.find('div', {'id': 'bodyContent'}).find_all(
    'a', href = re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print('*************** ***************** *******************')
        print(link.attrs['href'])


random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html =urlopen(f"http://en.wikipedia.org{articleUrl}")
    bs = BeautifulSoup(html, 'html.parser')

    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)


