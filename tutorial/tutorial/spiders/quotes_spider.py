"""
************************** Our first class spider *********************
Spider are class you define and that Scrapy uses to scrape information from a website.
They must subclass Spider
Define the initial request to make
optionally how to follow links in a page
how to parse the downloaded page content to extract data
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    """
    name: identifies the Spider, must be unique, you can't set the same name for different Spider
    """
    name = 'quotes'

    def start_requests(self):
        """
        must
        :return: an iterable of Requests (you can return a list of request or a generator function), which Spider will
        begin to crawl from.
        Subsequent request will be generated successively from these initial requests
        """
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]

        # for url in urls:
        #     yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        """
        Handle the response downloaded for each of the request made.
        :param response: is an instance of TextResponse, that hold the page content and has further helpful methods to
        handle it
        The parse() method usually
        1. parses the response,
        2. extracting the scraped data as dicts
        3. finding new URLs to follow
        4. creating new requests( Requests) from them
        # """
        # page = response.url.split('/')[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Save file {filename}')
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }


