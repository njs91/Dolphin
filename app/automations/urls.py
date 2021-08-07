from django.urls import path
from . import views

urlpatterns = [
    path('accounts/<str:pk>/automations',
         views.automation_list, name="automation_list"),
    path('accounts/<str:pk>/automations/create',
         views.automation_create, name="automation_create"),
    path('accounts/<str:pk>/automations/<str:automation_id>',
         views.automation_view, name="automation_view"),
    path('accounts/<str:pk>/automations/<str:automation_id>/edit',
         views.automation_edit, name="automation_edit"),
    path('accounts/<str:pk>/automations/<str:automation_id>/delete',
         views.automation_delete, name="automation_delete"),
    path('accounts/<str:pk>/automations/<str:automation_id>/add_message',
         views.automation_add_message, name="automation_add_message"),
]
