# -*- coding: utf-8 -*-
from django.db import models


class Article(models.Model):
    def __init__(self):
        return self.pub_title

    pub_title = models.CharField(max_length=200)
    pub_author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    pub_content = models.TextField()
