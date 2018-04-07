#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time:2017/9/7

from wxpy import *
import json


# 扫码登陆
bot = Bot(cache_path=True)

# 初始化图灵机器人 (API key 申请: http://tuling123.com)
# tuling = Tuling(api_key='75137612d89c42f0b9d7a3f5133ec656')

# 自动回复所有文字消息
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    print(
        '''
        发送者 -> {0}
        消息内容 -> {1}

        '''.format(msg.sender, msg.text ))
    print(msg)
    with open('record.txt','utf-8', 'w+') as f:
        f.write(json.dumps(msg))
        print('save')

    with open('yellow.list','utf8', 'r+') as f:
        yellow = json.loads(f.read())

    flag='avavav'
    if ( msg.member is not None ) and ( msg.sender in yellow ) :
        if flag in msg.text[:len(flag)]:
            content = r'嘿，想啥呢，年轻人好好学习去！'
            msg.sender.send(content)
















    #tuling.do_reply(msg)


# 开始运行
bot.join()

'''
import wxpy.api.chats.chat as cchat
c = cchar.Chat()
c.send_msg()
c.send()


'''
