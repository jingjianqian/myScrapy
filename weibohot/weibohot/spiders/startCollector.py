import scrapy


class StartcollectorSpider(scrapy.Spider):
    name = 'startCollector'
    allowed_domains = ['www.baidu.com/s?wd=%E6%98%8E%E6%98%9F']
    start_urls = ['http://www.baidu.com/s?wd=%E6%98%8E%E6%98%9F/']

    def parse(self, response):

        start_contains = response.xpath('/html/body//div[@id="1"]//div[contains(@class,"op_exactqa_item")]//div')
        print(len(start_contains))
        print(len(start_contains.extract()))
        for starts_div in start_contains:
            # print(index)
            # print(starts_div)
            # avatar = starts_div.xpath('//p[@class="op_exactqa_item_img"]//img/@src').extract()
            # print(avatar)
            pass
        pass
