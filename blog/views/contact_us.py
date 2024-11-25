from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import ArticleModel, CategoryModel, CommentModel, ContactUsModel
from django.contrib import messages
from django.views import View
from account.models import CustomUserModel
from ..forms.contact_us import ContactUsForm
from django.db.models import Q, Count

def contact_us (request):
    form = ContactUsForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.stage  = ContactUsModel.StageChoices.NEW
            form_obj.assigned_to = (CustomUserModel.objects.filter(is_staff=True).annotate(message_count=Count('assigned__id')).order_by('message_count').first()) # here 'assigned' is a related name
            form_obj.save()
            return redirect('home')

    return render(request, 'contact.html', context = {
        'form' : form
    })