import requests
import urllib.request
import chardet
import re
import os
import threading
import time
import winsound


def geturl(pageurl):
    try:
        req = urllib.request.Request(pageurl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
        resp = urllib.request.urlopen(req, timeout=5)

        return resp.read()
    except:
        return 'error'


def htmldecode(html):
    if html != 'error':
        try:
            return html.decode('utf8')
        except:
            fencoding = chardet.detect(html)['encoding']
            if fencoding == 'GB2312':
                fencoding = 'GBK'
            return html.decode(fencoding)
    else:
        print('error')
        return 'error'


def getpagelist(url):
    resp = requests.get(url)
    page = resp.text.encode(resp.encoding).decode(r'utf-8')
    # reg = re.compile(r'(\s)')
    # page = re.sub(reg, '', page)

    reg = re.compile(r'href="(/touxiang/qinglv/2017/(?:.*?).html)" class="imgTitle"')
    linkslist = reg.findall(page)
    while len(linkslist) < 10:  ##########
        print('重获帖子列表...')
        linkslist = getpagelist(url)
    return linkslist


# <a href="htm_data/16/1708/2574533.html" target="_blank" id=""><font><font>日你个老逼[11P]</font></font></a>

def getpiclist(url):
    page = htmldecode(geturl(url))
    reg = re.compile(r'(\s)')
    page = re.sub(reg, '', page)

    reg = re.compile(r'href="(http://img2.woyaogexing.com/(?:.*?).[jJp][pPn][gGg])"')
    piclist = reg.findall(page)

    return piclist


def savepic(picture_link, filename, savepath):

    page = geturl(picture_link)
    if page == 'error':
        pass
    elif os.path.exists(filename):
        print('existed')
    else:
        try:
            with open(savepath + '\\' + filename + picture_link[-4:], 'wb') as f:
                f.write(page)
        except Exception as er:
            print(er)


def count():
    c = 1
    while True:
        yield c
        c += 1



def download_tz_pic(savepath, groupname, picture_link):
    tiezi_count  = next(counter)

    if not (os.path.exists('0.jpg')) or (os.path.exists('1.jpg')) or (os.path.exists('2.jpg')):
        pics = getpiclist(picture_link)


        threads = []
        for pic_idx,piclink in enumerate(pics):
            pic_task = threading.Thread(target=savepic, args=(piclink, groupname + '_' + str(pic_idx) + '_' + piclink.split('/')[-1].split('!')[0], savepath))
            threads.append(pic_task)
        for pic_task in threads:
            pic_task.setDaemon(True)
            pic_task.start()
        time.sleep(min(max(len(threads) / 4, 1.5), 7))
        print('第', tiezi_count, '贴: 图片数：', len(pics))
        print('<<下 载 完 成>>  ', groupname, '\n')


# ############### #
#    运行部分      #
if __name__ == '__main__':
    host = 'http://www.woyaogexing.com/'
    addr = 'touxiang/qinglv/index_{0}.html'

    url = host + addr
    print('''
 None:   网站每页90贴
         页码: 1-127
''')

    bg,ed =1,5
    bg = abs(int(input(' 起始页码: ')))

    ed = abs(int(input(' 终止页码: ')))

    print('正在建立存储文件夹...')
    if not os.path.exists('picture'):
        os.mkdir('picture')
    os.chdir('picture')
    pth = os.getcwd()

    counter = count()
    for page_idx in range(bg, ed):
        if page_idx == 1:
            url = host + 'touxiang/qinglv/index.html'
        else:
            url = url.format(str(page_idx))
        print('正在获取帖子列表...')
        links = getpagelist(url)
        print('已获取')
        tiezi_task = []
        for tiezi_idx in range(len(links)):

            link = host + links[tiezi_idx]

            groupname = link.split(r'/')[-1].split(r'.')[0]
            if os.path.exists(groupname + '_1'):
                print('existed')
            else:
                download_tz_pic(pth, groupname, link)
            
        time.sleep(10)
        # for task in tiezi_task:
        # task.join()
    os.chdir(pth)
    os.popen('for /f "tokens=*" %%i in ("dir/s/b/ad^|sort /r") do rd "%%i"')
