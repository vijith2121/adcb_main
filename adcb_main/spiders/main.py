import scrapy
# from adcb_main.items import Product
from lxml import html

class Adcb_mainSpider(scrapy.Spider):
    name = "adcb_main"
    start_urls = ["https://example.com"]

    def parse(self, response):
        parser = html.fromstring(response.text)
        print("Visited:", response.url)
