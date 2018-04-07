#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2018/2/3

import requests
import re
import bs4
from bs4 import BeautifulSoup


def get_movie_info(response):
    '''
    解析页面，返回影片信息
    
    :param response:
    :return:
    '''
    print(response)
    soup = BeautifulSoup(open('moviepage.html', 'rb').read(), 'html5lib')
    movieinfo = soup.find('span', style=re.compile(r'.*?'))
    all_movie_info = movieinfo.contents[1]
    st = '\n'.join(all_movie_info.text.replace('\u3000', '\t').replace('\t\t', '').split('◎'))
    reg = re.compile(r'(.*?)\t(.*?)\n')
    temp = reg.findall(st)
    d = {}
    for i, k in temp:
        d[i] = k
    direct = d.get('导演')
    area = d.get('产地')
    doubanscore = d.get('豆瓣评分')
    # 处理数据
    
    
    
    
    temp = all_movie_info.text.replace('\u3000', '\t').split('◎')
    # 提取主演名字，组成 元组的列表
    cast = temp[-2].split('\t')
    cast = [i.strip() for i in cast if len(i) > 2]
    cast = [tuple([i[:i.find(' ')], i[i.find(' '):]]) for i in cast]
    intro = temp[-1].replace('\t', '').replace('简介', '').replace('【下载地址】', '').strip()
    
    d.update({'主演': cast, '简介': intro})
    return d


if __name__ == '__main__':
    inf = get_movie_info('')
