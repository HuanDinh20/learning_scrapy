"""
The most obvious approach is to write a separate web crawler or page parser for each
website. Each might take in a URL, string, or BeautifulSoup object, and return a
Python object for the thing that was scraped.
"""
import re
import urllib
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))

class Website:
    def __init__(self, name, url, titleTag,bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag


def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')


def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.find_all('p', {"class": "story-content"})
    body = 'n'.join([line.text for line in lines])
    return Content(url, title, body)


def scrapeReuters(url):
    bs = getPage(url)
    title = bs.find('title')
    lines = bs.find_all('p', {"class": "text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__"
                                       "nEccO body__base__22dCE body__large_body__FV5_X article-body__element__2p5pI"})
    body = 'n'.join([line.text for line in lines])
    return Content(url, title, body)


def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class', 'post-body'}).text
    return Content(url, title, body)


# url = 'https://www.brookings.edu/blog/future-development2018/01/26/delivering-inclusive-urban-access-3-uncomfortable' \
#       '-truths/ '
#
# content = scrapeBrookings(url)
# print('Title: {}'.format(content.title))
# print('URL: {}\n'.format(content.url))
# print('<>' * 10)
# print(content.body)
# print('<>' * 10)
# url = "https://www.washingtonpost.com/"
# content = scrapeNYTimes(url)
# print('Title: {}'.format(content.title))
# print('URL: {}\n'.format(content.url))
# print(content.body)
# print('*' * 10)
# url = "https://www.reuters.com/world/europe/ukraines-zelenskiy-calls-heavy-arms-eu-membership-russia-pounds-cities-2022-06-23/ "
# content = scrapeReuters(url)
# print('Title: {}'.format(content.title))
# print('URL: {}\n'.format(content.url))
# print(' = = ' * 10)
# print(content.body)
# print(' = = ' * 10)
"""
As you start to add scraper functions for additional news sites, you might notice a
pattern forming. Every site’s parsing function does essentially the same thing:
1. Selects the title element and extracts the text for the title
2. Selects the main content of the article
3. Selects other content items as needed
4. Returns a Content object instantiated with the strings found previously

"""
class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        Utility function used to get content string from a BeautifulSoup object and a selector
        Return an empty string if no object is found for the given selector
        """
        selectedElems = pageObj.select(selector)
        print('*'*20)
        print('selectedElems: ', selectedElems)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join(
                [elem.get_text() for elem in selectedElems]
            )
        return ''
    def parse(self, site, url):
        """
        Extract content from a given page URL
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                print('<>'*20)
                content.print()

crawler = Crawler()
siteData = [
['O\'Reilly Media', 'http://oreilly.com',
 'h1', 'section#product-description'],
['Reuters', 'http://reuters.com', 'h1',
 'div.StandardArticleBody_body_1gnLA'],
['Brookings', 'http://www.brookings.edu',
 'h1', 'div.post-body'],
['New York Times', 'http://nytimes.com',
 'h1', 'p.story-content']
]
websites = []
for row in siteData:
    print('- - - '*10)
    print('row:',row)
    websites.append(Website(row[0], row[1], row[2], row[3]))
    print('>'*25)
    print(websites)

crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
# crawler.parse(websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')


