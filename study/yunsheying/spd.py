import requests
import logging
logging.basicConfig(level=logging.DEBUG)


def save(url):
    r = requests.get(url, timeout=5)
    if r.status_code ==200:
        logging.debug('content get')
        fname=url.split(r'/')[-1]
		''' <img src="/statics/js/uploadeditor/php/../attached/image/20171114/20171114154735_97593.jpg" alt="">
		'''
		
		
        with open(fname+'.jpg', 'wb') as fi:
            fi.write(r.content)
            logging.info('')
        return fname
    else:
        return ' '




urls = ['http://yunidphoto.com/index.php/Repeat/info/id/{}'.format(i) for i in range(100,200)]



for url in urls:
    logging.info('get...'+url)
    save(url)
