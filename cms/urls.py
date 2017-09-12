# coding=utf-8
from django.conf.urls import patterns, url, include
from django.contrib import admin
from cms.views import home, category, article, search, test


urlpatterns = [
    url(r'^$', home, name='cms-home'),
    url(r'^category/(?P<slug>[-\w]+)/$', category, name='cms-category'),
    url(r'^article/(?P<slug>[-\w]+)/$', article, name='cms-article'),
    url(r'^search/$', search, name="cms-search"),
    url(r'^(?P<slug>[-\w]+)/(?P<slug2>[-\w]+)/$', test),
]


