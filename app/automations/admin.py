from django.contrib import admin
from automations import models


@admin.register(models.Automation)
class AutomationAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "account", "date_created")
    fields = ("name", "description", "account")  # @todo: add messages
    list_filter = ('date_created',)
