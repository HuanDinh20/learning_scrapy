import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ArticleitemsSpider(CrawlSpider):
    name = 'articleItems'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//*[@id="mw-content-text"]//text()').extract()

        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was last edited on', '')
        print('URL is: {}'.format(url))
        print('title is: {} '.format(title))
        print('text is: {}'.format(text))
        print('Last updated: {}'.format(lastUpdated))

"""
This new ArticleSpider extends the CrawlSpider class. Rather than providing a
start_requests function, it provides a list of start_urls and allowed_domains.
This tells the spider where to start crawling from and whether it should follow or
ignore a link based on the domain

A list of rules is also provided. This provides further instructions on which links to
follow or ignore (in this case, you are allowing all URLs with the regular expres‐
sion .*).
XPath
is often used when retrieving text content including text in child tags (for example, an
<a> tag inside a block of text)
 If you use the CSS selector to do this, all text within
child tags will be ignored.
"""

"""
rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items',
 follow=True)]

This line provides a list of Scrapy Rule objects that define the rules that all links
found are filtered through
 When multiple rules are in place, each link is checked
against the rules in order. The first rule that matches is the one that is used to deter‐
mine how the link is handled. If the link doesn’t match any rules, it is ignored.
 A Rule can be provided with six arguments:
 1. link_extractor: The only mandatory argument, a LinkExtractor object.
 2. callback: The function that should be used to parse the content on the page.
 3. follow: Indicates whether you want links found at that page to be included in a future
crawl. If no callback function is provided, this defaults to True (after all, if you’re
not doing anything with the page, it makes sense that you’d at least want to use it
to continue crawling through the site). If a callback function is provided, this
defaults to False. 
Despite all the flexible features of the LinkExtractor class, the most common argu‐
ments you’ll probably use are these:
1. allow: Allow all links that match the provided regular expression.
2. deny: Deny all links that match the provided regular expression.
"""

