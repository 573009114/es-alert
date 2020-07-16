from django.http import HttpResponse,JsonResponse

def returnResponse(code,msg,extra):
    '''
    定义接口返回json格式
    '''
    data=dict()
    data['code'] = code
    data['msg'] = msg
    data['extra']=extra
    return JsonResponse(data)

