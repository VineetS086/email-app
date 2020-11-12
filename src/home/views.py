from django.shortcuts import (
    redirect, render, get_object_or_404 )
from django.http import (HttpResponse, )
from django.contrib import messages

#User and login imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import User_Key
from .forms import CreateUserForm, LoginUserForm

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
    form = LoginUserForm()
    context = {
        'form'  : form
        }
    if request.method == "POST":
        form = LoginUserForm(request, request.POST)
        if form.is_valid():
            username_   = request.POST.get('username')
            password_   = request.POST.get('password')
            user = authenticate(username = username_, password = password_)
        
            if user is not None:
                login(request, user)
                #return HttpResponse('<h1>Hello World</h1><h1>Email Page Redirect</h1>')
                messages.success(request, 'Login Sucessful')
                return redirect('Home:Home')
            
        else:
            context['message'] = 'Invalid username/password'
    #update_history(request)'''
    context = {
        'form'  : form
    }
    return render(request, 'home/login.html', context)


#SignUp
def signup_view(request):           #SignUp
    #update_history(request)
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            create_user_(form)
            return HttpResponse("User Saved")

    context = {
        'form'  : form,

    }
    return render(request, 'home/signup.html', context)

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
        return HttpResponse(f'<h1>You Are Activated...</h1>')

    else:
        return HttpResponse(f'<h1>Activativation Failed</h1>')
    
