from django.http import HttpResponse

def index(req):
    return HttpResponse('<h1>hello world,welcome to django</h1>')