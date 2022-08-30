from urllib.request import urlopen
from bs4 import BeautifulSoup
"""
h speed is not necessarily an advantage in web
scraping, given that the speed of the network itself will almost always be your largest
bottleneck.
"""
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html5lib')

print(bs)
print("================================")
print(bs.h1)
print(bs.div)
bs_2 = BeautifulSoup(html.read(), 'lxml')
print(bs_2.head())
"""One of the disadvantages of lxml is that it has to be installed separately and depends
on third-party C libraries to function. """
"""
Another popular HTML parser is html5lib. Like lxml, html5lib is an extremely for‐
giving parser that takes even more initiative correcting broken HTML. It also
depends on an external dependency, and is slower than both lxml and html.parser.
Despite this, it may be a good choice if you are working with messy or handwritten
HTML sites.
"""