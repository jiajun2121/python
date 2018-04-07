#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2018/1/20


class Movie(dict):
    def __init__(self, title, date, srcurl):
        self.title = title
        self.date = date
        self.srcurl = srcurl




a = Movie('','','')
print(a)



