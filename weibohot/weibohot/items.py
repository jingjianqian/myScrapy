# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibohotItem(scrapy.Item):
    # 热搜排名
    index = scrapy.Field()
    # 热搜关键字
    title = scrapy.Field()
    # 热搜点击数
    hit = scrapy.Field()
    # 热搜 新 热 沸 爆
    type = scrapy.Field()
    # 热搜连接
    hot_href = scrapy.Field()
    # 热搜明细
    hot_details = scrapy.Field()
    pass
