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
 
## Command line tools(命令行工具)
###命令工具文档简要说明

> scrapy -h

> Usage:

> scrapy <command> [options] [args]

> Available commands:

>  bench         Run quick benchmark test

>  fetch         Fetch a URL using the Scrapy downloader

>  genspider     Generate new spider using pre-defined templates

>  runspider     Run a self-contained spider (without creating a project)

>  settings      Get settings values

>  shell         Interactive scraping console

>  startproject  Create new project

>  version       Print Scrapy version

>  view          Open URL in browser, as seen by Scrapy

>  [ more ]      More commands available when run from project directory

command line主要分为global类型跟project-only类型，global命令不依赖项目，project-only必须在scrapy的项目下才能运行

#### 常见的global command:

* startproject  
 >scrapy startproject <project_name> [project_dir]
* genspider
> scrapy genspider [-t template] <name> <domain>
> (我就不翻译，怎么滴，谁叫我英文cow B)Create a new spider in the current folder or in the current project’s spiders folder, if called from inside a project. The <name> parameter is set as the spider’s name, while <domain> is used to generate the allowed_domains and start_urls spider’s attributes.
 Usage example:
>$ scrapy genspider -l <br> 
>Available templates:<br> 
>  basic<br> 
>  crawl<br> 
>  csvfeed<br> 
>  xmlfeed<br> 
>$ scrapy genspider example example.com<br> 
>Created spider 'example' using template 'basic'<br> 

$ scrapy genspider -t crawl scrapyorg scrapy.org
Created spider 'scrapyorg' using template 'crawl'
</p>
* setting
> 
* runspider

* shell

* fetch

* view

* version
 
常见的project-only command：

* crawl
* check
* list
* edit
* parse
* bench
 ## 数据解析
 > 前面大概学习了下数据抓取已经几个常用的command  tools（很多没写，需要就看文档咯）。安装Beautiful   