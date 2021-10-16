from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    PLANS = (
        ("free", "free"),
        ("pro", "pro")
    )

    plan = models.CharField(max_length=10, choices=PLANS, default="free")

    # @todo: add plan field to django admin on individual account pages

    def __str__(self) -> str:
        return self.first_name
