from django.contrib.auth.models import User
from django.shortcuts import (redirect, )
from django.urls import resolve

from .models import History

def create_user_(request):

    user = User(
        username    = request.POST.get('username'),
        first_name  = request.POST.get('first_name'),
        last_name   = request.POST.get('last_name'),
        email       = request.POST.get('email'),
        password    = request.POST.get('password'),  
    )
        
    user.save()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return f'" {ip} "'



def update_history(request, action='Page Visit'):
    user_   = request.user if request.user.is_authenticated else None
    
    his = History(
        user        = user_,
        page        = resolve(request.path_info).url_name,
        action      = action,
        email_from  = request.POST.get('email_from'),
        email_to    = request.POST.get('email_to'),
        ip          = get_client_ip(request),
    )
    his.save()

