from django.shortcuts import render, redirect
from accounts.models import Account
from .forms import AccountForm
# from .models import *
from django.contrib.auth.forms import UserCreationForm


def get_accounts(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'accounts/account_list.html', context)


def get_account(request, pk):
    account = Account.objects.get(id=pk)
    # subscribers = account.subscriber_set.all()
    # could also use subscribers = Subscriber.objects.filter(account=account) # better?
    context = {'account': account}
    return render(request, 'accounts/account.html', context)


def edit_account(request, pk):
    account = Account.objects.get(id=pk)
    form = AccountForm(instance=account)

    if request.method == 'POST':
        # print('post', request.POST)
        # pass instance - without instance=account, it would create a new account
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()  # saves data to DB

    context = {'account': account, 'form': form}
    return render(request, 'accounts/edit_account.html', context)


def delete_account(request, pk):
    account = Account.objects.get(id=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('/')

    context = {'account': account}
    return render(request, 'accounts/delete.html', context)


def create_account(request):
    form = AccountForm()
    # form = UserCreationForm()

    if request.method == 'POST':
        form = AccountForm(request.POST)
        # form = UserCreationForm(request.POST)
        # should hash the password, check username/email doesnt already exist, etc
        if form.is_valid():
            form.save()
            return redirect('/login')

    context = {'form': form}
    return render(request, 'accounts/create_account.html', context)


def login_page(request):
    context = {}
    return render(request, 'accounts/login.html', context)
