from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    pass
    # subscriber = ____ < one:many
    # subscribers = models.ForeignKey(
    # Subscriber, null = True, on_delete = models.SET_NULL)
    # need to add fields: subs, em_messages, automations, landing_pages
    # may need to define some fields as classes in separate apps, then add as foreign key
    # need to make password field required
    # should also use email field instead of username to log in, and require email instead of username when creating accounts
    # set USERNAME_FIELD & REQUIRED_FIELDS?


class Subscriber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True)
    # tags = _________________ many to many field, with later option of users being able to define custom tags
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    verified = models.BooleanField(default=False)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    list_display = ('first_name', 'email', 'date_joined', 'verified')
