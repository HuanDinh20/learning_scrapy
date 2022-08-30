import scrapy


class ExplorationSpider(scrapy.Spider):
    name = 'exploration'
    allowed_domains = ['productionvn.akselos.com:9020']
    start_urls = ['http://productionvn.akselos.com:9020/']

    def parse(self, response):
        pass
