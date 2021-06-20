from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account),
    path('account/edit/', views.edit_account),
    path('account/subscribers/', views.subscribers),
]
