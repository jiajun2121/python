#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun time:2017/12/25

import pymysql


# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='rtpswd123',
                             db='testdb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
'''
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'zhyea.com',
          'db':'employees',
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }
connection = pymysql.connect(**config)
'''


# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('liu', 'bei', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()
cursor.execute("SELECT * from employee")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
import pprint as p
p.pprint(data)

# 关闭数据库连接
db.close()


'''
# 使用 execute() 方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
'''