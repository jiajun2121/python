import urllib.request
import re


class Novel:
    def __init__(self, novelurl):
        self.url = novelurl
        self._novel_home_page = None
        self.chpaters = []
        self.chpater_link = []
        self.NovelName = self.url
        self.chpater_regular = r'style="" href="(.*?)">(.*?)</a>'
        self.content_regular = r'<div id="content"(?:.*?)>\s{0,}(.*?)\s{0,}</div>'
        self.NovelName_reqular = ''
        self.NovelLength = 0
        
        self._novel_home_page = self._getpage(self.url)
    
    def _getpage(self, theurl):
        try:
            request = urllib.request.Request(theurl)
            request.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')
            page = urllib.request.urlopen(request)
            page = page.read()
            try:
                page = page.decode('utf-8')
            except:
                page = page.decode('gbk')
            return page
        except Exception as e:
            print('page error')
            return 'error'
    
    def _getnovelname(self):
        try:
            self.NovelName = re.compile('<h1>(.*?)</h1>').findall(self._novel_home_page)[0].split(' ')[0]
        except:
            pass
    
    def getlist(self):
        self._getnovelname()
        try:
            
            temp = re.compile(self.chpater_regular).findall(self._novel_home_page, re.S)
            for each in temp:
                self.chpaters.append(each[1])
                self.chpater_link.append(each[0])
            self.NovelLength = len(self.chpaters)
            print('link got')
        
        
        except Exception as e:
            print('link error', e)
            return 'error'
    
    def save_chpaters(self):
        with open(self.NovelName + r'.novel', 'w+', encoding='utf-8') as chp_f:
            for each in range(self.NovelLength):
                chp_f.write(self.url + self.chpater_link[each] + '\t' + self.chpaters[each] + '\n')
                chp_f.flush()
    
    def SaveNovel(self):
        for index in range(self.NovelLength):

            try:
                html = self._getpage(self.url + self.chpater_link[index])
                if html != 'error':
                    
                    
                    content = re.findall(self.content_regular, html, re.S | re.M)
                    
                    reg = re.compile(r'(\s)|(<br/>)|(&\w\w\w\w;)|(&\w\w;)')
                    content = re.sub(reg, '<br>', content[0])
     
                    reg = re.compile(r'((?:<br>){2,}|(?:<br/>){2,}|(?:\t){2,})')
                    content = reg.sub('\n\n', content)
                    
                    lst = content.split('\n\n')
                    for i in range(3):
                        if 'type=' in lst[-1]:
                            lst.pop()
                    with open(self.NovelName + '.txt', 'a+', encoding='utf8') as fl:
                        fl.write('\n\n\n\n\n' + str(self.chpaters[index]) + '\n\n')
                        print(self.chpaters[index])
                        for item in lst:
                            if item not in ' \t\n':
                                fl.write('    ' + item + '\n')
                        fl.flush()
                else:
                    with open(self.NovelName + '.txt', 'a+', encoding='utf8') as fl:
                        fl.write('\n' + 'error' + str(eachlink))
            except Exception as e:
                print('text error', e)


'''

novel_home_page = getpage('http://www.23us.cc/html/87/87195/')
chpaters = getlist(novel_home_page)
novalname = getnovelname(novel_home_page)
save_chpaters(novalname, chpaters)nn

for link in chpaters:
    gettext(link)

fl.close()
'''

if __name__ == '__main__':
    # 走进修仙
    nurl = 'http://www.23us.cc/html/87/87195/'
    
    n = Novel(nurl)
    n.getlist()
    n.save_chpaters()
    n.SaveNovel()
