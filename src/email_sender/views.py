from django.shortcuts import (redirect, render,  )
from django.http import (HttpResponse, )

#User and login imports
from django.contrib.auth import authenticate, login, logout

#created module
from .extra import (
    create_user_,
    update_history,
)

def home_view(request):             #
    update_history(request)
    return HttpResponse(f'<h1>Hello, World!</h1>Home <p>welcome {request.user}</p>')
    

#Login and Logout
def login_view(request):            #Login
    update_history(request)

    if request.method == "POST":
        username_   = request.POST.get('username')
        password_   = request.POST.get('password')

        user = authenticate(username = username_, password = password_)
        
        if user is not None:
            login(request, user)
            return redirect('../')
            

        else:
            pass
            # Warning/ReCheck Message
    
    return HttpResponse('<h1>Hello, World!</h1>Login')


#SignUp
def signup_view(request):           #SignUp
    update_history(request)

    if request.method == "POST":
        pass

    return HttpResponse('<h1>Hello, World!</h1>Signup')


def email_sender_view(request):     #POST Request Form
    update_history(request)
    return HttpResponse('<h1>Hello, World!</h1>email_sender')


##Anish
