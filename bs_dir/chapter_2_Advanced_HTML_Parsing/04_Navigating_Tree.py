"""
The find_all function is responsible for finding tags based on their name and
attributes. But what if you need to find a tag based on its location in a document?
That’s where tree navigation comes in handy
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.div.p)
print(" = = = = = = ==            = = = == = = = = = =")
"""
************** Dealing with children and other descendants *********************
In computer science and some branches of mathematics, you often hear about horri‐
ble things done to children: moving them, storing them, removing them, and even
killing them. Fortunately, this section focuses only on selecting them!

In general, BeautifulSoup functions always deal with the descendants of the current
tag selected
If you want to find only descendants that are children, you can use the .children
tag
"""

for child in bs.find('table', {'id': 'giftList'}).children:
    print(">><<><><><><><><><><><><><><><<><><><<><><")
    print(child)

"""
Dealing with siblings
The BeautifulSoup next_siblings() function makes it trivial to collect data from
tables, 
"""

for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print('+++++++ +++++++ +++++++')
    print(sibling)

"""
Dealing with parents
When scraping pages, you will likely discover that you need to find parents of tags
less frequently than you need to find their children or siblings. Typically, when you
look at HTML pages with the goal of crawling them, you start by looking at the top
layer of tags, and then figure out how to drill your way down into the exact piece of
data that you want. Occasionally, however, you can find yourself in odd situations
that require BeautifulSoup’s parent-finding functions, .parent and .parents.
"""
print('~~~~~~~~~~~~~~~                                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(bs.find('table', {'id': 'giftList'}).parent.get_text())