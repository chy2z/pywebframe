from django.http import HttpResponse
from django.shortcuts import render

def info(request):
    return HttpResponse("info");

def error(request):
    return HttpResponse("error");