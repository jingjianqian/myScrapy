# -*- coding: utf-8 -*-
import scrapy

from weibohot.items import WeibohotItem


class Weibohosprider01Spider(scrapy.Spider):
    name = 'weibohosprider01'
    #allowed_domains = ['s.weibo.com']
    base_url = 'https://s.weibo.com'
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot/']
    item = WeibohotItem()

    def parse(self, response):
        table = response.xpath('//table/tbody/tr')
        for tr in table:
            indexArr_temp = tr.xpath('./td[@class="td-01 ranktop"]/text()|./td[@class="td-01"]/text()')
            temp_hit = tr.xpath('./td[@class="td-02"]/span/text()')
            temp_hotType = tr.xpath('./td[@class="td-03"]/i/text()')
            self.item['index'] = indexArr_temp.extract_first() if len(indexArr_temp) > 0 else 'top'
            self.item['title'] = tr.xpath('./td[@class="td-02"]/a/text()').extract_first()
            self.item['hit'] = temp_hit.extract_first() if len(temp_hit) > 0 else '0'
            self.item['type'] = temp_hotType.extract_first() if len(temp_hotType) > 0 else '0'
            ifAdvice = self.item['type'] == '商'
            if ifAdvice:
                hot_href = self.item['hot_href'] = self.base_url + tr.xpath('./td[position()=2]/a/@href_to').extract_first()
            else:
                hot_href = self.item['hot_href'] = self.base_url + tr.xpath('./td[position()=2]/a/@href').extract_first()

            yield scrapy.Request(url=hot_href, callback=self.parse_detail, meta={'item': self.item})
            # print(111111, hot_href)
            # yield from response.follow_all(hot_href, self.parse_detail, dont_filter=True)
            # yield {
            #     'index': self.item['index'],
            #     'title': self.item['title'],
            #     'hit': self.item['hit'],
            #     'type': self.item['type'],
            #     'hot_href': self.item['hot_href'],
            #     'hot_details': self.item['hot_details']
            # }

    def parse_detail(self, response):
        self.item['hot_details'] = response.xpath('//html').extract()
        yield self.item
        # print(response.header)
        # print()
        # yield {
        #     'index': self.item['index'],
        #     'title': self.item['title'],
        #     'hit': self.item['hit'],
        #     'type': self.item['type'],
        #     'hot_href': self.item['hot_href'],
        #     'hot_details': response.xpath('//div[@class=m-con-l]')
        # }

    def getWeiBoHotDatas(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, meta={'item': self.item})
