import re
from io import BytesIO

import scrapy
from PIL import Image

from workDaily.spiders.utils.ocr import MyOcr

"""
    workingDaily代码重构 
    逻辑
    1、根据域名获取真正登录的url
    2、登录页带cookie访问
       2.1 如果cookie有效，开始进入功能请求
       2.2 如果cookie失效, 通过账户密码登录（需要识别验证码）
    3、进入功能也没
    4、TODO 待完善细节功能清单
"""


class WorkSpider(scrapy.Spider):
    name = "work"
    allowed_domains = ["ame.primeton.com"]
    start_urls = ["https://ame.primeton.com/",
                  "https://ame.primeton.com/default/common/jsp/codeImage.jsp?name=verifyCode&imageHeight=21&length=4&type=number"]  # 首页以及 验证码默认地址
    login_api = 'https://ame.primeton.com/default/org.gocom.abframe.auth.LoginManager.verifyCode.biz.ext'  # 登录接口
    captcha_code_url = "https://ame.primeton.com/default/common/jsp/codeImage.jsp?name=verifyCode&imageHeight=21&length=4&type=number"

    def __init__(self, name=None):  # 初始化一些数据
        super().__init__(name)
        self.headers = None
        self.cookies = None

    def start_requests(self):
        # TODO 目前写死cookie ,后续补充为登录后获取的cookie
        self.cookies = {
            "JSESSIONID": "4B217DA6BFEA1AF0D294B966541CEF9F",
            "cas-login": "CASTGC=TGT-34738-Bg3NGqnXmEafZEvoWvC4A7x5gTAMCtgc2Plg4vdtPapbBhbQlw",
            "jingjq": "%2Fdefault%2Fame%2Flogin%2Fimage%2Fyuanbao1.jpg"
        }
        self.headers = {
            'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Host': 'ame.primeton.com',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=A9B66A4196A9738F6C394580D2C70A6E'
        }
        return [scrapy.FormRequest(self.start_urls[0],
                                   formdata={'user': 'john', 'pass': 'secret'},
                                   callback=self.parse)]

    def parse(self, response, *args, **kwargs):
        redirect_url = re.findall(r'href = "(.*?)"', response.text)  # 获取url返回的script请求地址
        print(len(redirect_url))
        # 跳转到真正的主页
        if len(redirect_url) > 0:
            print('开始进入主页')
            yield scrapy.Request(
                redirect_url[0],
                cookies=self.cookies,
                dont_filter=True,
                headers=self.headers,
                callback=self.parse_login
            )
        else:
            print("获取登录页失败!")
            print("开始推送消息")
            # TODO 后续完善推送到小程序
            print("结束爬虫!")
            return None

    def parse_login(self, response):
        print("parse login")
        if response.status == 200:
            yield scrapy.Request(
                self.captcha_code_url,
                cookies=self.cookies,
                dont_filter=True,
                headers=self.headers,
                callback=self.login_with_captchaCode
            )

    def login_with_captchaCode(self, response):
        print('into loginWithCaptchaCode')
        captcha_data = response.body  # 验证码二进制信息
        img = Image.open(BytesIO(captcha_data))  # PIL读取二进制
        catpath_path = './images/catpath.png'
        img.save(catpath_path)  # 保存图片到文件
        myOcr = MyOcr(catpath_path)
        result = myOcr.OcrOneImage()
        formData = 'code=' + result + '&password=Jing.jianqian2334&flag=true&userid=jingjq'
        print('识别验证码为：' + result)
        print('开始以验证码登录')
        yield scrapy.FormRequest(
            self.login_api,
            method='POST',
            formdata=formData,
            callback=self.check_loginStatus
        )

    def check_loginStatus(self, response):
        print('into check_loginStatus')
        print(response)

