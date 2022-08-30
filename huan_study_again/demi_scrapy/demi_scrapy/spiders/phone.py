import scrapy
from .. import items


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['www.thegioididong.com']
    start_urls = ['http://www.thegioididong.com/dtdd']

    def parse(self, response):
        # Request tới từng sản phẩm có trong danh sách các Macbook dựa vào href
        for item_url in response.css("li.item &gt; a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(item_url),
                                 callback=self.parse_macbook)  # Nếu có sản phẩm thì sẽ gọi tới function parse_macbook
