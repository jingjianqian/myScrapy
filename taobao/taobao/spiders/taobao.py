import scrapy
from bs4 import  BeautifulSoup

class taobap(scrapy.Spider):
    name = 'taobao'

    def start_requests(self):
        urls = [
            "https://shopsearch.taobao.com/search?app=shopsearch",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_html)  # url为请求地址，self.function为制定解析函数

    def parse_html(self,response):
        page = response.body
        print(page)
        print('asdf')
        # soup = BeautifulSoup(
        #     page,
        #     'lxml'
        # )
        # print(page)
        # level_one_hot_cat = soup.h2
        # print("start....")
        # print(level_one_hot_cat)
        # print("start....")


