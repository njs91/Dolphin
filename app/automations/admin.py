from django.contrib import admin
from automations.models import Automation
from messages.models import Message


# class MessageInline(admin.TabularInline):
#     model = Message
#     extra = 0


@admin.register(Automation)
class AutomationAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "account", "date_created")
    fields = ("name", "description", "account")  # @todo: add messages
    list_filter = ('date_created',)
    # inlines = [MessageInline, ]
