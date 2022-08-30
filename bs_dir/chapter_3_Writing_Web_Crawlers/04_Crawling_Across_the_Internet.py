"""
“How do you build
Google?” My answer is always twofold: “First, you get many billions of dollars so that
you can buy the world’s largest data warehouses and place them in hidden locations
all around the world. Second, you build a web crawler.”
"""
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

page = set()
random.seed(datetime.datetime.now())


# Retrieve the list of all Internal Links found on a page
def getInternalLinks(bs, includeUrl):
    includeUrl = f'{urlparse(includeUrl).scheme}://{urlparse(includeUrl).netloc}'
    internalLinks = []
    print('<>' * 10)
    print(re.compile('^(/|.*' + includeUrl + ')'))
    # Find all links that begin with a "/"
    for link in bs.find_all('a',
                            href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    print(' = = ' * 10)
                    print(includeUrl + link.attrs['href'])
                    internalLinks.append(
                        includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
                    print(' + + + ' * 10)
                    print(link.attrs['href'])
    return internalLinks


# retrieve the list of all external links found on page

def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # Find all links that start with https that do not contain the current excludeUrl
    for link in bs.find_all('a',
                            href=re.compile('(https|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs,
                                     urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external link, looking around the site for one')
        domain = f'{urlparse(startingPage).scheme}://{urlparse(startingPage).netloc}'
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExteralOnly(startingPage):
    externalLinks = getRandomExternalLink(startingPage)
    print(f'Random external link is: {externalLinks}')
    followExteralOnly(externalLinks)


followExteralOnly('https://www.oreilly.com/')
