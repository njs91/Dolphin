from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:pk>/subscribers/',
         views.get_subscribers, name="get_subscribers"),
    path('account/<str:pk>/subscribers/<str:sub_id>',
         views.get_subscriber, name="get_subscriber"),
]
