# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkdailyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Captcha_codeItem(scrapy.Item):
    image_url = scrapy.Field()
    image_name = scrapy.Field()
