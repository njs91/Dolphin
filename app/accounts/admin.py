from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from subscribers.models import Subscriber


# class SubscriberInline(admin.TabularInline):
#     model = Subscriber
#     extra = 0


# class AccountAdmin(UserAdmin):
#     inlines = [SubscriberInline, ]
#     list_display = ("first_name", "plan", "email")

# @todo: make plan field show in django admin on individual account pages


class AccountAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email", "date_joined",
                    "username", 'password', 'plan')
    # show filter option according to specified field
    list_filter = ('date_joined',)
    # fields = ("first_name", "email", "date_joined", "username", 'password', 'plan') # would only show these fields on indivdual user page
    # inlines = [SubscriberInline, ] # would show a table of subscribers on individual user page
    # exclude = ('first_name') # would exclude from individual user page


admin.site.register(Account, AccountAdmin)
