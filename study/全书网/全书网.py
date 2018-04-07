# _*_ utf-8 _*_
import requests
import random
from bs4 import BeautifulSoup
import re
import time
import datetime
class Book_spider():


    '''
    所有章节列表页面
    '''
    def items_list(self):
        book_request = requests.get(self.url, headers=random.choice(self.headers))
        book_request.encoding = 'gbk'#看网站编码是什么，不然就会爬出的数据是乱码       
        book_obj = BeautifulSoup(book_request.text, 'html.parser')
        book_divs = book_obj.find_all('a')#找到所有章节的a标签连接
        for item in book_divs:
            if 'book/0' in item.attrs['href']:#筛选掉无用的a标签连接
                time.sleep(3)#暂停三秒防止ip被封
                title = item.text
                self.item_content(item.attrs['href'],title)     
    
    '''
    每章节的正文内容
    '''
    def item_content(self, item_url, title):
        content_request = requests.get(item_url, headers=random.choice(self.headers))
        if content_request.status_code == 200:
            content_request.encoding = 'gbk'
            content_obj = BeautifulSoup(content_request.text, 'html.parser')
            content_obj.encode('utf-8')
            content = content_obj.find('div', attrs={'id': 'content'})        
            with open('xianni.txt', 'a', encoding='utf-8') as f:#将小说保存到txt文件中
                f.write('\n'+title+'\n')
                info_text = content.text.split(' ')
                for info in info_text:                
                    if info != '\n' and info != '':
                        '''
                        因为编码格式问题会报错如下：
                        UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 9: illegal multibyte sequence
                        info.replace(u'\xa0', u' ')  用此方法可保存，后面的两个替换是因为每页都有这样的两个多余字符串
                        '''
                        
                        f.write(info.replace(u'\xa0', u' ').replace(u'style5();',u' ').replace(u'style6();',u' '))
                        
                print(title+' 爬取完成')


    def __init__(self,url=None):
        self.url = url or 'http://www.quanshuwang.com/book/0/567'
        self.headers = [
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
        {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
        ]
        
        '''
        MAX_RETRIES = 20
        session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
        session.mount('https://', adapter)
        session.mount('http://', adapter)
        self.get = session.get
        '''
        print('start: %s' % str(datetime.date.today())+" "+time.strftime("%H:%M:%S"))
        self.items_list()
        print('end: %s' % str(datetime.date.today())+" "+time.strftime("%H:%M:%S"))
bs = Book_spider()