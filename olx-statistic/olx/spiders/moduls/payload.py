#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "odlsandrey"
__email__ = "odlsandrey@gmail.com"

import json
import logging

from datetime import datetime
from scrapy.utils.project import get_project_settings

logger = logging.getLogger(__name__)
settings = get_project_settings()

class CretePayload:
    """формирует словарь для передачи в теле запроса
    обрабатывает ответы API + чтение и запись """

    def __init__(self):
        # импорт настроек API
        self.id = settings.get('CLIENT_ID')
        self.client = settings.get('CLIENT_SECRET')
        self.scope = settings.get('SCOPE')
        self.file = settings.get('ERROR_POST')
        self.file_json = settings.get('JSON_DUMP')

    def start_form(self) -> dict:
        """variables for start_requests"""
        req = {
            'grant_type': 'client_credentials',
            'scope': self.scope,
            'client_id': self.id,
            'client_secret': self.client}
        return req

    def update_form(self):
        """variables for response to update_token"""
        if self.load_old_tokens():
            refresh = self.load_old_tokens()
            req = {
                  "grant_type": "refresh_token",
                  "client_id": self.id,
                  "client_secret": self.client,
                  "refresh_token": refresh
                }
            return req
        else:
            return None

    def load_old_tokens(self) -> str:
        """загрузить json файл и взять refresh_token"""
        with open(self.file_json, 'r',  encoding='utf-8') as rfile:
            dump = json.load(rfile)
        if dump['refresh_token'] and isinstance(dump['refresh_token'], str):
            return dump['refresh_token']
        else:
            logger.debug('ERROR ошибка при чтении JSON фала!')
            return False

    def save_new_tokens(self, dump: dict) -> None:
        """обновить хранимые данные json tokens"""
        with open(self.file_json, 'w+') as wfile:
            json.dump(dump, wfile)
        return None

    def check_access_token(self, body) -> bool:
        """ проверить данные ответа """
        body = json.loads(body)
        if int(body['expires_in']) < 1800: # 30 минут
            if body['access_token']:
                return True
            else:
                logger.debug("Токен пуст")
                return False
        else:
            logger.info('Оставшееся время: %s сек.' % body['expires_in'])
            return False

    def check_refresh_token(self, body) -> bool:
        """ проверить данные ответа по обновлению """
        body = json.loads(body)
        if body['expires_in'] > 84000: # ~ 23.30 минут
            # выполним запись дампа в json файл
            logger.info('CHECK_REFRESH True %s' % body)
            try:
                dumps = {
                    "access_token": body["access_token"],
                    "refresh_token": body["refresh_token"],
                    "token_type": body["token_type"]
                    }
            except Exception as err:
                logger.warning("ERROR", err)
            if dumps:
                self.save_new_tokens(dumps)
                return True
        elif body['expires_in'] < 84000: # ~ 23.30 минут:
            logger.info('Токен жив не желает обновляться!)')
            return True

    def write_error_body(self, req, err_body) -> None:
        """записать запрос и ответ сервера"""
        lines = ('[%s] REQUEST: %s RESPONSE: %s' % (datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"), req, err_body))
        with open(self.file, 'a+') as wfile:
            wfile.write((lines) + '\n')
        logger.info('Запись данных об ошибке')
        return None


