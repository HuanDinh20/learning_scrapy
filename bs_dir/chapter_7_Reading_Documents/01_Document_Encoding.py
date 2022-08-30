"""
*********************************** Ecoding in Action *************************
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

textPage = urlopen('https://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print('Before Encode:')
print(textPage.read()[:100])

textPage = urlopen('http://www.pythonscraping.com/' \
                   'pages/warandpeace/chapter1-ru.txt')
print('After Encode:')
print(str(textPage.read(), 'utf-8'))

print(' <> '*30)
print('BeautifulSoup:')
html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
content = bytes(content, 'UTF-8')
content = content.decode('UTF-8')
print(content[:100])
