#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/11/5

'''
href="http://www.btava.cc/torrent/C861D8EEE58FEA0420C2E1379DE5071DB7873B47.html"


'''

from wxpy import *
import json
import requests
import re


flags = ['AVAVAV', 'AV女优']

# 扫码登陆
bot = Bot(cache_path=True)


# 初始化图灵机器人 (API key 申请: http://tuling123.com)
# tuling = Tuling(api_key='75137612d89c42f0b9d7a3f5133ec656')



# 自动回复所有文字消息
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    print(msg)
    with open(r'yellow.list', mode='r+', encoding='utf8') as f:
        yellow = json.loads(f.read())
    
    if (msg.member is not None) and (msg.sender in yellow):
        print(msg)
    
        keyword = guolv(msg.text, flags)
        magent =getmagenturl(keyword)
        content = '以下为多个链接\n\n'.format(magent)
        msg.sender.send(content)


def guolv(text, flag):
    if flag[0] in text:
        keyword = ''.join([i for i in text.replace(flag[0], '') if ord(i) < 128 and i.isalnum()]).replace(' ', '')
        return keyword
    
    elif flag[1] in text:
        keyword = ''.join([i for i in text.replace(flag[1], '') if ord(i) > 128 and i.isalnum()]).replace(' ', '')
        return keyword
    else:
        return None

def getmagenturl(keyword=None):
    url = 'http://www.btava.cc/s/{0}.html'.format(keyword)
    text = requests.get(url).text
    # get link
    reg = re.compile(r'href="http://www.btava.cc/torrent/(.*?)).html')
    magent = reg.findall(text)[:3]
    
    return magent

# 开始运行
bot.join()



'''
import wxpy.api.chats.chat as cchat
c = cchat.Chat()
c.send_msg()
c.send()


'''
