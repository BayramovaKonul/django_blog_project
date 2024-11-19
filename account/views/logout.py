
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout


# Create your views here.

def user_logout(request):
    logout(request)
    return redirect("login")
    # reuqest.COOKIES - to get cookies
