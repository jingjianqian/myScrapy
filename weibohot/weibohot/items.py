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


class StarsItem(scrapy.Item):
    # 名字
    name = scrapy.Field()
    # 头像
    avatar = scrapy.Field()
    # 地区
    region = scrapy.Field()
    # 简介
    introduction = scrapy.Field()
    # 职业
    job = scrapy.Field()
    # 生日
    birthday = scrapy.Field()
    # 身高
    height = scrapy.Field()
    # 体重
    weight = scrapy.Field()
    # 国籍
    country = scrapy.Field()
    # 别名
    alias = scrapy.Field()
    # 名族
    nationality = scrapy.Field()
    # 出生地
    birthplace = scrapy.Field()
    # 毕业院校
    williams_college = scrapy.Field()
    # 星座
    constellation = scrapy.Field()
    # 经纪公司
    jyp = scrapy.Field()
    # 性别
    sex = scrapy.Field()
    # 血型
    blood_type = scrapy.Field()