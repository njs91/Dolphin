from django.db import models
from accounts.models import Account
from messages.models import Message


class Automation(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return self.name
