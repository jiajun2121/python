#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/12/28



fin = open('fanhao.txt', mode='w+', encoding='utf-8')
fh = []

for e in open('麻生希.csv'):
    vedioinfo = e.split(',')
    title, _, company, fanhao, other_actress, timelong = vedioinfo
    a = dict(zip(['title', 'date', 'company', 'fanhao', 'other_actress', 'timelong'], vedioinfo))
    
    fin.writelines(a['title'] + '\r')
fin.close()
print('over')
