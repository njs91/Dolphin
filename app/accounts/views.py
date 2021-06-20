from django.shortcuts import render
from .models import *


def account(request):
    return render(request, 'accounts/account.html')


def edit_account(request):
    return render(request, 'accounts/edit_account.html')
