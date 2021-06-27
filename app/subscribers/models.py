from django.db import models
from accounts.models import Account


class Tag(models.Model):
    name = models.CharField(max_length=100)
    #subscribers = models.ManyToManyField(Subscriber, blank=True)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True)
    # tags: many to many field, with later option of users being able to define custom tags
    # cannot uncomment, otherwise error: "NameError: name 'Tag' is not defined" - but already has many:many relationship - just not showing in django admin
    tags = models.ManyToManyField(Tag, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    verified = models.BooleanField(default=False)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    list_display = ('first_name', 'email', 'date_joined', 'verified')
