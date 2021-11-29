BOT_NAME = 'olx'
SPIDER_MODULES = ['olx.spiders']
NEWSPIDER_MODULE = 'olx.spiders'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
#COOKIES_ENABLED = False
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': '*/*',
'Cache-Control': 'no-cache',
'Host': 'www.olx.ua',
'accept-encoding': 'gzip, deflate',
'Connection': 'close',
'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}

# данные для доступа
CLIENT_ID = '120513'
CLIENT_SECRET = 'admhGMIsuLNt8qc4uSECRETKEY6ktf0ZXEWP2UtjKuyzMTiHE'
SCOPE = 'read write v2'

# файл хранит последние параметры токенов и token_type
JSON_DUMP = 'data/token_save.json'
ERROR_POST = 'data/error-body.log'
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware':None,
}

########################################################
#
#               Settings to InfluxDB
#
########################################################

HOST = 'localhost'
PORT = '238086'
USERNAME = 'user'
PASSW = 'secret'
DATABASE = 'database'
TABLES = 'olx'

# Driver path
DRIVER = '/root/driver/chrome/chromedriver'

