# coding=utf-8

"""
Created on 2016-04-24 @author: Eastmount
功能: 爬取新浪微博用户的信息及微博评论
网址:http://weibo.cn/ 数据量更小 相对http://weibo.com/
"""
import datetime
import time
import re
import os
import sys
import codecs
import shutil
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

#先调用浏览器chrome
driver = webdriver.Chrome()
wait = ui.WebDriverWait(driver,10)

#全局变量 文件操作读写信息
inforead = codecs.open("SinaWeibo_List_best_1.txt", 'r', 'utf-8')
infofile = codecs.open("SinaWeibo_Info_best_1.txt", 'a', 'utf-8')
follow = codecs.open("SinaWeibo_FollowNumber.txt",'a','utf-8')
#********************************************************************************
#							第一步: 登陆weibo.cn
#		该方法针对weibo.cn有效(明文形式传输数据) weibo.com见学弟设置POST和Header方法
#				LoginWeibo(username, password) 参数用户名 密码
#********************************************************************************

def LoginWeibo(username, password):
	try:
		#输入用户名/密码登录
		print(u"准备登陆Weibo.cn网站...")
		driver.get("http://login.sina.com.cn/")
		elem_user = driver.find_element_by_name("username")
		elem_user.send_keys(username) #用户名
		elem_pwd = driver.find_element_by_name("password")
		elem_pwd.send_keys(password) #密码
		#elem_rem = driver.find_element_by_name("safe_login")
		#elem_rem.click()			 #安全登录

		#重点: 暂停时间输入验证码(http://login.weibo.cn/login/ 手机端需要)
		time.sleep(20)

		#elem_sub = driver.find_element_by_xpath("//input[@class='smb_btn']")
		#elem_sub.click()			 #点击登陆 因无name属性
		#如果登陆按钮采用动态加载 则采用输入回车键登陆微博
		elem_pwd.send_keys(Keys.RETURN)
		time.sleep(2)

		#获取Coockie 推荐资料:http://www.cnblogs.com/fnng/p/3269450.html
		print(driver.current_url)
		print(driver.get_cookies() ) #获得cookie信息 dict存储
		print(u'输出Cookie键值对信息:')
		for cookie in driver.get_cookies():
			#print cookie
			for key in cookie:
				print(key, cookie[key])

		#driver.get_cookies()类型list 仅包含一个元素cookie类型dict
		print(u'登陆成功...')


	except Exception as e:
		print("Error: ",e)
	finally:
		print(u'End LoginWeibo!\n\n')



#********************************************************************************
#				 访问http://s.weibo.com/页面搜索热点信息
#				 爬取微博信息及评论，注意评论翻页的效果和微博的数量
#********************************************************************************

def GetComment(key):
	try:
		global infofile	  #全局文件变量
		driver.get("http://s.weibo.com/")
		print('搜索热点主题:', key)

		#输入主题并点击搜索
		item_inp = driver.find_element_by_xpath("//input[@class='searchInp_form']")
		item_inp.send_keys(key)
		item_inp.send_keys(Keys.RETURN)	#采用点击回车直接搜索

		
	except Exception as e:
		print("Error: ",e)
	finally:
		print('Search!\n\n')
		print('**********************************************\n')


#*******************************************************************************
#								程序入口 预先调用
#		 注意: 因为sina微博增加了验证码,但是你用Firefox登陆输入验证码
#		 直接跳转到明星微博那部分,即: http://weibo.cn/guangxianliuyan
#*******************************************************************************

if __name__ == '__main__':
	
	os.system('title 微博爬虫')
	#os.system('mode con lines=40 cols=80')
	os.system('color 0a')
	
	#定义变量
	username = 'zhao1429175876@163.com'			 #输入你的用户名
	password = 'supper.zhao.'			  #输入你的密码
	user_id =str("2303490360")

	#操作函数
	LoginWeibo(username, password)	  #登陆微博
	os.system("cls")
	#在if __name__ == '__main__':引用全局变量不需要定义 global inforead 省略即可


	#搜索热点微博 爬取评论
	#global infofile	  #全局文件变量
	lst = [u"颜末",u"郑合惠子"]
	for key in lst:
		for x in range(20):
			time.sleep(3)
			driver.get("http://s.weibo.com/")
			print('搜索热点主题:', key)

			#输入主题并点击搜索
			item_inp = driver.find_element_by_xpath("//input[@class='searchInp_form']")
			item_inp.send_keys(key)
			item_inp.send_keys(Keys.RETURN)	#采用点击回车直接搜索

	
	
	
	
	#GetComment(key)
	
	print("爬取完毕,即将退出浏览器")
	time.sleep(3)
	
	driver.quit()
	os.system('exit')
	infofile.close()
	inforead.close()
	follow.close()

