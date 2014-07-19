from django.conf.urls import patterns, include, url
from kenix.apps.home import views as home_views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('kenix.apps.home.views',
                       url(r'^$', home_views.HomeView.as_view(), name='index'),
)