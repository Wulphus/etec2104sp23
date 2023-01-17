import asyncio
import tornado.web
import time
import Quote
import os
import os.path
import Index, Quote, TemplateTest


HTMLDIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..","html"
    )
)
#Fooooo

class IndexPage(tornado.web.RequestHandler):
    def get(self):
        self.write(time.strftime("%B %d %A %I:%M %p"))
       


class AboutPage(tornado.web.RequestHandler):
    def get(self):
        self.write("About my life!")

def makeApp():
    endpoints = [
        ("/",IndexPage),
        ("/quote", Quote.Handler),
        ("/fancy",TemplateTest.Handler)     #new

    ]
    app = tornado.web.Application(endpoints,
        static_path=HTMLDIR
    )
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()
