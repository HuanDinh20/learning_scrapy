"""
Although Scrapy is single threaded, it is capable of making ahnd handling many requests asynchronously. So it faster
bs4, although I have always been a firm believer that faster is not always better when
it comes to web scraping.
With that said, using Scrapy’s item pipeline can improve the speed of your web scra‐
per even further by performing all data processing while waiting for requests to be
returned, rather than waiting for data to be processed before making another request.
To create an item pipeline, revisit the settings.py file that was created at the beginning
of the chapter. You should see the following commented lines:
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
# 'wikiSpider.pipelines.WikispiderPipeline': 300,
#}
Uncomment the last three lines and replace with the following:
ITEM_PIPELINES = {
 'wikiSpider.pipelines.WikispiderPipeline': 300,
}
This provides a Python class, wikiSpider.pipelines.WikispiderPipeline, that will
be used to process the data, as well as an integer that represents the order in which to
run the pipeline if there are multiple processing classes.
"""