"""
 BeautifulSoup and regular expres‐
sions go hand in hand when it comes to scraping the web. In fact, most functions that
take in a string argument (e.g., find(id="aTagIdHere")) will also take in a regular
expression just as well.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
 {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})

for image in images:
    print('<><><><><>')
    print(image['src'])

"""
Acessing Attributes
Often in web scraping you’re not looking for the content of a tag; you’re
looking for its attributes. This becomes especially useful for tags such as a, where the
URL it is pointing to is contained within the href attribute; or the img tag, where the
target image is contained within the src attribute.
"""
"""
Lambda Expressions:
If you have a formal education in computer science, you probably learned about
lambda expressions once in school and then never used them again.
"""