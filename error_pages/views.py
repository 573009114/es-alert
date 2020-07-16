from django.shortcuts import render

# Create your views here.

def error_404(request,exception):
    """
    404提示页
    """
    return render(request, 'error/404.html')


def error_500(request):
    """
    500提示页
    """
    return render(request, 'error/500.html')


def error_401(request,exception):
    """
    401提示页
    """
    return render(request, 'error/401.html')


def error_403(request,exception):
    """
    403提示页
    """
    return render(request, 'error/403.html')
