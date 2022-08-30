import scrapy
from scrapy import FormRequest


class LogginFirstSpider(scrapy.Spider):
    name = 'loggin_first'
    allowed_domains = ['https://quotes.toscrape.com/login']
    start_urls = ['https://quotes.toscrape.com/login']

    def start_requests(self):
        return [
            FormRequest(self.start_urls[0], formdata={"username": "huandinh2022",
                                                "password": "27081996"}, callback=self.parse)]

    def parse(self, response):
        print("<<<<<<<<<<<<< 0 case: ", response.css("title::text").get())
        # for products in response.css("div.item"):
        #     link = products.css('a').attrib['href']
        #     print(">>>>>>>>>>>>>>> 1 case >>>>>>>>>>", link)
