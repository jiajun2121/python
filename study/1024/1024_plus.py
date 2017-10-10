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
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
        resp = urllib.request.urlopen(req)

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
    page = htmldecode(geturl(url))
    reg = re.compile(r'(\s)')
    page = re.sub(reg, '', page)

    reg = re.compile(
        r'h3><ahref="((?:.*?).html)"target="_blank"id="">(?:<fontcolor=green>){0,1}(.*?)(?:</font>){0,1}</a><')

    linkslist = reg.findall(page)
    while 'P]' not in linkslist[0][1]:
        linkslist.pop(0)
    while len(linkslist) < 10:  ##########
        print('重获帖子列表...')
        linkslist = getpagelist(url)
    return linkslist


# <a href="htm_data/16/1708/2574533.html" target="_blank" id=""><font><font>日你个老逼[11P]</font></font></a>

def getpiclist(url):
    page = htmldecode(geturl(url))
    reg = re.compile(r'(\s)')
    page = re.sub(reg, '', page)

    reg = re.compile(r"<inputsrc='((?:.*?).[jJ][pP][gG])'type='image'")
    piclist = reg.findall(page)

    return piclist


def savepic(url, filename, path):
    page = geturl(url)
    if page != 'error':
        try:
            with open(path + '\\' + filename + url[-4:-1] + url[-1], 'wb') as f:
                f.write(page)
        except: Exception

def count():
    c = 1
    while True:
        yield c
        c +=1


def download_tz_pic(pth, the_dir, pic_link):
    tiezi_count  = next(counter)
    os.chdir(pth)
    try:
        if not os.path.exists(the_dir):
            os.mkdir(the_dir)
        os.chdir(pth + '\\' + the_dir)
    except: Exception

    if not (os.path.exists('0.jpg')) or (os.path.exists('1.jpg')) or (os.path.exists('2.jpg')):
        pics = getpiclist(pic_link)


        threads = []
        for pic_idx in range(len(pics)):
            pic_task = threading.Thread(target=savepic, args=(pics[pic_idx], str(pic_idx), str(pth + '\\' + the_dir)))
            threads.append(pic_task)
        for pic_task in threads:
            pic_task.setDaemon(True)
            pic_task.start()
        time.sleep(min(max(len(threads) / 4, 1.5), 7))
        print('第', tiezi_count, '贴: 图片数：', len(pics))
        print('<<下 载 完 成>>  ',the_dir,'\n')


# ############### #
#    运行部分      #
if __name__ == '__main__':
    host = 'http://cl.3m4.xyz/'
    addr = 'thread0806.php?fid=16&search=&page=1'

    url = host + addr
    print('''
 None:   网站每页90贴
         页码: 1-127
''')


    bg = abs(int(input(' 起始页码: ')))

    ed = abs(int(input(' 终止页码: ')))
    print('正在建立存储文件夹...')
    if not os.path.exists('CLpicture'):
        os.mkdir('CLpicture')
    os.chdir('CLpicture')
    pth = os.getcwd()

    counter = count()
    for page_idx in range(bg, ed):
        url = url[0:-1] + str(page_idx)
        print('正在获取帖子列表...')
        links = getpagelist(url)
        print('已获取')
        tiezi_task = []
        for tiezi_idx in range(len(links)):
            if 'htm_data/' not in links[tiezi_idx][0]:
                continue
            link = host + links[tiezi_idx][0]

            dirname = str(links[tiezi_idx][1])


            task = threading.Thread(target=download_tz_pic, args=(pth, dirname, link))
            tiezi_task.append(task)
        for task_idx in range(len(tiezi_task)):
            tiezi_task[task_idx].setDaemon(True)
            tiezi_task[task_idx].start()
            if task_idx % 25 == 0:
                time.sleep(10)

        time.sleep(10)
        # for task in tiezi_task:
        # task.join()
    os.chdir(pth)
    os.system('for /f "tokens=*" %%i in ("dir/s/b/ad^|sort /r") do rd "%%i"')
