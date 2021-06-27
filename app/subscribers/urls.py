from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:pk>/subscribers/',
         views.get_subscribers, name="get_subscribers"),
]
