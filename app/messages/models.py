from django.db import models
from accounts.models import Account
# from automations.models import Automation  # < FAILS
from automations.models import *  # < WORKS
# from apps.get_model(email_messages, Message)   # < FAILS
# from django.apps get_model(email_messages, Message)  # < FAILS
# from django.apps import apps  # < FAILS
# Automations = apps.get_model('email_messages', 'Messages')  # < FAILS


class Message(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=128)
    text = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    automations = models.ManyToManyField(Automation)

    def __str__(self):
        return self.name
