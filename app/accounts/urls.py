from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts', views.get_accounts, name="get_accounts"),
    path('accounts/<str:pk>/', views.get_account, name="get_account"),
    path('accounts/<str:pk>/edit/', views.edit_account,
         name="edit_account"),
    path('accounts/<str:pk>/delete/', views.delete_account, name="delete_account"),
    path('accounts/create', views.create_account, name="create_account"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password_confirm.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_complete.html"),
         name="password_reset_complete"),
]
