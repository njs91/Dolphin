from django.db import models

# Create your models here.

# class Account(models.Model):
# fields: subs, em_messages, automations, landing_pages, first_name, last_name, email, date_created

# class Subscriber(models.Model):
# fields: first_name, email, tags, date_created, verified


class Subscriber(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    # tags = _________________
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    verified = models.BooleanField(default=False)
