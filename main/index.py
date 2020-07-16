import time

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from api.alert import *
from api.contacts import *
from api.data_source import *
from api.lib.utils import returnResponse
from django.template import RequestContext
from django.db.models import Count
from django.db.models import Sum  # 引入


@login_required
def home(request):
    rules_total=EsAlertRules.objects.aggregate(Count('id'))
    alert_users=EsAlertMembers.objects.aggregate(Count('id'))
    alert_group=EsAlertGroups.objects.values('group_name').distinct().count()
    rules=EsAlertRules.objects.all().values('id','es_index_prefix',
                'es_query','log_count','in_minutes','trigger','product','name',
                'priority','no_deal','owner','create_time')[0:5]
    users=EsAlertMembers.objects.all().values('name','tel','email')[0:4]

    data=dict()
    res = dict()
    res['rules_total'] = rules_total
    res['alert_users'] = alert_users
    res['alert_group'] = alert_group
    res['rules'] = rules
    res['users'] = users
    data['code'] = 1000
    data['msg'] = 'success'
    data['extra'] = res
    return render(request,'backend_v1.0/index.html',{'response':data})

@login_required
def contacts_list(request):
    '''
    获取联系人列表
    '''
    if request.method == 'GET':
        data=dict()
        try:
            result=EsAlertMembers.objects.all().values('id','name','tel','email')
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = result
        except Exception as e:
            data['code'] = 1001
            data['msg'] = 'error'
            data['extra'] = str(e)
        return render(request,'backend_v1.0/contacts-list.html',{'response':data})

@login_required
def group_list(request):
    '''
    获取报警组列表
    '''
    if request.method == 'GET':
        data=dict()
        try:
            # group = EsAlertGroups.objects.all().values('id','member__name','group_name')
            group=EsAlertGroups.objects.raw("SELECT a.id,a.group_name, GROUP_CONCAT(b.`name` SEPARATOR '|')  member_name FROM es_alert_group  as a LEFT JOIN es_alert_members as b ON a.member_id = b.id GROUP BY a.`group_name`;")
            members = EsAlertMembers.objects.all().values('id','name')
            res = dict()
            format_data=list()
            for i in group:
                res={
                    'group':[
                        {
                            'id':i.id,
                            'name':i.group_name,
                            'members':i.member_name,
                        }
                    ]
                }
                format_data.append(res)
            
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = format_data

        except Exception as e:
            data['code'] = 1001
            data['msg'] = 'error'
            data['extra'] = str(e)
        return render(request,'backend_v1.0/group-list.html',{'response':data,'members':members})

@login_required
def rules_list(request):
    '''
    告警规则
    '''
    method = request.method
    if method == 'GET':
        response=EsAlertRules.objects.all().values('id','es_index_prefix',
                'es_query','log_count','in_minutes','trigger','product','name',
                'priority','no_deal','owner','create_time')
        return render(request,'backend_v1.0/rules-list.html',{'response':response})

@login_required
def rules_index(request):
    '''
    告警规则
    '''
    return render(request,'backend_v1.0/rules-index.html')  
