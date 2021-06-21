from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:id>/', views.account, name="account"),
    path('account/edit/', views.edit_account, name="edit_account"),
]
