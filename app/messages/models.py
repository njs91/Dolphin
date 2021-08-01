from django.db import models
from accounts.models import Account


class Message(models.Model):
    name = models.CharField(max_length=100),
    subject = models.CharField(max_length=128),
    text = models.TextField(),
    account = models.ForeignKey(Account, on_delete=models.CASCADE),
    #automations = models.ManyToMainField(Automation)

    def __str__(self):
        return self.name
