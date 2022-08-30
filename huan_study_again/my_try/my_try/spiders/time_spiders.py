import scrapy


class TimeingSpider(scrapy.Spider):
    name = "timing"

    def start_requests(self):
        link_1 = scrapy.FormRequest("https://productionvn.akselos.com:9020/" \
                                    "training_time_predict_projects/loi.nguyen/" \
                                    "GE_Wind/127PB_Phase_3_full_model_v2?view=jobs&job_id=&page_index=0",
                                    formdata={'user': 'huandinh2022', 'pass': '27081996'})
        link_2 = scrapy.FormRequest("https://productionvn.akselos.com:9020/" \
                                    "training_time_predict_projects/loi.nguyen/" \
                                    "GE_Wind/127PB_Phase_3_full_model_v2?view=jobs&job_id=&page_index=1",
                                    formdata={'user': 'huandinh2022', 'pass': '27081996'})
        urls = [link_1.url, link_2.url]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"timing-{page}.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f"Saved {filename}")

