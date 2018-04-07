#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2018/1/20

import requests
from  bs4 import BeautifulSoup


def get_movie(soup):
    title = soup.find_all('h1', class_='font14w')[0].text,
    temp = soup.find_all('span',class_='font_888')
    info = soup.find_all('div', 'info')[0]
    pass









url = r'http://www.80s.tw/dm/22138'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__jsluid=427a28742a1c64cdf9d55556d495e11b; Hm_lvt_652f84236c4c73e10377e2dd54891ff3=1516455214,1516458495; pc_fan=1; Hm_lpvt_652f84236c4c73e10377e2dd54891ff3=1516460329',
    'DNT': '1',
    'Host': 'www.80s.tw',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
req = requests.get(url=url, headers=header, verify=False)
sou = BeautifulSoup(req.content, 'lxml')
sou.find_all('div', 'info')

ls = get_movie(sou)
