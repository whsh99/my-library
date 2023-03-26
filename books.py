# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:28:19 2022

@author: 陳永興
"""

class Book(object):
    def __init__(self, bn, tl, typ, lang, stat, b_date, r_date):  # 初始化書籍
        self.bn = bn  # bn: 書號
        self.tl = tl  # tl: 書名
        self.typ = typ  # typ: 書類型
        self.lang = lang  # lang: 書語言
        self.stat = stat  # stat: 書狀態
        self.b_date = b_date  # b_date: 借書日期
        self.r_date = r_date  # r_date: 還書日期