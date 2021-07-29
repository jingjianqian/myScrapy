import scrapy


class StartcollectorSpider(scrapy.Spider):
    name = 'startCollector'
    allowed_domains = ['www.baidu.com/s?wd=%E6%98%8E%E6%98%9F']
    start_urls = ['http://www.baidu.com/s?wd=%E6%98%8E%E6%98%9F/']

    def parse(self, response):
        pass
