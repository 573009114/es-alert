"""alert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
"""

from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
import error_pages.views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView 

from . import index
from api import contacts

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('openapi/', include('api.urls')),
]

urlpatterns += [
    path('', index.home,name='home'),
    path('contacts/',index.contacts_list,name='contacts'),
    path('group/',index.group_list,name='group'),
    path('rules/',index.rules_list,name='rules'),
    path('rules/index',index.rules_index,name='index'),
    # path('users/',index.users_list,name='users'),
]
# urlpatterns += [
#     path('', index.home, name='home'),
#     path('alert/rules', index.alert_config, name='alert'),
#     path('alert/rules/view', index.alert_view, name='alert_view'),
#     path('alert/rules/edit', index.alert_edit, name='alert_edit'),
#     path('alert/rules/del', index.alert_del, name='alert_delete'),
#     path('alert/rules/create', index.alert_create, name='alert_create'),

#     path('alert/group', index.group_view, name='group_view'),
#     path('alert/group/edit', index.group_edit, name='group_edit'),
#     path('alert/group/create', index.group_create, name='group_create'),
#     path('alert/group/del', index.group_del, name='group_del'),

#     path('access/', index.auth_config, name='access'),
#     path('system/', index.sys_config, name='system'),
# ]

urlpatterns += [
    path('account/',include('account.urls'))
]

handler404 = error_pages.views.error_404
handler403 = error_pages.views.error_403
handler401 = error_pages.views.error_401
handler500 = error_pages.views.error_500

