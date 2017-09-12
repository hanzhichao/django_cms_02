# coding=utf-8
from django.conf.urls import patterns, url
from cms.views import home, category, article, search


urlpatterns = [
    url(r'^$', home, name='cms-home'),
    url(r'^category/(?P<slug>[-\w]+)/$', category, name='cms-category'),
    url(r'^article/(?P<slug>[-\w]+)/$', article, name='cms-article'),
    url(r'^search/$', search, name="cms-search"),
]
