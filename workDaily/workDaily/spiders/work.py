import json
import re
from io import BytesIO

import scrapy
from PIL import Image
from scrapy.http.cookies import CookieJar

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
    check_status_api = 'https://ame.primeton.com/default/org.gocom.abframe.auth.LoginManager.verifyCode.biz.ext'  # 登录状态接口
    login_url = 'https://ame.primeton.com/default/sso.login?SSOLOGOUT=true'  # 登录页面
    captcha_code_url = "https://ame.primeton.com/default/common/jsp/codeImage.jsp?name=verifyCode&imageHeight=21&length=4&type=number"
    working_hours_api = 'https://ame.primeton.com/default/ame/clipview/com.primeton.eos.ame_common.wx_worktime.wx_wtime.biz.ext'
    cookie_jar = CookieJar()

    def __init__(self, name=None):  # 初始化一些数据
        super().__init__(name)
        self.headers = None
        self.cookies = None

    def start_requests(self):
        # TODO 目前写死cookie ,后续补充为登录后获取的cookie
        self.cookies = {
            "JSESSIONID": "AEB7E4B97C54E2CC874AC2AAD189795F",
            "cas-login": "CASTGC=TGT-24214-7ZvOaRW0mCro4imwaQdfktV5E2s93u4CqP2kafYUzO6H5aYegF",
            "jingjq": "%2Fdefault%2Fame%2Flogin%2Fimage%2Fyuanbao1.jpg"
        }

        # 先发送获取验证
        return [scrapy.Request(
                self.captcha_code_url,
                cookies=self.cookies,
                dont_filter=True,
            )]

    def parse(self, response, *args, **kwargs):
        # 获取cookie
        Cookie = response.headers.getlist('Set-Cookie')
        cookies = Cookie[0].decode(encoding='utf-8').split(";")
        cookies_dict = {}
        for i in cookies:
            tempList = i.split("=")
            if len(tempList) > 1:
                cookies_dict[tempList[0]] = tempList[1]
            else:
                cookies_dict[tempList[0]] = True
        print(cookies_dict)
        print("endCookie")
        captcha_data = response.body  # 验证码二进制信息
        img = Image.open(BytesIO(captcha_data))  # PIL读取二进制
        print("1231")
        print(img)
        catpath_path = './images/catpath1.png'
        img.save(catpath_path)  # 保存图片到文件
        myOcr = MyOcr(catpath_path)
        result = myOcr.OcrOneImage()
        formData = 'code=' + result + '&password=Jing.jianqian2334&flag=true&userid=jingjq'
        print("formData:" + formData)
        print('识别验证码为：' + result)
        print('开始以验证码登录')
        print(self.check_status_api + "?" + formData)
        if Cookie is not None:
            print('开始检测登录状态')
            yield scrapy.Request(
                self.check_status_api + "?" + formData,
                cookies=cookies_dict,
                dont_filter=True,
                callback=self.check_loginStatus
            )
        # 验证登录状态
        # redirect_url = re.findall(r'href = "(.*?)"', response.text)  # 获取url返回的script请求地址
        # print(len(redirect_url))
        # # 跳转到真正的主页
        # if len(redirect_url) > 0:
        #     print('开始进入主页')
        #     yield scrapy.Request(
        #         redirect_url[0],
        #         cookies=self.cookies,
        #         dont_filter=True,
        #         callback=self.parse_login
        #     )
        # else:
        #     print("获取登录页失败!")
        #     print("开始推送消息")
        #     # TODO 后续完善推送到小程序
        #     print("结束爬虫!")
        #     return None

    def parse_login(self, response):
        print("parse login")
        if response.status == 200:
            yield scrapy.Request(
                self.captcha_code_url,
                cookies=self.cookies,
                dont_filter=True,
                callback=self.login_with_captchaCode
            )

    def login_with_captchaCode(self, response):
        print('into loginWithCaptchaCode')
        # cookie_jar = CookieJar()
        # cookie_jar.extract_cookies(response, response.request)
        # print(len(cookie_jar))
        # Cookie = response.headers.getlist('Set-Cookie')
        # print(Cookie)
        # print("endCookie")
        # # cookiejar是类字典类型的,将它写入到文件中
        # with open('cookies.txt', 'w') as f:
        #     for cookie in cookie_jar:
        #         print(cookie)
        #         f.write(str(cookie) + '\n')
        #
        # print(self.cookies)
        # captcha_data = response.body  # 验证码二进制信息
        # img = Image.open(BytesIO(captcha_data))  # PIL读取二进制
        # catpath_path = './images/catpath.png'
        # img.save(catpath_path)  # 保存图片到文件
        # myOcr = MyOcr(catpath_path)
        # result = myOcr.OcrOneImage()
        # formData = 'code=' + result + '&password=Jing.jianqian2334&flag=true&userid=jingjq'
        # print("formData:" + formData)
        # print('识别验证码为：' + result)
        # print('开始以验证码登录')
        # print(self.login_api + "?" + formData)
        # yield scrapy.Request(
        #     self.login_api + "?" + formData,
        #     method='GET',
        #     body=formData,
        #     dont_filter=True,
        #     callback=self.check_loginStatus
        # )

    def check_loginStatus(self, response):
        print('into check_loginStatus')
        print(response.text)
        # captcha_data = response.body  # 验证码二进制信息
        # img = Image.open(BytesIO(captcha_data))  # PIL读取二进制
        # catpath_path = './images/catpath.png'
        # img.save(catpath_path)  # 保存图片到文件
        # myOcr = MyOcr(catpath_path)
        # result = myOcr.OcrOneImage()

        #
        # print('into check_loginStatus')
        # print(response.status)
        # if response.status == 200:
        #     print("登录请求正常")
        #     try:
        #         login_result = json.loads(response.text)
        #         print(login_result['status'])
        #         if login_result['status'] == '0':  #
        #             print('登录成功了，你想干嘛就干嘛了！')
        #
        #             # print(scrapy.Request.meta)
        #             # print(self.working_hours_api + "?year=2023&month=3")
        #             # yield scrapy.Request(
        #             #     self.working_hours_api + "?year=2023&month=3",
        #             #     cookies=self.cookies,
        #             #     dont_filter=True,
        #             #     callback=self.handles_working_hourse
        #             # )
        #         else:
        #             print('已经是登录状态，重新尝试！')
        #             # yield scrapy.Request(
        #             #     self.working_hours_api + "?year=2023&month=3",
        #             #     cookies=self.cookies,
        #             #     dont_filter=True,
        #             #     callback=self.handles_working_hourse
        #             # )
        #             # yield scrapy.Request(
        #             #     self.captcha_code_url,
        #             #     cookies=self.cookies,
        #             #     dont_filter=True,
        #             #     callback=self.login_with_captchaCode
        #             # )
        #     except Exception:
        #         print('完犊子了！')
        #         pass
        # else:
        #     print('登录失败思密达')

    def handles_working_hourse(self, response):
        print('into handles_working_hourse')
        print(response.text)
