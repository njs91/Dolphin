from django.shortcuts import render, redirect
from accounts.models import Account
from .forms import AccountForm
# from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def get_accounts(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'accounts/account_list.html', context)


@login_required(login_url='login')
def get_account(request, pk):
    account = Account.objects.get(id=pk)
    # subscribers = account.subscriber_set.all()
    # could also use subscribers = Subscriber.objects.filter(account=account) # better?
    context = {'account': account}
    return render(request, 'accounts/account.html', context)


@login_required(login_url='login')
def edit_account(request, pk):
    # @todo: need to only allow account holders to edit their own accounts
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


@login_required(login_url='login')
def delete_account(request, pk):
    account = Account.objects.get(id=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('/')
    else:
        messages.info(request, "Count not delete account.")

    context = {'account': account}
    return render(request, 'accounts/delete.html', context)


def create_account(request):
    if request.user.is_authenticated:
        return redirect('get_account', str(request.user.id))
    else:
        form = AccountForm()
        # form = UserCreationForm()
        # note: issue here when creating account password: makes an invalid format that cannot be used with login form on login page

        if request.method == 'POST':
            form = AccountForm(request.POST)
            # form = UserCreationForm(request.POST)
            # should hash the password, check username/email doesnt already exist, etc
            if form.is_valid():
                form.save()
                # could add message such as 'Account created successfully. You can now log in'
                return redirect('/login')
            else:
                messages.info(request, "Count not create account.")

        context = {'form': form}
        return render(request, 'accounts/create_account.html', context)


def login_page(request):
    print('--- test login ---')
    print('HERE', request.user.id)
    if request.user.is_authenticated:
        return redirect('get_account', str(request.user.id))
    else:
        if request.method == 'POST':
            print('METHOD IS POST')
            username = request.POST.get('username')
            password = request.POST.get('password')
            print('username', username, 'pw', password)

            # authenticate user - ensures they're in db etc
            user = authenticate(request, username=username, password=password)
            print('user', user)
            if user is not None:  # if authenticated successfully
                login(request, user)
                print('--- should be successful')
                return redirect('get_accounts')
            else:
                messages.info(request, "Wrong username or password.")
        print('--- fail')
        context = {}
        return render(request, 'accounts/login.html', context)


# @todo: add login required or check if user is authenticated?
def logout(request):
    logout(request)
    return redirect('login')
