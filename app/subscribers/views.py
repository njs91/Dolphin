from django.http import response
from django.shortcuts import render, redirect
from accounts.models import Account
from subscribers.models import Subscriber
from .forms import SubscriberForm
from .filters import SubscriberFilter


def get_subscribers(request, pk):
    account = Account.objects.get(id=pk)
    subscribers = account.subscriber_set.all()
    filter = SubscriberFilter(request.GET, queryset=subscribers)
    subscribers = filter.qs
    context = {'account': account,
               'subscribers': subscribers, 'filter': filter}
    return render(request, 'subscribers/subscribers.html', context)


def get_subscriber(request, pk, sub_id):
    account = Account.objects.get(id=pk)  # pk needed? it'll be in the URL
    subscriber = Subscriber.objects.get(id=sub_id)
    context = {'account': account, 'subscriber': subscriber}
    return render(request, 'subscribers/subscriber.html', context)


def edit_subscriber(request, pk, sub_id):
    account = Account.objects.get(id=pk)
    subscriber = Subscriber.objects.get(id=sub_id)
    form = SubscriberForm(instance=subscriber)

    if request.method == 'POST':
        form = SubscriberForm(request.POST, instance=subscriber)
        if form.is_valid():
            form.save()
            redirect_url = '/accounts/' + pk + '/subscribers/' + sub_id
            return redirect(redirect_url)

    context = {'subscriber': subscriber, 'form': form, 'account': account}
    return render(request, 'subscribers/edit.html', context)


def delete_subscriber(request, pk, sub_id):
    account = Account.objects.get(id=pk)
    subscriber = Subscriber.objects.get(id=sub_id)
    if request.method == 'POST':
        subscriber.delete()
        redirect_url = '/account/' + pk + '/subscribers/'
        return redirect(redirect_url)
    # @todo: do we need account variable and as part of context?
    context = {'account': account, 'subscriber': subscriber}
    return render(request, 'subscribers/delete.html', context)


def create_subscriber(request, pk):
    account = Account.objects.get(id=pk)
    form = SubscriberForm()

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = '/accounts/' + pk + '/subscribers/'
            return redirect(redirect_url)

    context = {'form': form, 'account': account}
    return render(request, 'subscribers/create.html', context)
