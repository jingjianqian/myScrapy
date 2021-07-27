# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from weibohot.utils.mysql import MysqlUtil


class WeibohotMysqlPipeline:

    # 连接数据库
    def __init__(self):
        self.mysqlUtil = MysqlUtil()

    def process_item(self, item, spider):
        print(item)
        self.mysqlUtil.insertHotRecord(item)
        return item
