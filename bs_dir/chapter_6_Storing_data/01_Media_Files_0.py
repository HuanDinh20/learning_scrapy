"""
You can store media files in two main ways: by reference and by downloading the file
itself.
1. Store a file by reference by storing the URL where the file is located.
** Advantages:
    * Scrapers run much faster and require much less bandwidth when they don’t have
to download files.
    * You save space on your own machine by storing only the URLs
    * It is easier to write code that stores only URLs and doesn’t need to deal with additional file downloads.
    * Lessen the load on the host server by avoiding large file downloads
** Disadvantage:
    * Embedding these URLs in your own website or application is known as hotlink‐
ing, and doing it is a quick way to get you in hot water on the internet.
    * You do not want to use someone else’s server cycles to host media for your own
applications
    * The file hosted at any particular URL is subject to change
    * Real web browsers do not just request a page’s HTML and move on. They down‐
load all of the assets required by the page as well. Downloading files can help
make your scraper look like a human is browsing the site, which can be an
advantage.
"""

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')

imageLocation = bs.find('div', {'class': "pagelayer-wp-title-section"}).find('img')['src']
urlretrieve(imageLocation, r'A:\huan_shit\learning_scrapy\bs_dir\chapter_6_Storing_data\01logo.png')
"""
This works well if you need to download only a single file and know what to call it
and what the file extension is. But most scrapers don’t download a single file and call
it a day. 
"""
