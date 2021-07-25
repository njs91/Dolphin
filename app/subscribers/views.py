from django.http import response
from django.shortcuts import render, redirect
from accounts.models import Account
from subscribers.models import Subscriber
from .forms import SubscriberForm
from .filters import SubscriberFilter
from django.http import HttpResponse


def get_subscribers(request, pk):
    # if the user doesn't own the account and is not an admin
    if int(pk) is not request.user.id and not request.user.groups.filter(name__in=['admin']).exists():
        return HttpResponse('Account does not have authorisation for access', status=401)
        # @todo: neaten the above 2 lines? put in @decorator or something as repeated often
    account = Account.objects.get(id=pk)
    subscribers = account.subscriber_set.all()
    filter = SubscriberFilter(request.GET, queryset=subscribers)
    subscribers = filter.qs
    context = {'account': account,
               'subscribers': subscribers, 'filter': filter}
    return render(request, 'subscribers/subscribers.html', context)


def get_subscriber(request, pk, sub_id):
    # if the user doesn't own the account and is not an admin
    if int(pk) is not request.user.id and not request.user.groups.filter(name__in=['admin']).exists():
        return HttpResponse('Account does not have authorisation for access', status=401)
    account = Account.objects.get(id=pk)  # pk needed? it'll be in the URL
    subscriber = Subscriber.objects.get(id=sub_id)
    context = {'account': account, 'subscriber': subscriber}
    return render(request, 'subscribers/subscriber.html', context)


def edit_subscriber(request, pk, sub_id):
    # if the user doesn't own the account and is not an admin
    if int(pk) is not request.user.id and not request.user.groups.filter(name__in=['admin']).exists():
        return HttpResponse('Account does not have authorisation for access', status=401)
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
    # if the user doesn't own the account and is not an admin
    if int(pk) is not request.user.id and not request.user.groups.filter(name__in=['admin']).exists():
        return HttpResponse('Account does not have authorisation for access', status=401)
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
    # if the user doesn't own the account and is not an admin
    if int(pk) is not request.user.id and not request.user.groups.filter(name__in=['admin']).exists():
        return HttpResponse('Account does not have authorisation for access', status=401)
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
