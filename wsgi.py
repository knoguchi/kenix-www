from google.appengine.ext import ndb
import django.core.handlers.wsgi

application = ndb.toplevel(django.core.handlers.wsgi.WSGIHandler())
