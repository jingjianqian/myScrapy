# 遇到的问题与笔记
## 目前认为是要安装固定格式来
> 官网说明:中文为来自英语三级的G主翻译

<b>*name*</b>: identifies the Spider. It must be unique within a project, that is, you can’t set the same name for different Spiders.

<b>name</b>: 爬虫的识别名,项目中名字必须是唯一的.

<b>*start_requests()*</b>: must return an iterable of Requests (you can return a list of requests or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial requests.


<b>*start_requests()*</b>: 必须返回请求列表（可以返回一个存放请求地址的list组或者一个一般的方法），这样你的蜘蛛就能成功在这些默认的地址里进行抓取（瞎几把猜的了）

*<b>parse()</b>* a method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.

*<b>parse()</b>* 这个方法是每个处理请求返回的响应，响应参数是文本响应的实例，内容是是请求页面的内容，在方法里面可以进行更细致的处理（怎么样，我厉害吧）



## scrapy shell
 > scrapy的命令
 
 <code>scrapy shell "www.taobao.com"</code> 这个命令会抓取剁手网站，在命令行里可以对返回结果进行处理，比如紧接着<code>response.css('title'')</code>,作为一个猥琐程序员，你应该知道这句命令的大概意思了吧！！
 还有很多命令，我就不写了，因为这么多命令特么要写到什么时候？
 
* 数据解析
>     def parse(self, response):
>       for quote in response.css('div.quote'):
>           yield  {
>               'text':quote.css('span.text::text').extract_first(),
>               'author':quote.css('small.author::text').extract_first(),
>               'tags':quote.css('div.tags a.tag::text').extract(),
>           }
 parse方法改为上述,spider文件夹下命令行运行<code>scrapy crawl  quotes -o quotes.json</code>会把解析出来的内容保存到文件中    