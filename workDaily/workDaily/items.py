# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class WorkdailyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_url = scrapy.Field()
    image_name = scrapy.Field()
    pass


class CaptchaCodeItem(ImagesPipeline):
    image_url = scrapy.Field()
    image_name = scrapy.Field()
