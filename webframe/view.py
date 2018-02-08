from django.http import HttpResponse
from django.shortcuts import render

"""
首页
"""


def index1(request):
    context = {}
    context['hello'] = 'Hello World 1!'
    return render(request, 'app-1/index.html', context);


def index2(request):
    context = {}
    context['hello'] = 'Hello World 2!'
    return render(request, 'app-2/index.html', context);

'''
测试
'''


def test(request):
    return HttpResponse("views");


"""
参数
"""

def paths1(request,name,age):
    context = {}
    context['id'] = 'paths1'
    context['name'] = name
    context['age']=age
    return render(request, 'app-1/paths.html', context);


def paths2(request,name,age,sex):
    context = {}
    context['id'] = 'paths2'
    context['name'] = name
    context['age']=age
    context['sex'] = sex
    return render(request, 'app-1/paths.html', context);

def paths3(request,name,age):
    context = {}
    context['id'] = 'paths3'
    context['name'] = name
    context['age']=age
    return render(request, 'app-1/paths.html', context);