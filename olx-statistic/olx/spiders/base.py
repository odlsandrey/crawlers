#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Паук для основного обхода обьявлений автора
"""

__author__ = "odlsandrey"
__email__ = "odlsandrey@gmail.com"

import logging
from time import sleep

import scrapy
from pydispatch import dispatcher
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from olx.spiders.moduls.selector import Selectors
from olx.items import BaseOlxItem

logger = logging.getLogger(__name__)
settings = get_project_settings()
sel = Selectors().sel

class OlxBase(scrapy.Spider):

    def __init__(self):
        self.path_driver = settings.get('DRIVER')
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_experimental_option( "prefs", {'profile.default_content_settings.images': 2})
        options.add_argument("--headless")
        options.add_argument('--window-size=1200,960')
        self.browser = webdriver.Chrome(chrome_options = options,
                           executable_path = self.path_driver)
        super(OlxBase, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    name = 'base'
    # Insert start page
    start_urls = ['https://www.olx.ua/.......',]

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS' : {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'
            },
        'DOWNLOADER_MIDDLEWARES' : {
            'olx.middlewares.OlxDownloaderMiddleware': 543,
            },
        'ITEM_PIPELINES' : {'olx.pipelines.OlxPipeline': 300,},
        'CONCURRENT_REQUESTS' : 1,
        'DOWNLOAD_TIMEOUT': 18,
        'DOWNLOAD_DELAY' : 17,
        'LOG_ENABLED': True,
        'LOG_DATEFORMAT' : '[%Y-%m-%d %H:%M:%S]',
        # 'LOG_FILE' : 'base_spider.log',
        'COOKIES_ENABLED': True,
        }

    def spider_closed(self):
        self.browser.close()
        self.browser.quit()

    def parse(self, response):
        sleep(16)
        for l in response.css(sel['alllinks']).getall():
            yield response.follow (url=l, callback=self.read_body)
            sleep(6)

    def read_body(self, response):
        sleep(20)
        # print(response.request.headers)
        item = BaseOlxItem()
        item['name'] = response.css(sel['name']).get().rstrip()
        item['title'] = response.css(sel['title']).get().rstrip()
        id_art = response.css(sel['id_art']).getall()
        try:
            item['id_art'] = self.clean(id_art[0].rstrip())
        except IndexError as err:
            logger.debug("Index error", err)
        advert_views = response.css(sel['advert_views']).get()
        if advert_views is not None:
            item['advert_views'] = self.clean(advert_views)
        else:
            logger.debug("Error advert_views is empty")
        price = response.css(sel['price']).get().rstrip()
        item['price'] = self.clean(price)
        item['link'] = response.url
        yield item
        sleep(2.5)

    def clean(self, text):
        digits = [symbol for symbol in text if symbol.isdigit()]
        cleaned_text = ''.join(digits)
        if not cleaned_text:
            return None
        return int(cleaned_text)


