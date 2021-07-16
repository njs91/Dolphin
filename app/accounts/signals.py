from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from .models import Account


# called whenever Account is saved (i.e. new account created from account form or django admin)
def default_account_settings(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)


post_save.connect(default_account_settings, sender=Account)
