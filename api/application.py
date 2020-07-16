 # -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import *
from api.lib.utils import returnResponse
import json
from urllib.request import quote, unquote
from django.contrib.auth.decorators import login_required

@login_required
def application(request):
    method = request.method
    if method == 'POST':
        app_name = request.POST.get('app_name')
        app_url = request.POST.get('app_url')
        app_event = request.POST.get('app_event')

        fileds={
            'name': app_name,
            'url': app_url,
            'event': app_event
        }
        try:
            result = AppType.objects.update_or_create(defaults=fields,id=aid)
        except ValueError:
            result = AppType.objects.update_or_create(defaults=fields,id=None)
        except Exception as e:
            return returnResponse(1001,'error',str(e))
        return returnResponse(1000,'success',result.id)
    