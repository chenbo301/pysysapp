# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    return render(request, 'home.html', request)


def article(request):
    return render(request, 'article.html', request)
