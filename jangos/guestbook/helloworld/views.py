from django.shortcuts import render
from django.http import HttpResponse

def index(rqeuest):
    return HttpResponse("<h1>hello</h1>")
