from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.get_accounts, name="get_accounts"),
    path('accounts/<str:pk>/', views.get_account, name="get_account"),
    path('accounts/<str:pk>/edit/', views.edit_account,
         name="edit_account"),
    path('accounts/<str:pk>/delete/', views.delete_account, name="delete_account"),
    path('accounts/create', views.create_account, name="create_account"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
]
