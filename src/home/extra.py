from django.contrib.auth.models import User
from django.shortcuts import (redirect, )
from django.urls import resolve

from .models import History, User_Key

def create_user_(form):

    form.save()
    #print(form.cleaned_data)
    user = User.objects.get(username=form.cleaned_data['username'])
    User_Key.objects.create(user=user)
    user.user_key.activate(False)
 
# key = user.user_key.key 

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

