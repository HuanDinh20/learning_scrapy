import scrapy


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['www.thegioididong']
    start_urls = ['http://www.thegioididong/']

    def parse(self, response):
        pass
