import scrapy
class littleSpider(scrapy.Spider):
    name = 'myLittleSpider'
    def start_request(self):
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/1/',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        page = response.url.split("/")[-2]
        print("hello python!")
        filename = 'myspide-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)