from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from account import index

# from api.applications.index import *

urlpatterns = [
    path('login', index.login,name='login'),
    path('logout', index.logout,name='logout'),
    path('modify', index.modify_passwd,name='modify'),
] 