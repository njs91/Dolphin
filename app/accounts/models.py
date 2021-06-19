from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    pass
    # ensure has fields: subs, em_messages, automations, landing_pages, first_name, last_name, email, date_joined, password
    # should also use email field instead of username to log in, and require email instead of username when creating accounts
    # set USERNAME_FIELD & REQUIRED_FIELDS?


class Subscriber(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    # tags = _________________
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    verified = models.BooleanField(default=False)
