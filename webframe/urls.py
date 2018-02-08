"""
webframe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录
"""
# from django.contrib import admin
# from django.urls import path
from django.conf.urls import include, url
from . import view
from webframe.views import versionview

# 2级 路由
paths_patterns = [
    url(r'^paths/(?P<name>[\s\S]*)/(?P<age>[0-9]{1,3})/$', view.paths1),
    url(r'^paths/(?P<name>[\s\S]*)/(?P<age>[0-9]{1,3})/(?P<sex>[\s\S]{1})/$', view.paths2),
    url(r'^paths/(?P<name>[\s\S]*)/$', view.paths3, {'age': '33'}),
]

# 2级 路由
version_patterns = [
    url(r'^info',versionview.info),
    url(r'^error', versionview.error),
]

# 1级 路由
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^index1', view.index1),
    url(r'^index2', view.index2),
    url(r'^views$', view.test),
    url(r'^paths/(?P<name>[\s\S]*)/(?P<age>[0-9]{1,3})/$',view.paths1),
    url(r'^paths/(?P<name>[\s\S]*)/(?P<age>[0-9]{1,3})/(?P<sex>[\s\S]{1})/$',view.paths2),
    url(r'^paths/(?P<name>[\s\S]*)/$',view.paths3,{'age': '33'}),
    url(r'^path/', include(paths_patterns)),
    url(r'^version/', include(version_patterns)),
]
