#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/9/26

import urllib.request
import threading
import time
import os
import winsound


isover = 0

hosts = ''
ThreadCopy = 4

def run(urls):
    childThread = []
    global isover
    for url in urls:
        for i in range(ThreadCopy):
            task = threading.Thread(target=gethosts, args=(' ', url))
            childThread.append(task)
    
    for task in childThread:
        task.setDaemon(True)
        task.start()
    while not isover:
        time.sleep(3)

def gethosts(_,_url):
    global isover, hosts
    try:
        hosts = _getpage(_url)
        if not isover:
            isover = True
            print('获取hosts列表完成')

    except Exception as e:
        if not isover:
            print('get hosts error',e)

def _getpage(_url):
    global isover
    try:
        request = urllib.request.Request(_url)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')
    
        page_data = urllib.request.urlopen(request).read()
        try:
            page_data = page_data.decode('utf-8')
        except:
            if not isover:
                print('ERROR')
        os.popen('cls')
    
        return page_data
    except Exception as e:
        if not isover:
            print('get page error')


if __name__ == '__main__':
    hostsurls = ['https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts',
                 'https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts-files/hosts']

    run(hostsurls)

    os.popen('title "hosts"')
    
    print('''

 √√    √√  √√√      √√√√  √√√√√    √√√√
   √    √  √      √  √      √  √  √  √  √      √
   √    √  √      √  √              √      √
   √√√√  √      √    √√          √        √√
   √    √  √      √        √        √            √
   √    √  √      √          √      √              √
   √    √  √      √  √      √      √      √      √
 √√    √√  √√√    √√√√      √√√    √√√√
-----------------------------------------------------------
 如有360、电脑管家等安全软件提醒，请勾选允许和不再提醒！

 警告：执行该命令 您的hosts将被自动替换覆盖！
 如您原先的hosts有自己修改过的信息，请自行手动修改！

 -----------------------------------------------------------
 请选择使用：

 1.使用穿墙hosts（即在下面输入1）

 2.恢复初始hosts（即在下面输入2）
-----------------------------------------------------------
    ''')
    key = '1'     # input('')
    if key == '1':
        with open(r"源hosts.txt", 'w+', encoding='utf-8') as hf:

            #hosts  在run（）中已获取
            hf.write(hosts)
            print('hosts已保存至文件！')
            update_log = hosts.split('\n')[2][2:] + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #文件升级时间 + 开机更新时间记录
        os.popen(r'type 源hosts.txt > "%SystemRoot%\System32\drivers\etc\hosts"')
        if os.path.exists(r'补充hosts.txt'):
            os.popen(r'type 补充hosts.txt >> "%SystemRoot%\System32\drivers\etc\hosts"')
            print(r'补充hosts已加入')
        os.popen(update_log)
        os.popen(r'echo ' + update_log + ' >> log.log')
        os.popen(r'ipconfig/flushdns')
        print('''
-----------------------------------------------------------

 恭喜 覆盖本地hosts并刷新本地DNS解析缓存成功!

 现在去打开Google、Twitter、Facebook、Gmail、谷歌学术吧！

 谷歌这些网站记得使用https进行加密访问！

 即：https://www.google.com

 或者: https://www.google.com/ncr
       https://www.google.com.hk/ncr
-----------------------------------------------------------
''')
    elif key == '2':
        os.popen(r'cls')
        os.popen(r"echo 127.0.0.1 localhost > %SystemRoot%\System32\drivers\etc\hosts")
        os.popen(r'echo [%date:~0,4%-%date:~5,2%-%date:~8,2%] %time:~0,8%   恢复hosts')
        os.popen(r'echo [%date:~0,4%-%date:~5,2%-%date:~8,2%] %time:~0,8%   恢复hosts>> log.log')
        print(r'恭喜您，hosts恢复初始成功!')
    else:
        print('输入错误')
    time.sleep(1)
    winsound.Beep(700, 800)
    