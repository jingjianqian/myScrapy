import scrapy


class Weibohosprider01Spider(scrapy.Spider):
    name = 'weibohosprider01'
    allowed_domains = ['s.weibo.com/top/summary?cate=realtimehot']
    start_urls = ['http://s.weibo.com/top/summary?cate=realtimehot/']

    def parse(self, response):
        print(111, response)
