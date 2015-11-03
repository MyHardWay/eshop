'''
Created on 27 июля 2015 г.

@author: way
'''
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registrate/$', views.registrate_ajax, name='registrate_ajax'),
    ]