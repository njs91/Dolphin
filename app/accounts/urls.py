from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.get_accounts, name="get_accounts"),
    path('account/<str:pk>/', views.get_account, name="get_account"),
    path('account/<str:pk>/edit/', views.edit_account,
         name="edit_account"),
    path('account/<str:pk>/delete/', views.delete_account, name="delete_account"),
    path('account/create', views.create_account, name="create_account")
]
