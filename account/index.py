from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect('/')
        else:
            return render(request,'backend_v1.0/login.html',{"msg":"用户名不存在，或者密码错误！"})
    else:
        form = AuthenticationForm(request)

    kwargs = {
        'form': form,
    }
    return render(request, 'backend_v1.0/login.html', kwargs)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/account/login')

@login_required
def modify_passwd(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        old_password=request.POST.get('oldpassword')
        new_password1=request.POST.get('newpassword')
        repeat_password=request.POST.get('repeatpassword')
        response={}
        if repeat_password != new_password1:
            response['data']='您的确认密码和新密码不匹配'
        else: 
            new_password=new_password1
            if len(new_password)>8:
                user = auth.authenticate(username=username, password=old_password)
                if user is not None and user.is_active:
                    user.set_password(new_password)
                    user.save()
                    response['data']='密码修改成功'
                else:
                    response['data']='原密码错误'
            else:
                response['data']='密码长度不能小于8位或不能为空'
        return render(request,'backend_v1.0/change-passwd.html',{'msg':response['data']})
    else:
        return render(request,'backend_v1.0/change-passwd.html')
