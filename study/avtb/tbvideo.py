#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/9/5


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
    url = r'http://www.avtb002.com'
    print('来源：', url)

    filename = 'tb'

    reg = r'href="(/[0-9]{0,10}/).*?" title="(.*?)"'  # 正则表达式

    for i in range(1, 10):
        if i > 1:
            url = url + '/recent/' + str(i)

        list = getpagelist(url, reg)

        f = open('src.txt', 'a+', encoding= 'utf-8')
        for each in list:
            page = htmldecode(geturl(url + each[0]))
            src = re.findall(r'src="(http://\d.*?' + each[0][0:-1] + '.mp4.*?)"', page, re.S)[0]
            print(each[1])
            print(src)
            print('~~~~~~~')

            if each[0][1:-1] not in [f.read().split('\s')[3*x] for x in range(len(f.readlines())//2)]:
                f.write(each[0][1:-1] + '\t' + each[1] + '\n')
                f.write(src + '\n')
            f.flush()

        c.close()
