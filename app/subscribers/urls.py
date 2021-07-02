from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:pk>/subscribers/',
         views.get_subscribers, name="get_subscribers"),
    path('account/<str:pk>/subscribers/<str:sub_id>',
         views.get_subscriber, name="get_subscriber"),
    path('account/<str:pk>/subscribers/<str:sub_id>/edit',
         views.edit_subscriber, name="edit_subscriber"),
    path('account/<str:pk>/subscribers/<str:sub_id>/delete',
         views.delete_subscriber, name="delete_subscriber"),
]
