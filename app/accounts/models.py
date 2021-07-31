from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    PLANS = (
        ("free", "free"),
        ("pro", "pro")
    )

    plan = models.CharField(max_length=10, choices=PLANS, default="free")

    def __str__(self) -> str:
        return self.first_name
    # need to add fields: em_messages, automations, landing_pages
    # may need to define some fields as classes in separate apps, then add as foreign key
    # need to make password field required
    # should also use email field instead of username to log in, and require email instead of username when creating accounts
    # set USERNAME_FIELD & REQUIRED_FIELDS?
