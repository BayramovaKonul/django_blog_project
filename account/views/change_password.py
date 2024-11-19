
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


@login_required(login_url='login')
def change_password(request):
    form  = PasswordChangeForm(request.user, request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user=form.save()
        update_session_auth_hash(request, user)
    return render(request, 'change-password.html', context={
         'form': form
    })



