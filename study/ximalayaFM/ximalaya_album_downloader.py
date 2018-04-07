#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2018/1/29

import json
import re
import os
import sys
import time
import threading
import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup

hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Cookie': '_xmLog=xm_1517326971206_jd1tavyekbpnt3; trackType=web; x_xmly_traffic=utm_source%3A%26utm_medium%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1517326972; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1517326972; _ga=GA1.2.593201155.1517326972; _gat=1'
    
}

session = requests.Session()
session.mount('http://', HTTPAdapter(max_retries=3))
session.mount('https://', HTTPAdapter(max_retries=3))


def get_page_content(pageurl, data=None):
    """
    接受url data
    返回 response 对象
    :rtype: Resopnse
    """
    try:
        global session
        response = session.get(pageurl, headers=hd, timeout=10, params=data)
        
        # response = requests.get(pageurl, headers=hd, timeout=5)
        return response
    except Exception as er:
        print(er)
        with requests.Response() as r:
        	r.status_code=404
        	return r 


def get_album_content(album_id='4310827'):
    """
    接受专辑id album_id
    返回该专辑中所有音频的 id 的列表
    :rtype: list
    """
    sounds_id = []
    for page_number in range(1, 100):
        
        data = {'url': '/album/more_tracks',
                'aid': album_id,
                'page': page_number}
        
        url = r'http://m.ximalaya.com/album/more_tracks'
        s = get_page_content(url, data=data).json()
        sounds_id.extend(s['sound_ids'])
        print(s['sound_ids'])
        time.sleep(0.5)
        if s['next_page'] == 0:
            return sounds_id
        
        '''
        page = get_page_content(url, data=data).text

        soup = BeautifulSoup(page, 'lxml')
        results = soup.find_all('a', class_='title')
        s = [sound.get('href', None).split('/')[-2] for sound in results if sound.get('href', None) is not None]
        sounds_id.extend(s)
        if len(s) < 50:
            break
        '''
    return sounds_id


def get_sound_info(sound_id='38335071'):
    '''
    接受音频id
    返回该音频的字典格式信息
    :param sound_id:
    :return:
    '''
    sound_json_url = 'http://www.ximalaya.com/tracks/{0}.json'.format(sound_id)
    sound_info = json.loads(get_page_content(sound_json_url).text)
    return sound_info


def download_audio(sound_info, saved_path='.\\'):
    '''
    接受字典格式音频信息
    保存音频文件到给定目录，或默认当前目录
        保存路径为 专辑名/音频文件名
    
    :param sound_info:
    :param saved_path:
    :return:
    '''
    
    sid = sound_info['id']
    audio_name = sound_info['title']
    album_name = re.sub(r'[\\/| ]', '_', re.sub(r'[:*?"><]', '', sound_info['album_title'])).replace(' ', '')
    audio_src_url = sound_info['play_path_64'] or sound_info['play_path_32'] or sound_info['play_path']
    audio_format = audio_src_url.split('.')[-1]
    
    working_floder = os.path.join(saved_path, album_name)
    download_record_file = os.path.join(working_floder, '{0}.download_record.txt'.format(sid))
    file_name_path = os.path.join(working_floder, audio_name + r'.' + audio_format)
    
    if not os.path.exists(os.path.abspath(working_floder)):
        os.makedirs(working_floder)
    if os.path.exists(download_record_file):
        with open(download_record_file, 'r+', encoding='utf8')as f:  # 如果在下载记录中，视为已下载，跳过
            f.seek(0)
            if str(sid) in f.read().split('\n'):
                print('已存在 ', sid, audio_name)
                return None
    if not os.path.exists(file_name_path):
        response = get_page_content(audio_src_url)
        if 200 <= response.status_code <= 400:
            audio_data = response.content
            print('下载 ', file_name_path)
            with open(file_name_path, 'wb') as f:
                f.write(audio_data)
            with open(download_record_file, 'a+', encoding='utf8') as  recd:
                recd.write(str(sound_info['id']) + '\n')
        else:
            print('已存在 ', file_name_path)


def download_album(album_id, saved_path=r'.\\'):
    sounds_id = get_album_content(album_id)

    for sid in sounds_id:
        j = get_sound_info(sid)
        download_audio(j, saved_path)
        time.sleep(2)



if __name__ == '__main__':

	for album_id in sys.argv[1:]:
	    download_album(album_id)
	    time.sleep(10)
