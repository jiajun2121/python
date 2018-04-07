#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2018/2/7

import requests
import pymysql
import json
'''
Property	Description	Type	Basic	Advance	Premium	Default
id	条目id	str	Y	Y	Y	-
title	中文名	str	Y	Y	Y	-
original_title	原名	str	Y	Y	Y	''

alt	条目页URL	str	Y	Y	Y	-
mobile_url	移动版条目页URL	str	Y	Y	Y	-
ratings_count	评分人数	int	Y	Y	Y	0
wish_count	想看人数	int	Y	Y	Y	0
collect_count	看过人数	int	Y	Y	Y	0
do_count	在看人数，如果是电视剧，默认值为0，如果是电影值为null	int	Y	Y	Y	0 / null
subtype	条目分类, movie或者tv	str	Y	Y	Y	movie
douban_site	豆瓣小站	str	Y	Y	Y	''
year	年代	str	Y	Y	Y	''
summary	简介	str	Y	Y	Y	''
comments_count	短评数量	int	Y	Y	Y	0
reviews_count	影评数量	int	Y	Y	Y	0
seasons_count	总季数(tv only)	int	Y	Y	Y	0 / null
current_season	当前季数(tv only)	int	Y	Y	Y	0 / null
episodes_count	当前季的集数(tv only)	int	Y	Y	Y	0 / null
schedule_url	影讯页URL(movie only)	str	Y	Y	Y	''
aka	又名	array	Y	Y	Y	[]
images	电影海报图，分别提供288px x 465px(大)，96px x 155px(中) 64px x 103px(小)尺寸	dict	Y	Y	Y	-
rating	评分，见附录	dict	Y	Y	Y	-
genres	影片类型，最多提供3个	array	Y	Y	Y	[]
countries	制片国家/地区	array	Y	Y	Y	[]
directors	导演，数据结构为影人的简化描述，见附录	array	Y	Y	Y	[]
casts	主演，最多可获得4个，数据结构为影人的简化描述，见附录	array	Y	Y	Y	[]




'''


def get_movie_info(id=None):
    url = 'http://api.douban.com/v2/movie/subject/{id}'.format(id=id)
    infomation = requests.get(url, timeout=7).json()
    '''
    original_title = infomation['original_title']
    mov_id = infomation['id']
    title = infomation['title']
    aka = infomation['aka']
    alt = infomation['alt']
    mobile_alt = infomation['mobile_alt']
    rating = infomation['rating']
    ratings_count = infomation['ratings_count']
    subtype = infomation['subtype']
    languages = infomation['languages']
    images = infomation['images']
    wish_count = infomation['wish_count']
    collect_count = infomation['collect_count']
    '''

    return infomation


def insert(database, info):
    douban_id = int(info['id'])
    title = info['title'].join(["\'"]*2)
    o_title = info['original_title'].join(["\'"]*2)
    aka = json.dumps(info['aka']).join(["\'"]*2)
    m_url = info['mobile_url'].join(["\'"]*2)
    year = info['year']
    genres = json.dumps(info['genres']).join(["\'"]*2)
    alt = info['alt'].join(["\'"]*2)

    # SQL 插入语句
    sql = """INSERT INTO t_douban_movie(douban_id, title, original_title, aka, alt, mobile_url, `year`, genres)
             VALUES ({0}, {1},{2},{3},{4},{5},{6},{7})""".format(douban_id, title, o_title, aka, alt, m_url, year, genres)
    cursor = database.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        database.commit()
        return True
    except Exception as er:
        if er.args[0] != 1062:  # 主键已存在，忽略打印Exception
            print(er)
        # 如果发生错误则回滚
        database.rollback()
        return False


def save_to_db(db_config, info):

    db = pymysql.connect(**db_config)

    insert(db, info)
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    info = get_movie_info('26628256')
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'program_user',
        'password': 'A9AB6F4E55E031B9C6877E316C9F5A0E',
        'db': 'db_movie',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    save_to_db(config, info)
