from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:pk>/', views.get_account, name="get_account"),
    path('account/<str:pk>/edit/', views.edit_account, name="edit_account"),
]
