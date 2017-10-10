#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/9/26

import urllib.request
import threading
import time
import os
import json



class HOSTS_thread():
    def __init__(self, urls, copy=3):
        self.isover = False
        self.urls = urls
        self.childThread = []
        self.hosts = ''
        self.ThreadCopy = copy
    
    def run(self):
        print(threading.enumerate())
        for url in self.urls:
            #for i in range(self.ThreadCopy):
                task = threading.Thread(target=self.gethosts, args=('',url))
                self.childThread.append(task)
        
        for task in self.childThread:
            task.setDaemon(True)
            task.start()
        #print(threading.enumerate())
        while not self.isover:
            time.sleep(3)

    
    def gethosts(self,_ , _url):
        try:
            print('正在获取hosts列表...')
            self.hosts = self._getpage(_url)
            if not self.isover:
                self.isover = True
                print('获取hosts列表完成')
        except Exception as e:
            if not self.isover:
                print('get hosts error',e)

    def _getpage(self, _url):
        try:
            print(_url)
            request = urllib.request.Request(_url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')
        
            page_data = urllib.request.urlopen(request).read()
            try:
                page_data = page_data.decode('utf-8')
            except:
                if not self.isover:
                    print('ERROR')
            print('获取网页完成')
        
            return page_data
        except Exception as e:
            if not self.isover:
                print('get page error')


if __name__ == '__main__':
    hostsurls = ['https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts',
                 'https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts-files/hosts']
    
    h = HOSTS_thread(urls=hostsurls)
    h.run()
    
    with open('save.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(h.hosts.replace('\t',' ').split('\n')  ,indent=4))
