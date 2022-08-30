import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from ..items import ExItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls =('https://example.com', )

    # def parse(self, response):
    #     item = ExItem()
    #     item["Title"] = response.xpath("//div//h1/text()").extract()
    #     return item

    def parse(self, response):
        """ItemLoader helps coding management"""
        ld = ItemLoader(item=ExItem(), response= response)
        ld.add_xpath('Ex1', '//p', Join())
        ld.add_xpath('Ex2', '//p[1]/text()', MapCompose(lambda i: i.replace('.', ',')))
        ld.add_xpath('Ex3', '//p[1]/text()', MapCompose(str.strip))
        return ld.load_item()