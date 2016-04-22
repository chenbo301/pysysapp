# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^blogs/', include('blogs.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
