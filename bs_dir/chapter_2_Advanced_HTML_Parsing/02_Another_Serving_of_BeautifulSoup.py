from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

"""
Using this BeautifulSoup object, you can use the find_all function to extract a
Python list of proper nouns found by selecting only the text within <span
class="green"></span> tags 
"""

name_list = bs.findAll('span', {'class': 'green'})

for name in name_list:
    print(name.get_text())

"""
When to use get_text()? When to preseve Tags?
.get_text() strips all tags from the document you are working
with and returns a Unicode string containing the text only. 
Keep in mind that it’s much easier to find what you’re looking for
in a BeautifulSoup object than in a block of text. 
Call‐
ing .get_text() should always be the last thing you do, immedi‐
ately before you print, store, or manipulate your final data. In
general, you should try to preserve the tag structure of a document
as long as possible.
"""

"""
find()
find_all()
are the two functions you will likely use the
most. With them, you can easily filter HTML pages to find lists of desired tags, or a
single tag, based on their various attributes
"""
print(' = = = = = = ')
print(bs.find_all(['h1', 'h2', 'h3', 'h4']))
print('=========')
print(bs.find_all('span', {'class': {'green', 'red'}}))
print('<><><><><> <><><><><> <><><><><>')
nameList = bs.find_all(text='the prince')
print(nameList)

print(' - - - - - -')
title = bs.find(id='title')
print(title)