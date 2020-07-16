from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from api import contacts,alert,data_source

# from api.applications.index import *

# 联系人路由
urlpatterns = [
    path('contacts/create', contacts.alert_contacts_create,name='create'),
    path('contacts/delete', contacts.alert_contacts_delete,name='delete'),
    path('contacts/update', contacts.alert_contacts_update,name='update'),
    path('contacts/select', contacts.alert_contacts_select,name='select'),
    path('contacts/', contacts.alert_contacts_list,name='contacts'),
] 

# 告警组路由
urlpatterns += [
    path('group/', contacts.alert_group,name='group'),
] 

# 告警规则路由
urlpatterns += [
    path('alert',alert.alert_index,name='alerts'),
]
