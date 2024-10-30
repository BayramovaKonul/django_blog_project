
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def user_info(request, id):
    return HttpResponse(f'<h1>The information of the user {id} </h1>')

def user_pic(request, username):
    return HttpResponse(f'<h1>The pictures of the user {username} </h1>')