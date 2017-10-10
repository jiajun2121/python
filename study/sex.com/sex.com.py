import urllib.request
import chardet
import re
import os
import threading
import time
import winsound


def geturl(pageurl,i= 3):
    while i>0 :
        try:
            req = urllib.request.Request(pageurl)
            req.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
            resp = urllib.request.urlopen(req)

            return resp.read()
        except:
            pass
        return 'error'


def htmldecode(html):
    if html != 'error':
        try:
            return html.decode('utf-8')
        except:
            fencoding = chardet.detect(html)['encoding']
            if fencoding == 'GB2312':
                fencoding = 'GBK'
            return html.decode(fencoding)
    else:
        print('error')
        return 'error'


def getpagelist(url):
    page = htmldecode(geturl(url))
    reg = re.compile(r'(\s)')
    page = re.sub(reg, '', page)

    reg = re.compile(r'(https://images.sex.com/(?:.*?).(?:(?:jpg)|(?:gif)|(?:png)))')
    linkslist = reg.findall(page, re.S| re.M)

    return  linkslist

def savepic(url, filename='', path = os.getcwd()):

    page = geturl(url)
    if page != 'error':
        try:
            print('page get')
            print('wenjianming','\n' in (filename))
            with open(filename, 'wb') as f:
                f.write(page)
            print('保存成功',next(counter),path + '\\' + filename)
        except Exception as error:
            print('保存出错',error)
    else:
        print('访问图片链接失败')
            

def count():
    c = 1
    while True:
        yield c
        c += 1


# ############### #
#    运行部分      #
if __name__ == '__main__':
    os.system('title ' + str(__file__))
    host = 'https://www.sex.com/'
    addr = '?&page=1'

    url = host + addr


    #bg = abs(int(input(' 起始页码: ')))

    #ed = abs(int(input(' 终止页码: ')))



    if not os.path.exists('picture'):
        os.mkdir('picture')
    os.chdir('picture')
    pth = os.getcwd()


    tiezi_task = []
    links = []
    with open(r'..\\lk.txt','r',encoding='utf-8') as f:
        links = list(set(f.readlines()))
    for eachlink in links:
        dirname = eachlink.split('/')[-1].replace('\n','')
        if not os.path.exists(dirname):
            task = threading.Thread(target=savepic, args=(eachlink, dirname, pth))
            tiezi_task.append(task)
    print(len(tiezi_task))
    for task_idx in range(len(tiezi_task)):
        tiezi_task[task_idx].setDaemon(True)
        tiezi_task[task_idx].start()
        print('run task')
        if task_idx % 25 == 0:
            time.sleep(2)
        else:
            pass
    for task in tiezi_task:
        task.join()
    print('one page over')
    os.chdir(pth)

   

    for page_idx in range(1, 5):
        url = url[0:-1] + str(page_idx)
        print('正在获取帖子列表...')
        links = getpagelist(url)
        print('已获取')
        for each in links:
            with open('lk.txt','a',encoding='utf-8') as f:
                f.write(each+ '\n')
                print(each)

    os.system('for /f "tokens=*" %%i in ("dir/s/b/ad^|sort /r") do rd "%%i"')
