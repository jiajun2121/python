from tornado import web, httpserver, ioloop


class HomeHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        print('有人访问Home page')
        self.write(r"你好，我是XXX (๑•ั็ω•็ั๑)")


class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        print('有人访问Login page')
        self.write('login page')
        # self.render('Wopop.html')

class VideoHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        print('有人访问Video page')
        self.write('video page' + '\n\n\n')
        self.render('video.html')


setting = {
    'template_path': 'template'
}

application = web.Application([
    (r"/", HomeHandler),
    (r"/login", LoginHandler),
    (r"/video", VideoHandler),
])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    print("http://127.0.0.1:8080")
    ioloop.IOLoop.current().start()
