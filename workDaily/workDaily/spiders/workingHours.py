import scrapy


class WorkinghoursSpider(scrapy.Spider):
    name = "workingHours"
    allowed_domains = ["ame.primeton.com"]
    start_urls = ["http://ame.primeton.com/"]

    def parse(self, response):
        pass
