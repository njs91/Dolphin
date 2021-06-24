from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from subscribers import models


# class TagInline(admin.TabularInline):
#     model = models.Tag.subscribers.through
#     extra = 0
# unneeded - individual tag pages already show their subscribers


# class SubscriberInline(admin.TabularInline):
#     model = models.Subscriber.tags.through # ERROR: attributeError: type object 'Subscriber' has no attribute 'tags'


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email",
                    "date_joined", "verified", "account")


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    model = models.Subscriber
    # inlines = [TagInline, ] # inlines unneeded - individual tag pages already show their subscribers
    list_display = ("name", )
