
BOT_NAME = 'promoprice'

SPIDER_MODULES = ['prom.spiders']
NEWSPIDER_MODULE = 'prom.spiders'
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    #'prom.middlewares.PromDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware':None,
}

ITEM_PIPELINES = {
    'prom.pipelines.PromPipeline': 300,
}

SAVE_RESULT_XLSX = "result.xlsx"
DATA_RESULT_CSV = "data/dataprice.csv"

BASE_DATA_XLSX = "export.xlsx"
BASE_DATA_CSV = "data/export.csv"

DATA_PRICE_CSV = "data/dataprice.csv"

# Report Error files
ERROR_CSV_TMP = "data/error-data-read.csv"
ERROR_CSV_TMP_SIZE = 1024 * 1024 * 10
ERROR_XLS_RESULT = "error-price.xlsx"
PATH_VALIDATOR_ERROR = 'data/validator.log'
VALIDATOR_ERROR = True
VALIDATOR_ERROR_LOG_SIZE = 1024 * 1024 * 2

