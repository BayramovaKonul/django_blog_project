
from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import CustomUserModel
from ..forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.translation import gettext as _


def register(request):
    form  = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    

    return render(request, 'register.html', context={
         'form': form
    })



