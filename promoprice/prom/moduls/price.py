#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "odlsandrey"
__email__ = "odlsandrey@gmail.com"

from datetime import datetime

class PromPrice:

    def __init__(self):
        self.apf = "'"

    def format_price_string(self, parray) -> list:
        result = []
        for arrlist in parray:
            if len(arrlist) > 1:
                dolar = arrlist[0]
                try:
                    cent = arrlist[1].replace(',', '.')
                    summ = ('%s%s' % (dolar, cent))
                    summa = summ.replace(' ', '')
                    result.append(float(summa))
                except IndexError:
                    pass
            else:
                try:
                    dolar_f = arrlist[0].replace(' ', '')
                    result.append(float(dolar_f))
                except IndexError:
                    pass
        return result

    def statusbar(self, dataset, stattovar):
        if stattovar == "True":
            opis_price = self.tovar_isover(dataset)
        else:
            opis_price = self.tovar_true(dataset)
        clear_opis = self.clear_opis_price(opis_price)
        return clear_opis

    def tovar_isover(self, vara) -> list:
        dataset_isover = []
        for row in vara:
            if ("В наличии" in row[0]) or (row[0] == "Заканчивается"):
                dataset_isover.append(row)
        return dataset_isover

    def tovar_true(self, varb):
        dataset_true = []
        for row in varb:
            try:
                if ("В наличии" in row[0]):
                    dataset_true.append(row)
            except Exception:
                pass
        return dataset_true

    def clear_opis_price(self, opis_p) -> list:
        opis, price = [], []
        for n in range(0, len(opis_p)):
            opis.append(opis_p[n][1])
            price.append(opis_p[n][2])
        res = list(zip(opis, price))
        return res

    def valid_head(self, data_statusbar, articul) -> list:
        price = []
        for n in range(0, len(data_statusbar)):
            opis = data_statusbar[n][0].replace(',', '')
            try:
                opis_arr = opis.split(" ")
            except UnboundLocalError as error:
                print("Error valid_head", error)

            try:
                for artic in opis_arr:
                    artic = artic.replace(',', '')
                    if artic == articul:
                        price.append(data_statusbar[n][1])
                        break
            except UnboundLocalError as error:
                print("Error valid_head", error)
        return price

    def getprice(self, pricelist, price_str):
        er_price = "Not Found"
        new_arr = []
        price = self.str2float(price_str)

        for r in pricelist:
            r = float(r)
            if (r / price) < 3 and (price / r) < 3:
                new_arr.append(r)

        if new_arr:
            try:
                price_min = min(new_arr)
                price_max = max(new_arr)
                _price_midl = price_min + ((price_max - price_min) / 2)
                price_midl = (int(_price_midl * 100) / 100)
                if price_midl:
                    deviation = self.calc_deviation(price, price_midl)
                percent = self.percent(price, price_midl)
            except Exception as error:
                print("Error getprice :", error)

            return price_min, price_max, price_midl, price, deviation, percent
        else:
            return er_price, er_price, er_price, price, er_price, er_price

    def percent(self, base, midll) -> str:
        proc = 100 - ((midll * 100) / base)
        if midll > base:
            proc = proc
            return ("'% {0}".format(round(proc, 2)))
        return ("'% {0}".format(round(proc, 2)))

    def calc_deviation(self, price, price_midl):
        deviation = ('%s%s' % (self.apf,
                               (int((price - price_midl) * 100) / 100))                                     )
        return deviation

    def str2float(self, string):
        price = string.replace("'",'').replace(",",".")
        return (float(price))

    def check_dataset(self, dataset):
        for x in range(0, len(dataset)):
            if (dataset[x][0] == None) or\
                (dataset[x][1] == None) or\
                    (dataset[x][2] == None):
                return True
                break
        if len(dataset) == 0:
            return True
        return False

    def sevelog(self, fn, response, r_data):
        zagolovok = ["\n******* BODY ERROR *******************"]
        link = [[datetime.now().strftime("%Y-%m-%d")],
                [' - - %s' % (response)]]
        with open(fn, "a+") as file:
            print(*zagolovok, file=file, sep="\n")
            print(*link, file=file, sep="\n")
            print(*r_data, file=file, sep="\n")
        return None

    def savelogarticle(self, fn, response, r_data):
        zagolovok = ["\n******* ARTICLE ERROR **************"]
        link = [[datetime.now().strftime("%Y-%m-%d")],
                [' - - %s' % (response)]]
        with open(fn, "a+") as file:
            print(*zagolovok, file=file, sep="\n")
            print(*link, file=file, sep="\n")
            print(*r_data, file=file, sep="\n")
        return None

    def clear_text(self, text) -> str:
        sep = ["'", '(', ')']
        for row in sep: text = text.replace(row, '')
        return text

    pass
