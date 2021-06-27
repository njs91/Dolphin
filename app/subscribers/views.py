from django.shortcuts import render
from accounts.models import Account
from subscribers.models import Subscriber


def get_subscribers(request, pk):
    account = Account.objects.get(id=pk)
    subscribers = account.subscriber_set.all()
    context = {'account': account, 'subscribers': subscribers}
    return render(request, 'subscribers/subscribers.html', context)


def get_subscriber(request, pk, sub_id):
    account = Account.objects.get(id=pk)  # pk needed? it'll be in the URL
    subscriber = Subscriber.objects.get(id=sub_id)
    context = {'account': account, 'subscriber': subscriber}
    return render(request, 'subscribers/subscriber.html', context)
