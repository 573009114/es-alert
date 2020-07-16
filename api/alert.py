 # -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from api.models import *
from api.lib.utils import returnResponse
import json
import time

@login_required
def alert_index(request):
    '''
    报警规则
    '''
    method = request.method
    if method == 'POST':
        prefix = request.POST.get('es_index_prefix')
        es_query=request.POST.get('es_query')
        log_count=request.POST.get('log_count')
        in_minutes=request.POST.get('in_minutes')
        trigger=request.POST.get('trigger')
        product=request.POST.get('product')
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        no_deal=request.POST.get('no_deal')
        owner=request.POST.get('owner')
        create_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) 
        aid = request.POST.get('rule_id')
        data = dict()

        fields = {
            'es_index_prefix': prefix,
            'es_query': es_query,
            'log_count': log_count,
            'in_minutes': in_minutes,
            'trigger': trigger,
            'product': product,
            'name': name,
            'priority': priority,
            'no_deal': no_deal,
            'owner': owner,
            'create_time': create_time
        }
        try:
            result = EsAlertRules.objects.update_or_create(defaults=fields,id=aid)
        except ValueError:
            result = EsAlertRules.objects.update_or_create(defaults=fields,id=None)
        except Exception as e:
            return returnResponse(1001,'error',str(e))
         
        return returnResponse(1000,'success','更新成功')

    elif method == 'DELETE':
        aid =request.body.decode().split('=')[1]
        print(aid)
        data = dict()
        try:
            result = EsAlertRules.objects.filter(id=aid).delete()
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return returnResponse(1000,'success',result)
    else:
        aid=request.GET.get('id')
        data=dict()
        try:
            result = EsAlertRules.objects.filter(id=aid).values('id','es_index_prefix',
                'es_query','log_count','in_minutes','trigger','product','name',
                'priority','no_deal','owner','create_time')
            for r in result:
                result = r
            res = dict()
            res['id'] = result['id']
            res['es_index_prefix'] = result['es_index_prefix']
            res['es_query'] = result['es_query']
            res['log_count'] = result['log_count']
            res['in_minutes'] = result['in_minutes']
            res['product'] = result['product']
            res['name'] = result['name']
            res['priority'] = result['priority']
            res['no_deal'] = result['no_deal']
            res['trigger'] = result['trigger']
            res['owner'] = result['owner']
            data['code'] = 1000
            data['msg'] = 'success'
            data['extra'] = res
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return JsonResponse(data) 