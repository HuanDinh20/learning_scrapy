import scrapy
from scrapy import Request
from urllib import parse
from scrapy.loader import ItemLoader
from ..items import ExItem

class ManualSpider(scrapy.Spider):
    name = 'manual'
    allowed_domains = ['web']
    start_urls = ['https://quotes.toscrape.com/', ]

    def parse(self, response):
        next_selectors = response.xpath('//*[contains(@class, "next")]//a//@href')
        for url in next_selectors.extract():
            yield Request(parse.urljoin(response.url, url), callback=self.parse,
                          dont_filter=True)

        item_selectors = response.xpath('//*[contains(@class, "quotes")]//span//a//@href')
        for url in item_selectors.extract():
            yield Request(parse.urljoin(response.url,url), callback=self.getItem,
                          dont_filter=True)

    def getItem(self, response):
        ld = ItemLoader(item=ExItem, response=response)
        ld.add_xpath('author', "//*[contain(@class, 'author-title')]//text()")
        self.total_scrapes += 1
        print('Total scrapes >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>:', self.total_scraped)
        return ld.load_item()
