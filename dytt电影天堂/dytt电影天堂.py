#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03 21:10:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.request
import os
import re
import string

# 电影URL集合
movieUrls = []


# 获取电影列表
def queryMovieList():
    url = 'http://www.dytt8.net/html/gndy/dyzz/index.html'
    conent = urllib.request.urlopen(url)
    conent = conent.read()
    conent = conent.decode('gb2312', 'ignore')  # .encode('utf-8','ignore')
    pattern = re.compile('<div class="title_all"><h1><font color=#008800>.*?</a>></font></h1></div>' +
                         '(.*?)<td height="25" align="center" bgcolor="#F4FAE2"> ', re.S)
    items = re.findall(pattern, conent)
    
    str = ''.join(items)
    pattern = re.compile('<a href="(.*?)" class="ulink">(.*?)</a>.*?<td colspan.*?>(.*?)</td>', re.S)
    news = re.findall(pattern, str)
    
    for j in news:
        movieUrls.append('http://www.dytt8.net' + j[0])


def queryMovieInfo(movieUrls, item=None):
    for index, item in enumerate(movieUrls):
        movie_item_info = {}
        movie_item_info['url'] = item
        
        conent = urllib.request.urlopen(item)
        conent = conent.read()
        conent = conent.decode('gb2312', 'ignore')  # .encode('utf-8','ignore')
        
        movieName = re.findall(r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>', conent, re.S)
        if (len(movieName) > 0):
            movieName = movieName[0] + ""
            # 截取名称
            movieName = movieName[movieName.find("《") + 3:movieName.find("》")]
        else:
            movieName = ""
        
        movie_item_info['title'] = movieName.strip()
        
        movieContent = re.findall(r'<div class="co_content8">(.*?)</tbody>', conent, re.S)
        
        pattern = re.compile('<ul>(.*?)<tr>', re.S)
        movieDate = re.findall(pattern, movieContent[0])
        
        if (len(movieDate) > 0):
            movieDate = movieDate[0].strip() + ''
        else:
            movieDate = ""
        
        movie_item_info['date'] = movieDate[-10:]
        
        pattern = re.compile('<br /><br />(.*?)<br /><br /><img')
        movieInfo = re.findall(pattern, movieContent[0])
        
        if (len(movieInfo) > 0):
            movieInfo = movieInfo[0] + ''
            
            # 删除<br />标签
            movieInfo = movieInfo.replace("<br />", "").replace('\u3000' * 2, '').replace('&middot;', '*').replace(
                '\u3000', '\t').replace(' ','\t')
            
            # 根据 ◎ 符号拆分
            
            movieInfo = movieInfo.split('◎')
        
        else:
            movieInfo = ""
        
        m_info_dict = {}
        for item in movieInfo[1:]:
            d = dict([item.split(':')][0:2])
            m_info_dict.update(d)
        movie_item_info['base_info'] = movieInfo
        
        for item in movieInfo:
            print(item)
        
        # 电影海报
        pattern = re.compile('<img.*? src="(.*?)".*? />', re.S)
        movieImg = re.findall(pattern, movieContent[0])
        
        if (len(movieImg) > 0):
            movieImg = movieImg[0]
        else:
            movieImg = ""
        
        movie_item_info["poster"] = movieImg
        
        pattern = re.compile('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">.*?</a></td>', re.S)
        movieDownUrl = re.findall(pattern, movieContent[0])
        
        if (len(movieDownUrl) > 0):
            movieDownUrl = movieDownUrl[0]
        else:
            movieDownUrl = ""
        
        movie_item_info["download_url"] = movieDownUrl
        print(movie_item_info)
        print("------------------------------------------------\n\n\n")


if __name__ == '__main__':
    print("开始抓取电影数据")
    
    queryMovieList()
    
    print(len(movieUrls))
    
    queryMovieInfo(movieUrls)
    
    print("结束抓取电影数据")
