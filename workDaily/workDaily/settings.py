# Scrapy settings for workDaily project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = "workDaily"

SPIDER_MODULES = ["workDaily.spiders"]
NEWSPIDER_MODULE = "workDaily.spiders"

HTTPERROR_ALLOWED_CODES = [301]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "workDaily (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

allow_redirects = True
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# 设置图片存储目录
IMAGES_STORE = ".\\images"  # os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    # "workDaily.middlewares.WorkdailySpiderMiddleware": 543,
    "workDaily.middlewares.MyUserAgentMiddleware": 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "workDaily.middlewares.WorkdailyDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "workDaily.pipelines.ImagePipeline": 299,
    "workDaily.pipelines.OcrPipline": 300,
    "workDaily.pipelines.LoginPipeline": 301,
    # "workDaily.pipelines.WorkdailyPipeline": 302
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# 是否启用日志
LOG_ENABLED = True

# 日志使用的编码
LOG_ENCODING = 'utf-8'

# 日志文件(文件名)
LOG_FILE = None

# 日志格式
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# 日志时间格式
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'

# 日志级别 CRITICAL, ERROR, WARNING, INFO, DEBUG
LOG_LEVEL = 'INFO'

# 如果等于True，所有的标准输出（包括错误）都会重定向到日志，例如：print('hello')
LOG_STDOUT = True

# 如果等于True，日志仅仅包含根路径，False显示日志输出组件
LOG_SHORT_NAMES = False
