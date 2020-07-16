from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import *

# Create your views here.

def data_source_create(request):
    '''
    创建数据源
    '''
    if request.method == 'POST':
        name = request.POST.get('app_name')
        app_source = request.POST.get('app_source')
        data=dict()
      
        try:
            result=DataSource.objects.create(app_name=name,app_source=app_source)
            result.save
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = result
        except Exception as e:
            data['code'] = 1001
            data['msg'] = 'error'
            data['extra'] = e
        return HttpResponse(data)

def data_source_update(request):
    '''
    更新数据源
    '''
    if request.method == 'POST':
        app_id = request.POST.get('id')
        app_source = request.POST.get('app_source')
        name = request.POST.get('app_name')
        data=dict()
        try:
            result=DataSource.objects.filter(app_id=app_id).update(app_name=name,app_source=app_source)
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = result
        except Exception as e:
            data['code'] = 1001
            data['msg'] = 'error'
            data['extra'] = e
        return JsonResponse(data)

def data_source_delete(request):
    '''
    删除数据源
    '''
    if request.method == 'POST':
        app_id = request.POST.get('id')
        data=dict()
        try:
            result=DataSource.objects.filter(app_id=app_id).delete()
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = result
        except Exception as e:
            data['code'] = 1001
            data['msg'] = 'error'
            data['extra'] = e
        return JsonResponse(data)

def data_source_select(request):
    '''
    获取所有数据源
    '''
    if request.method == 'GET':
        data=dict()
        try:
            result=DataSource.objects.all().values('app_name','app_source','app_id')
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = result
        except Exception as e:
            data['code'] = 1001
            data['msg'] = 'error'
            data['extra'] = e
        return HttpResponse(data)
