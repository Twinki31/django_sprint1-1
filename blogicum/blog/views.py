from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    return render(request, 'blog/index.html')
