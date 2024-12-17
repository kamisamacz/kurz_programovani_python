from django.shortcuts import render
from django.http import HttpResponse

def data(request):
    return HttpResponse("Hello world!")