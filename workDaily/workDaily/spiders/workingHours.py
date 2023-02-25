import re

import scrapy

from workDaily.items import Captcha_codeItem


class WorkinghoursSpider(scrapy.Spider):
    name = "workingHours"
    allowed_domains = ["ame.primeton.com"]
    start_urls = ["https://ame.primeton.com/", "https://ame.primeton.com/default/ame/clipview/com.primeton.eos.ame_common.wx_worktime.wx_wtime.biz.ext?year=2023&month=2"]
    login_url = "https://ame.primeton.com/default/org.gocom.abframe.auth.LoginManager.verifyCode.biz.ext"
    cookies = {
        "JSESSIONID": "4B217DA6BFEA1AF0D294B966541CEF9F",
        "cas-login": "\"CASTGC=TGT-34738-Bg3NGqnXmEafZEvoWvC4A7x5gTAMCtgc2Plg4vdtPapbBhbQlw\"",
        "jingjq": "%2Fdefault%2Fame%2Flogin%2Fimage%2Fyuanbao1.jpg"
    }

    def parse(self, response, *args, **kwargs):
        main_page_list = re.findall(r'href = "(.*?)"', response.text)
        print(main_page_list)
        cookies = "JSESSIONID=4B217DA6BFEA1AF0D294B966541CEF9F; cas-login=\"CASTGC=TGT-34738-Bg3NGqnXmEafZEvoWvC4A7x5gTAMCtgc2Plg4vdtPapbBhbQlw\"; jingjq=%2Fdefault%2Fame%2Flogin%2Fimage%2Fyuanbao1.jpg"
        if len(main_page_list) > 0:
            yield scrapy.Request(
                self.start_urls[1],
                cookies=self.cookies,
                dont_filter=True,
                callback=self.parse_login
            )
        else:
            print("cookie失效！！")

    # 解析登录页面,得到验证码链接
    def parse_login(self, response):
        # item = Captcha_codeItem
        print("ahahha")
        print(response.body)
        # url = response.url  #.xpath('/html/body/img/@src').extract()
        # yield scrapy.Request(
        #     url,
        #     callback=self.login
        # )

    def login(self, response):
        yield scrapy.Request(
            self.start_urls[0],
            cookies=self.cookies,
            callback=self.parse_login
        )
