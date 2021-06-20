from django.urls import path
from . import views

urlpatterns = [
    path('account/subscribers/', views.subscribers),
]
