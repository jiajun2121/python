import urllib.request
import chardet
import re
import os
import threading
import time
import winsound


def geturl(pageurl):
    i = 0
    while i < 3:
        try:
            req = urllib.request.Request(pageurl)
            req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
            req.add_header('Referer', 'http://cl.3m4.xyz/htm_data/16/1708/2553516.html')
            
            resp = urllib.request.urlopen(req)
            
            return resp.read()
        except:
            return 'error'
        i -= 1


def htmldecode(html):
    if html != 'error':
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
        with open(path + '\\' + filename + url[-4:-1] + url[-1], 'wb') as f:
            f.write(page)


def download_tz_pic(pth, the_dir, pic_link):
    os.chdir(pth)
    os.mkdir(the_dir)
    time.sleep(0.5)
    os.chdir(pth + '\\' + the_dir)
    pics = getpiclist(pic_link)
    
    print('第', (page_idx - 1) * 90 + tiezi_idx + 1, '贴图片数：', len(pics))
    threads = []
    for pic_idx in range(len(pics)):
        pic_task = threading.Thread(target=savepic, args=(pics[pic_idx], str(pic_idx), str(pth + '\\' +dirname)))
        threads.append(pic_task)
    for pic_task in threads:
        pic_task.setDaemon(True)
        pic_task.start()
    time.sleep(min(max(len(threads) / 4, 1.5), 7))
    
    print(' = 下 载 完 成 = \n')
    os.chdir(pth)

if __name__ == '__main__':
    host = 'http://cl.3m4.xyz/'
    addr = 'thread0806.php?fid=16&search=&page=1'

    url = host+addr
    print('正在建立存储文件夹...')
    if not os.path.exists('CLpicture'):
        os.mkdir('CLpicture')
    os.chdir('CLpicture')
    pth = os.getcwd()
    # bg = int(input('qs页码: '))
    # ed = int(input('终止页码: '))
    for page_idx in range(1, 10):
        url = url[0:-1] + str(page_idx)
        print('正在获取帖子列表...')
        links = getpagelist(url)
        
        tiezi_task = []
        for tiezi_idx in range(len(links)):
            if 'htm_data/' not in links[tiezi_idx][0]:
                continue
            link = host + links[tiezi_idx][0]
            
            dirname = str(links[tiezi_idx][1])

            if os.path.exists(dirname):  # 已存在文件夹则认为以下载完成 跳过
                pass
                # print(link, '已存在')
            else:
                os.chdir(pth)
                os.mkdir(dirname)
                os.chdir(pth + '\\' + dirname)
                pics = getpiclist(link)
                print(dirname)
                print('第', (page_idx - 1) * 90 + tiezi_idx + 1, '贴图片数：', len(pics))
                threads = []
                for pic_idx in range(len(pics)):
                    pic_task = threading.Thread(target=savepic,    args=(pics[pic_idx], str(pic_idx), str(pth + '\\' + dirname)))
                    threads.append(pic_task)
                for pic_task in threads:
                    pic_task.setDaemon(True)
                    pic_task.start()
                time.sleep(min(max(len(threads) / 4, 1.5), 7))
                
                print(' = 下 载 完 成 = \n')
                os.chdir(pth)
                os.chdir('..')
        '''
                task = threading.Thread(target=download_tz_pic, args=(pth, dirname, link))
                tiezi_task.append(task)
        for task in tiezi_task:
            task.setDaemon(True)
            task.start()
        '''
            
        # time.sleep(10)
        # for task in tiezi_task:
            #task.join()








