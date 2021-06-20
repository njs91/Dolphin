from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from subscribers.models import Subscriber


class SubscriberInline(admin.TabularInline):
    model = Subscriber
    extra = 0


class AccountAdmin(UserAdmin):
    inlines = [SubscriberInline, ]


admin.site.register(Account, AccountAdmin)
