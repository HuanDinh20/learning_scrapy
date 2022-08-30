"""
Web crawlers would be fairly boring if all they did was hop from one page to the
other. To make them useful, you need to be able to do something on the page while
you’re there. Let’s look at how to build a scraper that collects the title, the first para‐
graph of content, and the link to edit the page (if available).
"""
"""
As always, the first step to determine how best to do this is to look at a few pages
from the site and determine a pattern. By looking at a handful of Wikipedia pages
(both articles and nonarticle pages such as the privacy policy page), the following
things should be clear:
1. All titles (on all pages, regardless of their status as an article page, an edit history
page, or any other page) have titles under h1 → span tags, and these are the only
h1 tags on the page. 
2. all body text lives under the div#bodyContent tag.
3. Edit links occur only on article pages. If they occur, they will be found in the
li#ca-edit tag, under li#ca-edit → span → a
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen(f'http://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            # We have encountered a new page
            newPage = link.attrs['href']
            print('-' * 20)
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)


getLinks('')
"""
********************** Different Patterns for Different Needs ****************

Obviously, some dangers are involved with wrapping multiple lines
in an exception handler. You cannot tell which line threw the
exception, for one thing. Also, if for some reason a page contains
an Edit button but no title, the Edit button would never be logged.
However, it suffices for many instances in which there is an order
of likeliness of items appearing on the site, and inadvertently miss‐
ing a few data points or keeping detailed logs is not a problem.

"""

"""
********************** Handling Redirects ****************
Redirects allow a web server to point one domain name or URL to a piece of content
at a different location. There are two types of redirects:
1. Server-side redirects, where the URL is changed before the page is loaded
2. Client-side redirects, sometimes seen with a “You will be redirected in 10 sec‐
onds” type of message, where the page loads before redirecting to the new one

Python 3.x, it handles redirects automatically
r = requests.get('http://github.com', allow_redirects=True)
Just be aware that, occasionally, the URL of the page you’re crawling might not be
exactly the URL that you entered the page on.

"""
