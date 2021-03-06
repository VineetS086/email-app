from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from.forms import EmailForm
from .email_sender import send_mail_

def index(request):
    form = EmailForm()
    if request.user.is_anonymous:
        return redirect('Home:Home')

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            #send mail
            
            #print(form.cleaned_data)
            send_mail_(form.cleaned_data)
            #print("Mail Sent")
            return redirect("Home:Home")


    context = {
        'form' : form,
    }
    return render(request, 'email_sender/textarea.html', context)