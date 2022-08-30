"""
Creating flexible and modifiable website layout types doesn’t do much good if you
still have to locate each link you want to scrape by hand.
This section shows how to incorporate these methods into a well-structured and
expandable website crawler that can gather links and discover data in an automated
way.
"""
"""
***************************************** Crawling Sites Through Search *********************************
One of the easiest ways to crawl a website is via the same method that humans do:
using the search bar.
several key points make this surprisingly trivial:
1. Most sites retrieve a list of search results for a particular topic by passing that topic as a string through a 
parameter in the URL
2. After searching, most sites present the resulting page as an identifiable list of links.
3. Each result link is either a relative URL or an absolute URL 
4. After you’ve located and normalized the URLs on the search page, you’ve suc‐
cessfully reduced the problem to the example in the previous section—extracting
data from a page, given a website format.
"""
import requests
from bs4 import BeautifulSoup


class Content:
    """Common base class for all articles/pages"""

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url

    def print(self):
        """
         Flexible printing function controls output
        """
        print("New article found for topic: {}".format(self.topic))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))
        print("URL: {}".format(self.url))


class Website:
    """Contains information about website strutures"""

    def __init__(self, name, url, searchUrl, resultListing,
                resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl  # defines where to go to get results
        self.resultListing = resultListing  # box hold information about each result
        self.resultUrl = resultUrl  # defines the tags inside resultListing
        self.absoluteUrl = absoluteUrl  # a boolean, absolute or relative
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def search(self, topic, site):
        """
        Search a given website for a given topic and records all the pages found
        """
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)

        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            if site.absoluteUrl:
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print("Something was wrong with that page or URL. Skipping")
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, title, body, url)
                content.print()


crawler = Crawler()
siteData = [
    ['O\'Reilly Media', 'https://oreilly.com',
     'https://ssearch.oreilly.com/?q=', 'article.product-result',
     'p.title a', True, 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com',
     'http://www.reuters.com/search/news?blob=',
     'div.search-result-content', 'h3.search-result-title a',
     False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
     'https://www.brookings.edu/search/?s=',
     'div.list-content article', 'h4.title a', True, 'h1', 'div.post-body']
]

sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3],
                         row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']

for topic in topics:
    print('Getting information about: ', topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
