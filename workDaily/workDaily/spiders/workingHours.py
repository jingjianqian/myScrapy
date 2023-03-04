import re

import scrapy

from workDaily.items import WorkdailyItem


class WorkinghoursSpider(scrapy.Spider):
    name = "workingHours"
    allowed_domains = ["ame.primeton.com"]
    captcha_code_url = [
        "https://ame.primeton.com/default/common/jsp/codeImage.jsp?name=verifyCode&imageHeight=21&length=4&type=number"]
    start_urls = ["https://ame.primeton.com/",
                  "https://ame.primeton.com/default/ame/clipview/com.primeton.eos.ame_common.wx_worktime.wx_wtime.biz.ext?year=2023&month=2"]
    login_url = "https://ame.primeton.com/default/org.gocom.abframe.auth.LoginManager.verifyCode.biz.ext"
    cookies = {
        "JSESSIONID": "4B217DA6BFEA1AF0D294B966541CEF9F",
        "cas-login": "\"CASTGC=TGT-34738-Bg3NGqnXmEafZEvoWvC4A7x5gTAMCtgc2Plg4vdtPapbBhbQlw\"",
        "jingjq": "%2Fdefault%2Fame%2Flogin%2Fimage%2Fyuanbao1.jpg"
    }

    def parse(self, response, *args, **kwargs):
        main_page_list = re.findall(r'href = "(.*?)"', response.text)
        cookies = "JSESSIONID=4B217DA6BFEA1AF0D294B966541CEF9F; cas-login=\"CASTGC=TGT-34738-Bg3NGqnXmEafZEvoWvC4A7x5gTAMCtgc2Plg4vdtPapbBhbQlw\"; jingjq=%2Fdefault%2Fame%2Flogin%2Fimage%2Fyuanbao1.jpg"

        headers = {
            'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
            'Accept': '*/*',
            'Host': 'ame.primeton.com',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=A9B66A4196A9738F6C394580D2C70A6E'
        }
        if len(main_page_list) > 0:
            yield scrapy.Request(
                self.start_urls[1],
                cookies=self.cookies,
                dont_filter=True,
                headers=headers,
                callback=self.parse_login
            )
        # else:
        #     item = WorkdailyItem()
        #     item['image_url'] = self.captcha_code_url[0]
        #     item['image_name'] = "Captcha_codeItem.png"
        #     return item

    # 解析登录页面,得到验证码链接
    def parse_login(self, response):
        # item = Captcha_codeItem
        item = WorkdailyItem()
        item['image_url'] = self.captcha_code_url[0]
        item['image_name'] = "Captcha_codeItem.png"
        yield item

    def login(self, response):
        yield scrapy.Request(
            self.start_urls[0],
            cookies=self.cookies,
            callback=self.parse_login
        )

    def loginWithCount(self, response):

        pass
