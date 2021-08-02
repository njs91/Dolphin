from django.contrib import admin
from messages import models


@admin.register(models.Message)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ("name", "account", "date_created")
