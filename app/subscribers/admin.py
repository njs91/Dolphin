from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from subscribers import models


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email",
                    "date_joined", "verified", "account")
