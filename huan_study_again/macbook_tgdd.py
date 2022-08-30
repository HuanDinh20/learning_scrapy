import scrapy


class MacbookTgddSpider(scrapy.Spider):
    name = 'macbook_tgdd'
    allowed_domains = ['www.thegioididong.com']
    start_urls = ['http://www.thegioididong.com/']

    def parse(self, response):
        pass
