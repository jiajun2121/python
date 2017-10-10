#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/8/29

import urllib.request
import chardet
import re
import time


def geturl(pageurl):
    try:
        req = urllib.request.Request(pageurl)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')

        response = urllib.request.urlopen(req)


        return response.read()
    except:
        return 'error'


def htmldecode(html):
    if html != 'error':
        try:
            return html.decode('utf8')
        except:
            html_encoding = chardet.detect(html)['encoding']
            if html_encoding == 'GB2312':
                html_encoding = 'GBK'
            return html.decode(html_encoding)
    else:
        print('error')
        return 'error'


def getpagelist(url, reg):
    page = htmldecode(geturl(url))

    reg = re.compile(reg)

    linkslist = reg.findall(page, re.S | re.M)

    return linkslist


# ############### #
#    运行部分      #
if __name__ == '__main__':
    host = r'http://www.ximalaya.com/'
    '''
    addr = r'43396178/album/4310827?page=6'     # 短篇
    filename = '2019短篇'
    '''
    addr = r'43396178/album/3866096?page=6'     # 长篇
    filename = '2049长篇'

    reg = r'track_id="(.*?)" track_title="(.*?)" track_intro=""></a>\s{0,}<span>(.*?)</span>'  # 正则表达式


    url = host + addr

    items = []
    for page_idx in range(1, 10):
        url = url[0:-1] + str(page_idx)
        item = getpagelist(url, reg)
        if len(item):
            items += item
        else:
            break

    print('已获取')


    # for index in range(len(items)):

    items.sort(key=lambda x: x[2].split('-'), reverse=True)


    with open(filename + '.txt', 'w+', encoding='utf8') as f:
        for each in items:
            print(each[0] + each[2] + each[1])
            f.write(each[0] + '\t' + each[2] + '\t' + each[1] + '\n')
