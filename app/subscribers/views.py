from django.shortcuts import render, redirect
from accounts.models import Account
from subscribers.models import Subscriber
from .forms import SubscriberForm
from .filters import SubscriberFilter
from django.contrib.auth.decorators import login_required
from core.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def get_subscribers(request, pk):
    account = Account.objects.get(id=pk)
    subscribers = account.subscriber_set.all()
    filter = SubscriberFilter(request.GET, queryset=subscribers)
    subscribers = filter.qs
    context = {'account': account,
               'subscribers': subscribers, 'filter': filter}
    return render(request, 'subscribers/subscribers.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def get_subscriber(request, pk, sub_id):
    account = Account.objects.get(id=pk)  # pk needed? it'll be in the URL
    subscriber = Subscriber.objects.get(id=sub_id)
    context = {'account': account, 'subscriber': subscriber}
    return render(request, 'subscribers/subscriber.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def create_subscriber(request, pk):
    account = Account.objects.get(id=pk)
    form = SubscriberForm()

    if request.method == 'POST':
        form = SubscriberForm(request.POST)

        if form.is_valid():
            new_sub = Subscriber.objects.create(
                first_name=form['first_name'].value(),
                email=form['email'].value(),
                account=account
            )

            new_sub.tags.set(form['tags'].value())
            # for tag in form['tags'].value(): # could also add the tags in a for loop
            #     new_sub.tags.add(tag)
            new_sub.save()
            redirect_url = '/accounts/' + pk + '/subscribers/'
            return redirect(redirect_url)

    context = {'form': form, 'account': account}
    return render(request, 'subscribers/create.html', context)
