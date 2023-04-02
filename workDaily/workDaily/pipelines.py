# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os.path
import re

import ddddocr
import scrapy
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

from workDaily.items import CaptchaCodeItem


# useful for handling different item types with a single interface

class WorkdailyPipeline:
    def process_item(self, item, spider):
        print("into WorkdailyPipeline")
        print(item)
        spider.engine.crawl(
            Request(
                method='post',
                body=json.dump(item),
                url=spider.login_url,
                callback=self.custom_callback,
            ),
            spider,
        )

    def custom_callback(self):
        print('into custom_callback')
        pass


class LoginPipeline:
    def open_spider(self, spider):
        print("called loginPipline open_spider method when start spider")

    def process_item(self, item, spider):
        print("into LoginPipline")
        print(item)
        # yield scrapy.Request(
        #     spider.login_url,
        #     dont_filter=True,
        #     headers=spider.headers,
        #     callback=spider.loginWithCount
        # )

    def close_spider(self, spider):
        print("called loginPipline close_spider  when close spider")


class OcrPipline:
    def process_item(self, item, spider):
        print("into OcrPipline")
        print(item)
        ocr = ddddocr.DdddOcr()
        captchaCodeItem = CaptchaCodeItem()
        try:
            with open(
                    'D:\\data\\code\\back\\python\\scrapy\\myScrapy\\workDaily\\workDaily\\spiders\\images\\catpath.png',
                    'rb') as f:
                image = f.read()
                # print(ocr.classification(image))
                captchaCodeItem['code_value'] = ocr.classification(image)
                print(captchaCodeItem)
            return captchaCodeItem
        except IOError:
            print("验证码文件未找到！！")
        pass


class ImagePipeline(ImagesPipeline):
    image_name = 'catpath.png'

    def get_media_requests(self, item, info):
        print(item['image_name'])
        self.image_name = 'image_name'
        return scrapy.Request(item['image_url'])

    def file_path(self, request, response=None, info=None, *, item=None):
        base_path = os.path.join(get_project_settings().get('IMAGES_STORE'), 'catpath.png')
        print(os.path.exists(base_path))
        if os.path.exists(base_path):
            print("验证码文件存在")
            os.remove(base_path)
        else:
            print("验证码文件不存在")
        return 'catpath.png'

    # def process_item(self, item, spider):
    #     print("process_item")
    #     print(item)

    def item_completed(self, results, item, info):
        for x in results:
            print(x)
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

#
# class ImagesrenamePipeline(ImagesPipeline):
#
#     def file_path(self, request, response=None, info=None):
#         """
#         重写ImagesPipeline类的file_path方法
#         实现：下载下来的图片命名是以校验码来命名的，该方法实现保持原有图片命名
#         :return: 图片路径
#         """
#         image_guid = "test.png" # request.url.split('/')[-1]  # 取原url的图片命名
#         return image_guid
#
#     def get_media_requests(self, item, info):
#         """
#         遍历image_urls里的每一个url，调用调度器和下载器，下载图片
#         :return: Request对象
#         图片下载完毕后，处理结果会以二元组的方式返回给item_completed()函数
#         """
#         for image_url in item['image_urls']:
#             yield Request(image_url)
#
#     def item_completed(self, results, item, info):
#         """
#         将图片的本地路径赋值给item['image_paths']
#         :param results:下载结果，二元组定义如下：(success, image_info_or_failure)。
#         第一个元素表示图片是否下载成功；第二个元素是一个字典。
#         如果success=true，image_info_or_error词典包含以下键值对。失败则包含一些出错信息。
#          字典内包含* url：原始URL * path：本地存储路径 * checksum：校验码
#         :param item:
#         :param info:
#         :return:
#         """
#         image_paths = [x['path'] for ok, x in results if ok]
#         item['image_paths'] = image_paths
