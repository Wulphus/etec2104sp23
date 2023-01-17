import tornado.web
import random

quotes = [
    "The only thing we have to fear is fear itself.",
    "Fourscore and seven years ago...",
    "We the People of the United States...",
    "Your quote here...",
    "Weeeeeeeeeeeeeee"
]
class Handler(tornado.web.RequestHandler):
    def get(self):
        q = random.choice(quotes)
        self.write(
            f'<img src="/static/quotationmarks.png"><br>{q}'
        )