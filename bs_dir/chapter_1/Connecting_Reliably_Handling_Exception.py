from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

"""
The web is messy. Data is poorly formatted, websites go down, and closing tags go
missing. One of the most frustrating experiences in web scraping is to go to sleep
with a scraper running, dreaming of all the data you’ll have in your database the next
day—only to find that the scraper hit an error on some unexpected data format and
stopped execution shortly after you stopped looking at the screen. In situations like
these, you might be tempted to curse the name of the developer who created the web‐
site (and the oddly formatted data), but the person you should really be kicking is
yourself, for not anticipating the exception in the first place!
"""
try:
    html_trial = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    print('it worked')

"""
, if the page is retrieved successfully from the server, there is still the issue of
the content on the page not quite being what you expected. Every time you access a
tag in a BeautifulSoup object, it’s smart to add a check to make sure the tag actually
exists. If you attempt to access a tag that does not exist, BeautifulSoup will return a
None object. The problem is, attempting to access a tag on a None object itself will
result in an AttributeError being thrown.
"""


# print(AttributeError)
def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = get_title('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print("Could not find title")
else:
    print(title)
"""
This checking and handling of every error does seem laborious at first, but it’s easy to
add a little reorganization to this code to make it less difficult to write (and, more
important, much less difficult to read)
"""
