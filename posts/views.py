from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def posts(request):
    return HttpResponse('<h1>Post List</h1>')
