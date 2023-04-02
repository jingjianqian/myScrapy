class LoginPipeline:
    def process_item(self, item, spider):
        print("into LoginPipline")
        # print(item)
        # yield scrapy.Request(
        #     spider.login_url,
        #     dont_filter=True,
        #     headers=spider.headers,
        #     callback=spider.loginWithCount
        # )
