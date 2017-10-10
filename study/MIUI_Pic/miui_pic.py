#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/9/7

import urllib.request
import os
import time
import json
import threading

# 接口： r'http://zhuti.xiaomi.com/wallpaper?page=1&sort=New&ajax=1&count=30&act=list&keywords='
# keyword = '风景'
# url = url + up.quote(keyword)


def geturl(pageurl):
    req = urllib.request.Request(pageurl)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')
    try:
        page = urllib.request.urlopen(req).read()
    except:
        print('http ERROR')
        page = None
    finally:
        return page


def SavePicture(pth, file_name, img):
    with open(pth + "\\" + file_name + ".jpg", 'wb+') as f:
        print('Picture: ' + file_name)
        f.write(img)

if __name__ == "__main__":

    imgsrc = r'http://file.market.xiaomi.com/thumbnail/jpeg/w965/'

    url = r'http://zhuti.xiaomi.com/wallpaper?ajax=1&act=list&count=50&page=1'

    pth = os.getcwd()
    if not os.path.exists('Picture'):
        os.mkdir('Picture')
    os.chdir(os.getcwd() + r'\Picture')

    for i in range(50, 100):
        print('one more page',end='\r')
        url = url[:-1] + str(i)
        json_str = geturl(url).decode('utf8')


        json_list = json.loads(json_str)

        tasks = []
        for each in json_list:
            if not os.path.exists(each['name'] + r'.jpg'):
                link = imgsrc + each['frontCover']
                img = geturl(link)
                t = threading.Thread(target=SavePicture, args=(pth + r'\Picture', each['name'], img))
                tasks.append(t)

        for task_idx in range(len(tasks)):
            tasks[task_idx].setDaemon(True)
            tasks[task_idx].start()

        for task in tasks:
            task.join()
        time.sleep(1.5)


