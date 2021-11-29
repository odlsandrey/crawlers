import logging

from scrapy import signals
from scrapy.utils.project import get_project_settings
from influxdb import InfluxDBClient

logger = logging.getLogger(__name__)
settings = get_project_settings()


class OlxPipeline:

    def __init__(self):
        self.host = settings.get('HOST')
        self.port = settings.get('PORT')
        self.user = settings.get('USERNAME')
        self.password = settings.get('PASSW')
        self.db = settings.get('DATABASE')
        self.table = settings.get('TABLES')
        self.client = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.client = InfluxDBClient(host=self.host,
                                port=self.port,
                                username=self.user,
                                password=self.password
                                )
        if self.client:
            logger.info('InfluxDB connect is open')
        pass

    def spider_closed(self, spider):
        self.client.close()
        if not self.client:
            logger.info('InfluxDB connect is close.')
        pass

    def process_item(self, item, spider):
        line ="""{tab},name={n} title={t},id={i},views={ad_v},price={p}""".format(
            tab = self.table,
            n = (f'"{item["name"]}"'),
            t = (f'"{item["title"]}"'),
            i = item['id_art'],
            ad_v = item['advert_views'],
            p = item['price'],
            )
        try:
            self.client.write([line], {'db': self.db}, 204, 'line')
        except Exception as err:
            logger.debug(f"Error to insert DB {err} \n data:{item}")
        return item

