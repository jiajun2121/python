#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-02 14:06:08
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import itertools as its
words = "1234568790@.qwertyuiopasdfghjklzxcvbnm"
r =its.product(words,repeat=8)
dic = open("pass.txt","a")


for i in r:
	print(i)
'''
    dic.write("".join(i))
    dic.write("".join("\n"))
'''
dic.close()
