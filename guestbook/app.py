from datetime import datetime
from babel.dates import format_datetime
from persistent.list import PersistentList
from markupsafe import escape
from five import grok


class Guestbook(grok.Model):
    meta_type = "guestbook"

    def __init__(self, id):
        super(Guestbook, self).__init__(id)
        self.comments = PersistentList()

    def add_comment(self, name, comment):
        self.comments.append(dict(name=name.decode('utf-8'),
                                  comment=comment.decode('utf-8'),
                                  created_at=datetime.now()))

class Index(grok.View):
    def format_datetime(self, dt):
        return format_datetime(dt, format="full", locale="ja")

    def nl2br(self, s):
        return unicode(escape(s)).replace('\n', '<br />')

class Post(grok.View):
    def update(self, name, comment):
        self.context.add_comment(name, comment)

    def render(self):
        return self.redirect(self.url(self.context))
