from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts import models

# does nothing


class SubscriberInline(admin.TabularInline):
    model = models.Subscriber
    extra = 1


admin.site.register(models.Account, UserAdmin)

# does noting


class AccountAdmin(admin.ModelAdmin):
    inlines = [SubscriberInline, ]
    #inlines = (SubscriberInline, )


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email",
                    "date_joined", "verified", "account")
