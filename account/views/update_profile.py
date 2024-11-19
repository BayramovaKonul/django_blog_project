from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from ..forms import UpdateProfileForm
from django.contrib import messages

@login_required(login_url='/login')
def update_profile(request):
    form  = UpdateProfileForm(request.POST or None, request.FILES or None,
                             instance=request.user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('home')
    
    return render(request, 'update_profile.html', context={
         'form': form
    })