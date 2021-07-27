# -*- coding: utf-8 -*-
import scrapy


class Weibohosprider01Spider(scrapy.Spider):
    name = 'weibohosprider01'
    allowed_domains = ['s.weibo.com/top/summary?cate=realtimehot']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot/']

    def parse(self, response):
        table = response.xpath('//table/tbody/tr')
        for tr in table:
            indexArr_temp = tr.xpath('./td[@class="td-01 ranktop"]/text()|./td[@class="td-01"]/text()')
            temp_hit = tr.xpath('./td[@class="td-02"]/span/text()')
            temp_hotType = tr.xpath('./td[@class="td-03"]/i/text()')
            yield {
                'index': indexArr_temp.extract_first() if len(indexArr_temp) > 0 else 'top',
                'title': tr.xpath('./td[@class="td-02"]/a/text()').extract_first(),
                'hit': temp_hit.extract_first() if len(temp_hit) > 0 else '0',
                'type': temp_hotType.extract_first() if len(temp_hotType) > 0 else '0',
                'hot_href': tr.xpath('./td[position()=2]/a/@href').extract_first()
                # # 热搜关键字
                # title = scrapy.Field()
                # # 热搜点击数
                # hit = scrapy.Field()
                # # 热搜 新 热 沸 爆
                # type = scrapy.Field()
                # # 热搜连接
                # hot_href = scrapy.Field()
            }

    # def parse(self, response):
    #     # print(response.body.decode())
    #     table_tr = response.xpath('//table/tbody/tr')
    #     indexArr = []
    #     title = []
    #     hits = []
    #     hotType = []
    #     hrefArry = []
    #     for trs in table_tr:
    #         indexArr_temp = trs.xpath('./td[@class="td-01 ranktop"]/text()|./td[@class="td-01"]/text()')
    #         if len(indexArr_temp) > 0:
    #             indexArr.append(indexArr_temp.extract_first())
    #         else:
    #             indexArr.append('top')
    #         title.append(trs.xpath('./td[@class="td-02"]/a/text()').extract_first())
    #         temp_hit = trs.xpath('./td[@class="td-02"]/span/text()')
    #         if len(temp_hit) > 0:
    #             hits.append(temp_hit.extract_first())
    #         else:
    #             hits.append('0')
    #         temp_hotType = trs.xpath('./td[@class="td-03"]/i/text()')
    #         # print(temp_hotType)
    #         if len(temp_hotType) > 0:
    #             hotType.append(temp_hotType.extract_first())
    #         else:
    #             hotType.append('0')
    #         hrefArry.append(trs.xpath('./td[position()=2]/a/@href').extract_first())
    #
    #     print(indexArr)
    #     return [indexArr, title, hits, hotType, hrefArry]

    def getWeiBoHotDatas(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse)
