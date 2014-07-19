from google.appengine.ext import ndb
import django.core.handlers.wsgi

app = ndb.toplevel(django.core.handlers.wsgi.WSGIHandler())
