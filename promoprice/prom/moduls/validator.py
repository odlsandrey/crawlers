#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" V 0.2 """

__author__ = "odlsandrey"
__email__ = "odlsandrey@gmail.com"

import string as String
from datetime import datetime


class ValidString:

    def __init__(self, art, description):
        super().__init__()
        self.__art = art
        self.__desc = description
        self.__valid = None
        self.__massiv = None

    @property
    def massiv(self):
        if self.__massiv is None:
            self.__massiv = self.__desc.split(' ')
        return self.__massiv

    @property
    def art(self):
        return self.__art

    @art.setter
    def art(self, art):
        self.__art = art.strip()
        self.__valid = None
        self.__massiv = None

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, description):
        self.__desc = description.strip()
        self.__valid = None
        self.__massiv = None

    @property
    def valid(self):
        """ property validator value articul and string """
        if self.__valid is None:
            self.__valid = self.check_massiv_descript(self.art, self.massiv)
        return self.__valid

    def check_massiv_descript(self, articul, massiv) -> bool:
        """ compare articul vs description """
        for st in massiv:
            if st == articul:
                valid_art = True
                break
            else: valid_art = False
        return valid_art

class ValidText:

    def __init__(self, **kwargs):
        self.__number = None
        self.defis = '-'
        self.__literaru = None
        self.__literaen = None
        super().__init__(**kwargs)

    @property
    def literaru(self):
        if self.__literaru is None:
            self.__literaru = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З',\
                   'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',\
                       'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я', \
                           'Ь', 'Ъ', 'Ё', 'Ы']
        return self.__literaru

    @property
    def literaen(self):
        if self.__literaen is None:
            self.__literaen = list([l for l in String.ascii_uppercase])
        return self.__literaen

    @property
    def number(self):
        if self.__number is None:
            n = list([n for n in String.digits])
            # n.append('-')
            self.__number = n
        return self.__number


class ValidTextString(ValidString, ValidText):

    def __init__(self, *args):
        super().__init__(*args)
        self.validator_error = False
        self.__isup =None
        self.badstring = 'data/badstring.txt'

    def articul_get(self, art=None, desc=None):
        """Return Valid Articul and String"""
        if art is None:
            art = self.art
        if desc is None:
            desc = self.desc

        all_dict = self.articul_geter()
        max_val = self.max_val_dict(all_dict)
        valid_articul = self.get_first_val_dict(max_val)
        return valid_articul, desc

    def articul_geter(self) -> dict:
        # parazit`s
        badlist = self.read_list(self.badstring)
        cri = self.clear_res_isup(badlist, self.isup)
        mdicts = self._create_dict(cri)
        clas = self.classifier(mdicts)
        return clas

    def read_list(self, fn) -> list:
        """ Read parazit list """
        arr = []
        with open(fn, 'r') as file:
            [arr.append(string.rstrip()) for string in file]
        return arr

    def clear_res_isup(self, badlist: list, isup: list) -> list:
        for r in badlist:
            try:
                isup.remove(r)
            except Exception:
                pass
        return self._del_double(isup)

    def _del_double(self, lists):
        lists = list(set(lists))
        return lists

    def _create_dict(self, arr: list) -> dict:
        mdict = {}
        for d in arr:
            mdict[d] = 0
        return mdict

    def classifier(self, mdict) -> dict:
        """ RU = 0.7 EN = 0.6 number = 0.1 defis = 0.1 """
        for key in mdict:
            if self.search_ru(key):
                mdict[key] += 0.7
            if self.search_en(key):
                mdict[key] += 0.7
            if self.search_number(key):
                mdict[key] += 0.1
            if self.search_defis(key):
                mdict[key] += 0.1
        return mdict

    def search_en(self, isupper) -> list:
        """ Search EN literal`s """
        result = []
        for string in isupper:
            label = True
            for litera in string:
                if litera in self.literaru:
                   label = False
                   break
            if label:
                result.append(string)
                label = False
        return result

    def search_ru(self, isupper) -> list:
        """Search RU literal`s"""
        result = []
        for string in isupper:
            label = True
            for litera in string:
                if litera in self.literaen:
                    label = False
                    break
            if label:
                result.append(string)
                label = False
        return result

    def search_number(self, result: list):
        articul = []
        for string in result:
            label = False
            for litera in string:
                if litera in self.number:
                    label = True
                    break
            if label:
                articul.append(string)
                label = False
        return articul

    def search_defis(self, res):
        art = []
        for string in res:
            label = False
            for litera in string:
                if litera in self.defis:
                    label = True
                    break
            if label:
                art.append(string)
                label = False
        return art

    def max_val_dict(self, mdict):
        di = {
            x: y for x, y in filter(
            lambda x: mdict[x[0]] == max(mdict.values()),
            mdict.items())
            }
        return di

    def get_first_val_dict(self, mdict):
        if len(mdict) > 0:
            for d in mdict:
                articul = d
                break
        elif len(mdict) == 0:
            articul = 0
        return articul

    @property
    def isup(self):
        """ Search upper string """
        if self.__isup is None:
            sp = []
            for a in self.massiv:
                if a.isupper() and len(a) > 3:
                    sp.append(a)
            self.__isup = sp
        return self.__isup

    pass






















