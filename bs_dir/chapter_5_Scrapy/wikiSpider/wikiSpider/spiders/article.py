import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'

    # start_urls = ['http://article/']

    def start_requests(self):
        urls = [
            'http://en.wikipedia.org/wiki/Python_'
            '%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python']
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print(f"URL is {url}")
        print(f"Title is {title}")


"""
The name of this class (ArticleSpider) is different from the name of the directory
(wikiSpider), indicating that this class in particular is responsible for spidering
through only article pages, under the broader category of wikiSpider, which you may
later want to use to search for other page types.

The name of this class (ArticleSpider) is different from the name of the directory
(wikiSpider), indicating that this class in particular is responsible for spidering
through only article pages, under the broader category of wikiSpider, which you may
later want to use to search for other page types.

The other key things to notice about this spider are the two functions
start_requests and parse. 

start_requests is a Scrapy - defined entry point to the program used to generate Request objects, that Scrapy uses to 
crawl the website

parse is a callback function defined by the user, and is passed to the Request object with callback = self.parse

"""
