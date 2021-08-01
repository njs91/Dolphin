from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/<str:pk>/messages/create',
         views.message_create, name="message_create"),
    path('accounts/<str:pk>/messages/<str:message_id>',
         views.message_view, name="message_view")
]
