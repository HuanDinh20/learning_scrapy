import scrapy


class TitleSpider(scrapy.Spider):
    name = 'title'
    allowed_domains = ['productionvn.akselos.com:9020']
    start_urls = ['http://productionvn.akselos.com:9020/']

    def parse(self, response):
        pass
