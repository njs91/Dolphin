from django.shortcuts import render
from accounts.models import Account
from subscribers.models import Subscriber
from .models import *


def account(request, id):
    account = Account.objects.get(id=id)
    # subscribers = account.subscribers_set.all()
    context = {'account': account}
    return render(request, 'accounts/account.html', context)


def edit_account(request):
    return render(request, 'accounts/edit_account.html')
