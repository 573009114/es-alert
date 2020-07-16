from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import *

# Create your views here.
def system_setting_create(request):
    if request.method == 'POST':
        webname = request.POST.get('webname')
        email = request.POST.get('email')
        data=dict()
        try:
            result=SystemSetting.objects.create(website_name=name,email=app_source)
            result.save
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = result
        except Exception as e:
            data['code'] = 1001
            data['msg'] = 'error'
            data['extra'] = e
        return HttpResponse(data)

def system_setting_update(request):
    if request.method == 'POST':
        webname = request.POST.get('webname')
        email = request.POST.get('email')
        sid = request.POST.get('id')
        data=dict()
        try:
            result=SystemSetting.objects.filter(id=sid).update(website_name=name,email=app_source)
            result.save
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = result
        except Exception as e:
            data['code'] = 1001
            data['msg'] = 'error'
            data['extra'] = e
        return HttpResponse(data)