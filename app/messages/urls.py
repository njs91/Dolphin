from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/<str:pk>/messages/create',
         views.message_create, name="message_create")
]
