# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'blogs'
urlpatterns = {
    url(r'^$', views.index, name='home'),
    url(r'^article/$', views.article, name='article'),
}
