# -*- coding: utf-8 -*-
import scrapy

from weibohot.items import WeibohotItem


class Weibohosprider01Spider(scrapy.Spider):
    name = 'weibohosprider01'
    # allowed_domains = ['s.weibo.com']
    base_url = 'https://s.weibo.com'
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot/']

    def parse(self, response):
        table = response.xpath('//table/tbody/tr')
        for tr in table:
            item = WeibohotItem()
            indexArr_temp = tr.xpath('./td[@class="td-01 ranktop"]/text()|./td[@class="td-01"]/text()')
            temp_hit = tr.xpath('./td[@class="td-02"]/span/text()')
            temp_hotType = tr.xpath('./td[@class="td-03"]/i/text()')
            item['index'] = indexArr_temp.extract_first() if len(indexArr_temp) > 0 else 'top'
            item['title'] = tr.xpath('./td[@class="td-02"]/a/text()').extract_first()
            item['hit'] = temp_hit.extract_first() if len(temp_hit) > 0 else '0'
            item['type'] = temp_hotType.extract_first() if len(temp_hotType) > 0 else '0'
            ifAdvice = item['type'] == '商'
            if ifAdvice:
                hot_href = item['hot_href'] = self.base_url + tr.xpath('./td[position()=2]/a/@href_to').extract_first()
            else:
                hot_href = item['hot_href'] = self.base_url + tr.xpath('./td[position()=2]/a/@href').extract_first()
            yield scrapy.Request(url=hot_href, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        self.base_url
        item = response.meta['item']
        item['hot_details'] = response.xpath('//html').extract()
        yield item

    def getWeiBoHotDatas(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, meta={'item': self.item})
