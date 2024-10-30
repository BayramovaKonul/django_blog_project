from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>/', views.user_info),   # I wrote int:id, otherwise it will take id as string, then we need to make conversion each time we need id.
    path('<username>/', views.user_pic),
]
# I wrote id inside <> to take id as a variable, not a part of URL.