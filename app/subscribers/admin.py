from django.contrib import admin
from subscribers import models


class SubscriberInline(admin.TabularInline):
    model = models.Subscriber.tags.through
    extra = 0


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email",
                    "date_joined", "verified", "account")


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    model = models.Subscriber
    list_display = ("name", )
    inlines = [SubscriberInline, ]
