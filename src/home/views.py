from django.shortcuts import (
    redirect, render, get_object_or_404 )
from django.http import (HttpResponse, )

#User and login imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import User_Key
#created module
from .extra import (
    create_user_,
    update_history,
)

def home_view(request):             #
    context = {
        
    }
    if request.user.is_authenticated:
        pass#return HttpResponse('<h1>Hello World</h1><h1>Email not found</h1>')

    #update_history(request)
    return render(request, 'home/index.html', context)
    

#Login and Logout
def login_view(request):            #Login
    context = {
        
    }

    if request.method == "POST":
        username_   = request.POST.get('username')
        password_   = request.POST.get('password')

        print(username_,password_)
        user = authenticate(username = username_, password = password_)
        
        if user is not None:
            login(request, user)
            return HttpResponse('<h1>Hello World</h1><h1>Email Page Redirect</h1>')
            
        else:
            context['message'] = 'Invalid username/password'
    #update_history(request)        
    return render(request, 'home/login.html')


#SignUp
def signup_view(request):           #SignUp
    #update_history(request)

    if request.method == "POST":
        pass

    #update_history(request)
    return HttpResponse('<h1>Hello, World!</h1>Signup')

def logout_view(request):           #Logout
    #update_history(request)
    logout(request)
    return redirect('Home:Home')


def activation_view(request, user_, key_):
    user    = get_object_or_404(User, username=user_)
    if user.is_active:
        return HttpResponse(f'<h1>You Are Already Activated...</h1>')
    
    if user.user_key.key == key_:
        user.user_key.activate()
        user.save()
        return HttpResponse(f'<h1>You Are Activated...</h1>')

    else:
        return HttpResponse(f'<h1>Activativation Failed</h1>')
    
