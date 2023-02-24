import scrapy

from workDaily.items import Captcha_codeItem


class WorkinghoursSpider(scrapy.Spider):
    name = "workingHours"
    allowed_domains = ["ame.primeton.com"]
    start_urls = [
        "https://ame.primeton.com/default/common/jsp/codeImage.jsp?name=verifyCode&imageHeight=21&length=4&type=number&timestamp=0.294451878200674"]
    login_url = "https://ame.primeton.com/default/org.gocom.abframe.auth.LoginManager.verifyCode.biz.ext"

    def parse(self, response, *args, **kwargs):
        print(2222222)
        print(response.text)
        pass
        # yield scrapy.Request(
        #     self.start_urls[0],
        #     callback=self.parse_login
        # )

    # 解析登录页面,得到验证码链接
    def parse_login(self, response):
        # item = Captcha_codeItem
        url = response.url  #.xpath('/html/body/img/@src').extract()
        yield scrapy.Request(
            url,
            callback=self.login
        )

    def login(self, response):
        print("2222222")
        print("2222222")
        print("2222222")
        print("2222222")
        print("2222222")
        print("2222222")
        print("2222222")
        print("2222222")
        print(response.text)
        print(11)
