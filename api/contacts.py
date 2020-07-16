 # -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from api.models import *
from api.lib.utils import returnResponse
import json
from urllib.request import quote, unquote


# Create your views here.

@login_required
def alert_contacts_create(request):
    '''
    创建联系人信息接口
    '''
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('telphone')
        email = request.POST.get('email')
        data=dict()
        try:
            result=EsAlertMembers.objects.create(name=name,tel=tel,email=email)
            result.save
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return returnResponse(1000,'success',result.id)
@login_required
def alert_contacts_list(request):
    '''
    获取联系人列表接口
    '''
    if request.method == 'GET':
        data=dict()
        try:
            result=EsAlertMembers.objects.all().values('id','name','tel','email')
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return returnResponse(1000,'success',result)
@login_required
def alert_contacts_delete(request):
    '''
    删除联系人接口
    '''
    if request.method == 'POST':
        id = request.POST.get('id')
        data=dict()
        try:
            result=EsAlertMembers.objects.filter(id=id).delete()
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return returnResponse(1000,'success',result)
@login_required
def alert_contacts_select(request):
    '''
    查找某个联系人接口
    '''
    if request.method == 'GET':
        id = request.GET.get('id')
        data=dict()
        try:
            result=EsAlertMembers.objects.get(id=id)
            res = dict()
            res['id'] = result.id
            res['name'] = result.name
            res['tel'] = result.tel
            res['email'] = result.email
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = res      
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        print(data)
        return JsonResponse(data)

@login_required
def alert_contacts_update(request):
    '''
    更新联系人信息接口
    '''
    if request.method == 'POST':
        id = request.POST.get('user_id')
        name = request.POST.get('name')
        tel = request.POST.get('telphone')
        email = request.POST.get('email')

        data=dict()
        try:
            result=EsAlertMembers.objects.filter(id=id).update(name=name,tel=tel,email=email)
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return returnResponse(1000,'success',result)

#####

@login_required
def alert_group(request):
    '''
    报警组创建接口
    '''
    method = request.method
    data=dict() 
    if method == 'POST':
        try:
            group_name=request.POST.get('name')
            usersid=request.POST.getlist('member_id')
            for uid in usersid:
                result=EsAlertGroups.objects.create(group_name=group_name,member_id=uid)
                result.save()
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return returnResponse(1000,'success',result.id)

    elif method == "DELETE":
        '''
        删除报警组成员关联记录
        '''
        req = request.body.decode().split('=')[1]
        name = unquote(req, encoding='utf-8')
        try:
            result=EsAlertGroups.objects.filter(group_name=name).delete()
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return returnResponse(1000,'success',result)
    else:
        id = request.GET.get('id')
        data=dict()
        try:
            result = EsAlertGroups.objects.filter(id=id).values('id','member__name','group_name','member_id') 
            for i in result:
                result = i
            res = dict()
            res['group_id'] = result['id']
            res['group_name'] = result['group_name']
            res['member_id'] = result['member_id']
            res['member_name'] = result['member__name']
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = res
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return JsonResponse(data) 