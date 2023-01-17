import tornado.web

class IndexPage(tornado.web.RequestHandler):
    def get(self):
        self.write("Tornado Warning!")