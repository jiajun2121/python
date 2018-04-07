#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/11/30
import math
import requests
import json
from bs4 import BeautifulSoup

'''
网站搜索到的文件的相关信息

'''


class FileWithMagnet:
    '''
    f = FileWithMagnet(title=None, hashcode=None, hot=0, size=None)
    
    
    获取文件磁力链接
    magnet_link = f.source
    
    设置文件属性
    f.content = {'title': title, 'hashcode': hashcode, 'hot': hot, 'size': size}

    '''
    
    def __init__(self, title=None, hashcode=None, hot=0, size=None):
        self.title = title
        self.hashcode = hashcode
        self.sharedate = None
        self.hot = hot
        self.size = size
        self._dict = None  # {'title': self.title, 'hashcode': self.hashcode, 'hot': self.hot, 'size': self.size}
    
    @property
    def source(self):
        return 'magnet:?xt=urn:btih:'.join(self.hashcode)
    
    @source.setter
    def source_setter(self):
        pass
    
    @property
    def content(self):
        """
        :rtype: dict

        """
        return self.__repr__()
    
    @content.setter
    def content_setter(self, dict_values):
        self.title = dict_values['title']
        self.hashcode = dict_values['hashcode']
        self.hot = dict_values['hot']
        self.size = dict_values['size']
        self.sharedate = dict_values['sharedate']
    
    def __repr__(self):
        '''
        
        :return:
        '''
        return repr(self.__dict__)
    
    @property
    def to_dict(self):
        return self.__dict__


'''
任意搜索关键词所对应的搜索结果
'''


class FanHao:
    def __init__(self, fanhao=''):
        self.fanhao = ''.join([i for i in fanhao if i == '-' or i.isalnum()]).upper()
        self.magnet = []
        self.list_of_file_dict = []
        
        if (fanhao is None) or not isinstance(self.fanhao, str):
            pass
    
    def download(self, limit=5, sort_key=None):
        if self.fanhao == '':
            raise ValueError('初始化时应输入搜索关键词')
        limit = max(limit, 1)
        
        html = requests.get('http://www.btava.cc/s/{0}.html'.format(self.fanhao))
        # get link
        soup = BeautifulSoup(html.content, 'html5lib')
        bt_list = soup.find_all('div', 'bt_list')
        for bt_file in bt_list:
            file = FileWithMagnet()
            file.title = bt_file.find_all('a')[0].text
            
            file.hashcode = bt_file.find_all('span', 'yak')[0].find_all('span', 'label-danger')[0].text
            
            Tmp = bt_file.find_all('span', 'label')
            file.sharedate = Tmp[0].text
            file.hot = Tmp[1].text.replace('°C', '')
            file.size = Tmp[2].text.upper().replace('GB', '')
            self.magnet.append(file)
            
            if len(self.magnet) > limit:
                break
        if sort_key is not None:
            try:
                self.magnet.sort(key=lambda x: x[sort_key], reverse=True)
            except KeyError:
                pass
    
    @property
    def to_list(self):
        
        self.list_of_file_dict = [each.to_dict for each in self.magnet]
        return self.list_of_file_dict
    
    def save(self, filename=None):
        if filename is None:
            filename = self.fanhao
        s = self.to_list
        savestr = json.dumps(s, indent=4)
        with open(filename + '.txt', 'w+', encoding='utf8') as sf:
            sf.write(savestr)


if __name__ == '__main__':
    '''
    with open('IPZ-573.txt') as ff:
        mag_json = ff.read()
        mag = json.loads(mag_json)
        mag.sort(key=lambda x: x['hot'], reverse=True)
    '''
    m = FanHao('MXGS-754')
    m.download()
    print(m.fanhao)
    m.save()





