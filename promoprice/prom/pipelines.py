import os

from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.utils.project import get_project_settings

import pyexcel


class PromPipeline(CsvItemExporter):

    def __init__(self):
       self.files = {}
       self.settings = get_project_settings()
       self.datacsv_ = self.settings.get('DATA_PRICE_CSV')
       self.datacsv = self.settings.get('DATA_RESULT_CSV')
       self.outexcel = self.settings.get('SAVE_RESULT_XLSX')
       self.csv_errorfile = self.settings.get('ERROR_CSV_TMP')
       self.errorfile = self.settings.get('ERROR_XLS_RESULT')

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open(self.datacsv_, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = [
            'articul',
            'posicion',
            'price_base',
            'price_midl',
            'deviation',
            'percent',
            'price_min',
            'price_max',
            'title'
            ]
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()
        self.csv2exl(self.datacsv, self.outexcel)
        if os.path.isfile(self.csv_errorfile):
            self.csv2exl(self.csv_errorfile, self.errorfile)
        self.del_csverror(self.csv_errorfile)
        print("Spider is closed!")

    def csv2exl(self, ifn, ofn):
        pyexcel.save_as(file_name=ifn,
                    dest_sheet_name="Result price",
                    dest_file_name=ofn)
        return None

    def del_csverror(self, fn):
        if os.path.isfile(fn):[os.remove(fn)]





