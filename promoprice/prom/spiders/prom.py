#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "odlsandrey"
__email__ = "odlsandrey@gmail.com"
""" V 2.0 """

import csv
import time
from time import sleep

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.http import JsonRequest

from prom.items import PromItem
from prom.settings import BASE_DATA_XLSX, BASE_DATA_CSV, ERROR_CSV_TMP

from prom.moduls.magent import UserAgent
from prom.moduls.price import PromPrice
from prom.moduls.constant import Selector
from prom.moduls.validator import ValidString as Vs
from prom.moduls.validator import ValidTextString as Vts

import pyexcel
import configparser

config = configparser.ConfigParser()
config.read("usersettings.ini")
logfile = 'data/readerror.txt'

def exl2csv() -> bool:
    start_time = time.time()
    pyexcel.save_as(file_name=BASE_DATA_XLSX, dest_file_name=BASE_DATA_CSV)
    print(f"INFO : time converter file {time.time() - start_time} seconds")
    return True


class ManedgerProm(scrapy.Spider):

    name = 'promoprice'
    if exl2csv():
        print("INFO : CSV File is create!")
    sleep(0.5)

    def __init__(self):
        # Settings
        self.pricelist = config.get("engine", "pricelist")
        self.stattovar = config.get("engine", "stattovar")
        self.tmp_error = ERROR_CSV_TMP
        self.datacsv = BASE_DATA_CSV
        # May Class
        self.sel = Selector()
        self.pp = PromPrice()
        self.ua = UserAgent()
        # local
        self.err = False
        self.creat_err_file = False

    custom_settings = {
        'CONCURRENT_REQUESTS' : 4,
        'DOWNLOAD_DELAY' : 17,
        'DOWNLOAD_TIMEOUT' : 30
        }
    apf = "'"

    def start_requests(self):
        search = 'https://prom.ua/search?search_term={get}'
        with open(self.datacsv, newline='') as csvfile:
            i = 0
            reader = csv.reader(csvfile, delimiter=',')
            for dstr in reader:
                if i > 0:
                    vts = Vts(dstr[0], dstr[1])
                    if not vts.valid:
                        art, desc = vts.articul_get()
                        # error logfile
                        if not Vs(art, desc).valid:
                            if not self.creat_err_file:
                                self.write_head()
                                self.creat_err_file = True
                                self.write_row(dstr[0], dstr[1], '',
                                                'validator')

                        item = PromItem()
                        item['articul'] = self.pp.clear_text(art)
                        item['posicion'] = self.pp.clear_text(desc)

                    elif vts.valid:
                        item = PromItem()
                        item['articul'] = self.pp.clear_text(dstr[0])
                        item['posicion'] = self.pp.clear_text(dstr[1])

                    if self.pricelist == "True":
                        item['price_base'] = self.pp.clear_text(dstr[8])
                    elif self.pricelist == "False":
                        item['price_base'] = self.pp.clear_text(dstr[2])

                    query = ('%s %s' % (item['posicion'], item['articul']))

                    if self.ua.swith(query):
                        yield Request(url=search.format(get=query),
                              headers=self.ua.myheaders(),
                              meta = {"item" : item},
                              callback=self.zerolevel)

                    if not self.ua.swith(query):
                        yield JsonRequest(url=self.ua.jurl(),
                              method='POST',
                              headers=self.ua.sup_head(query),
                              body=self.ua.body(query),
                              meta = {"item" : item,},
                              callback=self.toplevel)
                else: i += 1

    def zerolevel(self, response):
        item = response.meta['item']
        sleep(3)
        nalichie, opisanie, price = self.export_val(response)
        dataset = list(zip(nalichie, opisanie,
                           self.pp.format_price_string(price)))

        dataset_statusbar = self.pp.statusbar(dataset, self.stattovar)
        clear_head = self.pp.valid_head(dataset_statusbar, item['articul'])
        a, b, c, d, e, g = self.pp.getprice(clear_head, item['price_base'])

        if (a and b and c) != "Not Found":
            item['price_min'] = ('%s%s' % (self.apf, a))
            item['price_max'] = ('%s%s' % (self.apf, b))
            item['price_midl'] = ('%s%s' % (self.apf, c))
            item['price_base'] = d
            item['deviation'] = e
            item['percent'] = g
            yield item
        else:
            if not self.creat_err_file:
                self.write_head()
                self.creat_err_file = True
                write_list = (item['articul'] , item['posicion'],
                              (('%s%s' %(self.apf, item['price_base']))),
                              response.request.method)
                self.write_row(write_list)

    def toplevel(self, response):
        item = response.meta['item']
        sleep(6)
        telo = self.ua.topbody(response.body)
        clear_h = self.pp.valid_head(telo, item['articul'])
        a, b, c, d, e, g = self.pp.getprice(clear_h, item['price_base'])

        if (a and b and c) != "Not Found":
            item['price_min'] = ('%s%s' % (self.apf, a))
            item['price_max'] = ('%s%s' % (self.apf, b))
            item['price_midl'] = ('%s%s' % (self.apf, c))
            item['price_base'] = d
            item['deviation'] = e
            item['percent'] = g
            yield item
        else:
            if not self.creat_err_file:
                self.write_head()
                self.creat_err_file = True
            write_list = (item['articul'] , item['posicion'],
                          (('%s%s' %(self.apf, item['price_base']))),
                          response.request.method)
            self.write_row(write_list)

    def export_val(self, response) -> list:
        """ Export values list """
        price_s, nal_s, head_s = [], [], []
        for n in range(1, 21):
            try:
                data_price = response.xpath(
                    self.sel.price_res.format(n)
                                            ).getall()
                if len(data_price) == 0:
                    try:
                        data_price = response.xpath(
                            self.sel.price_res1.format(n)
                                                    ).getall()
                    except Exception:
                        pass
                if len(data_price) == 0:
                    try:
                        data_price = response.xpath(
                            self.sel.price_res3.format(n)
                                                    ).getall()
                    except Exception:
                        pass
                if len(data_price) == 0:
                    try:
                        data_price = response.xpath(
                            self.sel.price_res4.format(n)
                                                    ).getall()
                    except Exception:
                        pass

                if len(data_price) == 0:
                    try:
                        data_price = response.xpath(
                            self.sel.price_res5.format(n)
                                                    ).getall()
                    except Exception:
                        pass

                if len(data_price) == 0:
                    try:
                        data_price = response.xpath(
                            self.sel.price_res2.format(n+1)
                                                    ).getall()
                    except Exception:
                        pass

                if len(data_price) == 0:
                    try:
                        data_price = response.xpath(
                            self.sel.price_res6.format(n)
                                                    ).getall()
                    except Exception:
                        pass
                price_s.append(data_price)

                data_nal = response.xpath(self.sel.nal_res.format(n)).get()
                if data_nal is None:
                    data_nal = response.xpath(
                        self.sel.nal_res2.format(n)
                                              ).get()

                if data_nal is None:
                    data_nal = response.xpath(
                        self.sel.nal_res1.format(n+1)
                                              ).get()
                if data_nal is None:
                    data_nal = response.xpath(
                        self.sel.nal_res3.format(n)
                                              ).get()
                if data_nal is None:
                    data_nal = response.xpath(
                        self.sel.nal_res4.format(n)
                                              ).get()
                nal_s.append(data_nal)

                data_head = response.xpath(
                    self.sel.head_res.format(n)
                                          ).get()
                if data_head is None:
                    data_head = response.xpath(
                        self.sel.head_res3.format(n)
                                              ).get()
                if data_head is None:
                    data_head = response.xpath(
                        self.sel.head_res2.format(n)
                                              ).get()
                if data_head is None:
                    data_head = response.xpath(
                        self.sel.head_res1.format(n)
                        ).get()
                if data_head is None:
                    data_head = response.xpath(
                        self.sel.head_res4.format(n)
                        ).get()
                if data_head is None:
                    data_head = response.xpath(
                        self.sel.head_res2.format(n+1)
                                              ).get()
                if data_head is None:
                    data_head = response.xpath(
                        self.sel.head_res5.format(n)
                                              ).get()
                head_s.append(data_head)
            except IndexError:
                pass
        return nal_s, head_s, price_s

    def write_head(self) -> None:
        head = ['Articul', 'Descriptions', 'price', 'Title']
        with open(self.tmp_error, 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile, dialect = 'excel',
                                delimiter=',')
            writer.writerow(head)

    def write_row(self, array):
         with open(self.tmp_error, 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile, dialect = 'excel',
                                delimiter=',')
            writer.writerow(array)


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(ManedgerProm)
    process.start()
