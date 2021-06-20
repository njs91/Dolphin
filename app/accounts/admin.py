from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import models


class SubscriberInline(admin.TabularInline):
    model = models.Subscriber
    extra = 0


class AccountAdmin(UserAdmin):
    inlines = [SubscriberInline, ]


admin.site.register(models.Account, AccountAdmin)


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email",
                    "date_joined", "verified", "account")
