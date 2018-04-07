
# coding: utf-8

# In[33]:

import time
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import os
import json


# In[43]:

def get_content(url,headers={},timeout=60):
    head = {'Referer':'http://www.9ku.com/laoge/70.htm',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    }
    head = headers or head 
    response = requests.get(url,headers=head,timeout=timeout)
    return response  


def download_audio(aid=None,working_folder = ''):
    if aid == None:
        raise KeyError('参数 应输入歌曲id')
    else:
        pass

    working_folder =  os.path.join('.',working_folder)
    if not os.path.exists(working_folder):
        os.makedirs(working_folder)
    try:
        r = get_content('http://www.9ku.com/html/playjs/66/{0}.js'.format(aid),timeout=7)
    except requests.exceptions.ConnectTimeout as er :
        print('[解析失败] ')
        return 'False'
    info = json.loads(r.text[2:-1])
    filename = os.path.join(working_folder,info['mname'] + info['wma'][-4:])
    if os.path.exists(filename):
        print('[已存在]  ', filename)
        return 'Jump'
    else:
        src = info['wma']
        try:
            with open(filename,'wb') as f:
                f.write(get_content(src,timeout=15).content)
        except requests.exceptions.ConnectTimeout as er :
            print('[下载失败] ')
            return 'False'

        if os.path.exists(filename):
            print('[下载成功] ',filename)
            return 'True'
        else:
            return 'False'





start_url = 'http://www.9ku.com/laoge/70.htm'

page = get_content(start_url).text
soup = BeautifulSoup(page,'lxml')
s = soup.find_all('a',class_='songName')
ids = [i['href'][6:-4] for i in s]
print('Number of song:',len(ids))


sleeptime = 1
for aid in ids:
    result = download_audio(aid,'音乐')
    time.sleep(sleeptime)
    if result is 'True': 
        sleeptime -= 0.1
    elif result is 'False': 
        sleeptime += 0.5
    else:
        pass
    sleeptime = min(30, max(0.5,sleeptime))