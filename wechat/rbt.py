#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time:2017/9/7

from wxpy import *

# 扫码登陆
bot = Bot()

# 初始化图灵机器人 (API key 申请: http://tuling123.com)
tuling = Tuling(api_key='75137612d89c42f0b9d7a3f5133ec656')


# 自动回复所有文字消息
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)


# 开始运行
bot.join()
