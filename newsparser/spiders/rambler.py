import scrapy
from scrapy.http import HtmlResponse
from ..items import NewsparserItem
from scrapy.loader import ItemLoader

class RamblerSpider(scrapy.Spider):
    name = "rambler"
    allowed_domains = ["rambler.ru"]
    start_urls = ["https://news.rambler.ru/"]

    def parse(self, response):
        xpath_text = '''
                   //a[contains(@href, "news.rambler.ru")
                     or contains(@href, "pogoda.rambler.ru")
                     or contains(@href, "finance.rambler.ru")
                     or contains(@href, "vfokuse.rambler.ru")]/@href
        '''

        news_links = response.xpath(xpath_text).getall()
        print(response.status, response.url)
        for link in news_links:
            yield response.follow(link, callback=self.news_parse)  # перейти по ссылке


    def news_parse(self, response):
        item = NewsparserItem()
        item['header'] = response.xpath("//h1/text()").get()

        item['source'] = response.xpath("//div[@data-news_media-desktop='content_block']//div//p//text()").get()

        item['url'] = response.url
        yield item
