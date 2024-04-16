import scrapy


class RamblerSpider(scrapy.Spider):
    name = "rambler"
    allowed_domains = ["rambler.ru"]
    start_urls = ["https://rambler.ru"]

    def parse(self, response):
        pass
