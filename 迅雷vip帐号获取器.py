#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-28 19:16:55
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests as rq
import re


def get1():
    source = 'http://yunbo.xinjipin.com/articlelist/?33.html'
    web = rq.get(source).text
    url = re.findall('<li><p><a href=\"(.*?)\" title=', web)[0]
    web = rq.get('http://yunbo.xinjipin.com%s' % url)
    web.encoding = 'gb2312'
    web = web.text
    return re.findall(u'迅雷.*?([a-zA-z0-9\:]+?)[密码]+?([a-zA-z0-9]+?)</div>', web)


def get2():
    source = 'http://www.fenxs.com'
    web = rq.get(source).text
    url = re.findall(
        u'<h2><a href=\"(.*?)\" title=.*?迅雷会员账号分享.*?</a></h2>', web)[0]
    web = rq.get(url).text
    return re.findall(u'迅雷.*?([a-zA-z0-9\:]+?)[密码]+?([a-zA-z0-9]+?)<br />', web)


def get3():
    source = 'http://xlfans.com'
    web = rq.get(source).text
    url = re.findall(
        u'<h2><a href=\"(.*?)\" title=.*?迅雷会员账号分享.*?</a></h2>', web)[0]
    web = rq.get(url).text
    return re.findall(u'迅雷.*?([a-zA-z0-9\:]+?)[密码]+?([a-zA-z0-9]+?)<br />', web)


if __name__ == '__main__':
    import pandas as pd  # 方便输出显示
    import sys  # 判断系统版本

    print(u'\n============简单的迅雷账号获取器============\n           By http://kexue.fm\n')
    while True:
        if sys.version_info[0] < 3:
            s = raw_input(u'请选择数据源(输入s1或s2或s3，输入其他则退出): ')
        else:
            s = input(u'请选择数据源(输入s1或s2或s3，输入其他则退出): ')
        if s == 's1':
            print(pd.DataFrame(get1(), columns=[u'账号', u'密码']))
        elif s == 's2':
            print(pd.DataFrame(get2(), columns=[u'账号', u'密码']))
        elif s == 's3':
            print(pd.DataFrame(get3(), columns=[u'账号', u'密码']))
        else:
            break
