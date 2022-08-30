"""
When might crawling an entire website be useful, and when might it be harmful?
Web scrapers that traverse an entire site are good for many things, including the fol‐
lowing:
Generating a site map:
Gathering data

Clearly, this is a situation that can blow up quickly. If every page has 10 internal links,
and a website is 5 pages deep (a fairly typical depth for a medium-size website), the the number of pages you need to
crawl is 10 ^5, or 100,000 pages, before you can be sure that you’ve exhaustively covered the website. Strangely enough,
although “5 pages deep and 10 internal links per page” are fairly typical dimensions for a website,
very few websites have 100,000 or more pages. The reason, of course, is that the vast
majority of internal links are duplicates.

To avoid crawling the same page twice, it is extremely important that all internal links
discovered are formatted consistently, and kept in a running set for easy lookups,
while the program is running. A set is similar to a list, but elements do not have a
specific order, and only unique elements will be stored, which is ideal for our needs.
Only links that are “new” should be crawled and searched for additional links:
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(pageUrl):
    global pages
    html = urlopen(f'https://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html, 'html.parser')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We encounter a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                get_links(newPage)


get_links('')

"""
A Warning Regarding Recursion
This is a warning rarely seen in software books, but I thought you
should be aware: if left running long enough, the preceding pro‐
gram will almost certainly crash.

"""