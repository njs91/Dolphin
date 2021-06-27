from django.shortcuts import render
from accounts.models import Account


def get_subscribers(request, pk):
    account = Account.objects.get(id=pk)
    subscribers = account.subscriber_set.all()
    context = {'account': account, 'subscribers': subscribers}
    return render(request, 'subscribers/subscribers.html', context)
