
from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import CustomUserModel
from ..forms.login import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views import View

# Create your views here.

# def user_login(request):
#     form = LoginForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username = username, password=password)
#             if user is None:
#                 messages.info(request, _("Username or Password is incorrect"))
#                 return redirect("login")
#             login(request, user)
#             messages.success(request, _("Welcome to the website"))
#             return redirect("home")
            
#     return render(request, 'login.html', context={
#         'form' : form
#     })

class LoginView(View):
    http_method_names = ['get', 'post']
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'login.html', context={
        'form' : form
    })

    def post(self, request):
        form= self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password=password)
            if user is None:
                messages.info(request, _("Username or Password is incorrect"))
                return redirect("login")
            login(request, user)
            messages.success(request, _("Welcome to the website"))
            return redirect("home")

