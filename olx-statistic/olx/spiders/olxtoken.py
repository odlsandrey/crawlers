#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "odlsandrey"
__email__ = "odlsandrey@gmail.com"

import logging

import scrapy
from scrapy.spiders import CrawlSpider
from olx.spiders.moduls.payload import CretePayload

logger = logging.getLogger(__name__)
cp = CretePayload()

class OlxToken(CrawlSpider):

    def __init__(self):
        self.jurl =  'https://www.olx.ua/api/open/oauth/token'


    name = 'token'
    custom_settings = {
        'REFERER_ENABLED': False,
        'CONCURRENT_REQUESTS' : 1,
        'DOWNLOAD_DELAY' : 17,
        'COOKIES_ENABLED': True,
        'DOWNLOAD_TIMEOUT': 30,
        'LOG_ENABLED': True,
        # 'LOG_FILE ': 'data/spider.log',
        'LOG_DATEFORMAT': '[%Y-%m-%d %H:%M:%S]'
        }

    def start_requests(self):
        """проверочный запрос"""
        # print(cp.start_form)
        yield scrapy.FormRequest(url=self.jurl, method='POST',
                            formdata=cp.start_form(),                            
                            callback=self.token_check
                            )

    def token_check(self, response):
        """проверка данных жизни токена"""
        if response.status == 403:
            logger.info('Сервер понял запрос, но отказывается его выполнить')
        if response.status == 200:
            # обработать ответа
            if cp.check_access_token(response.body):
                # если токену ост. жить < 30 мин. обновить
                yield scrapy.FormRequest(url=self.jurl, method='POST',
                                    formdata=cp.update_form(),
                                    callback=self.update_token)
        else:
            # записать в лог + тело ответа в файл
            logger.warning('Ошибка чтения жизни токена')
            cp.write_error_body(response.request.body, response.body)

    def update_token(self, response):
        if response.status == 200:
            if cp.check_refresh_token(response.body):
                logger.info('Refresh Token Update')
                print('odls', response.body)
        else:
            logger.warning('Ошибка обновления refresh token')
            cp.write_error_body(response.request.body, response.body)
        return None

