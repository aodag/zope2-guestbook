from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from . import app


def addGuestbook(context, id, title):
    """ add new guestbook """
    guestbook = app.Guestbook(id)
    guestbook.title = title
    context._setObject(id, guestbook)
    return "OK"

manage_addGuestbookForm = PageTemplateFile('manage_addGuestbook', globals())

def initialize(registrar):
    registrar.registerClass(
        app.Guestbook,
        constructors=(manage_addGuestbookForm,
                      addGuestbook))
