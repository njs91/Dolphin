from django.shortcuts import render
from accounts.models import Account
# from .models import *


def get_account(request, pk):
    account = Account.objects.get(id=pk)
    # subscribers = account.subscriber_set.all()
    # could also use subscribers = Subscriber.objects.filter(account=account) # better?
    context = {'account': account}
    return render(request, 'accounts/account.html', context)


def edit_account(request, pk):
    account = Account.objects.get(id=pk)
    context = {'account': account}
    return render(request, 'accounts/edit_account.html', context)
