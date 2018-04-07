#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/11/5
import json
import requests
import re



text = '   avavav: ase 5186   👎   麻生希'.upper()
flags = ['AVAVAV', 'AV女优']


def getmagenturl(keyword=None):
    url = 'http://www.btava.cc/s/{0}.html'.format(keyword)
    text = requests.get(url).text
    print(text)
    # get link
    reg = re.compile(r'href="http://www.btava.cc/torrent/(.*?)).html')
    magent = reg.findall(text)[:3]
    magent = ''.join([lambda x:'\n\nmagnet:?xt=urn:btih:' + x for x in magent])
    
    return magent

def guolv(text, flag):

    if flag[0] in text:
        keyword = ''.join([i for i in text.replace(flag[0],'') if ord(i) < 128 and i.isalnum()]).replace(' ','')
        return keyword
    
    elif flag[1] in text:
        keyword = ''.join([i for i in text.replace(flag[1],'') if ord(i) > 128 and i.isalnum()]).replace(' ','')
        return keyword
    else:
        return None


keyword = guolv(text, flags)

magent = getmagenturl(keyword)
content = '以下为\n\n\n' + magent
print(content)
