import scrapy
from scrapy.http import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['web']
    start_urls = ['https://quotes.toscrape.com/login', ]

    def parse(self, response):
        csrf_token = response.xpath('//*[contains(@name, "csrf_token")]//@value').extract()
        return [
            FormRequest(
                "https://quotes.toscrape.com/login",
                formdata={"username": "a", "password": "a", "csrf_token": csrf_token[0]},
                callback=self.parse_item,
                dont_filter=True)]

    def parse_item(self, response):
        logout = response.xpath('//*[contains(@name, "logout")]')
        if len(logout) == 1:
            print("-------------------------------------------")
            print("Login success---")
