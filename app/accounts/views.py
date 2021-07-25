from django.shortcuts import render, redirect
from accounts.models import Account
from .forms import AccountForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.decorators import unauthenticated_user, allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def get_accounts(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'accounts/account_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def get_account(request, pk):
    account = Account.objects.get(id=pk)
    # subscribers = account.subscriber_set.all()
    # could also use subscribers = Subscriber.objects.filter(account=account) # better?
    context = {'account': account}
    return render(request, 'accounts/account.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def edit_account(request, pk):
    account = Account.objects.get(id=pk)
    form = AccountForm(instance=account)

    if request.method == 'POST':
        # pass instance - without instance=account, it would create a new account
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()  # saves data to DB

    context = {'account': account, 'form': form}
    return render(request, 'accounts/edit_account.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def delete_account(request, pk):
    account = Account.objects.get(id=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('/')
    else:
        messages.info(request, "Count not delete account.")

    context = {'account': account}
    return render(request, 'accounts/delete.html', context)


@unauthenticated_user
def create_account(request):
    form = AccountForm()
    # form = UserCreationForm()
    # note: issue here when creating account password: makes an invalid format that cannot be used with login form on login page

    if request.method == 'POST':
        form = AccountForm(request.POST)
        # form = UserCreationForm(request.POST)
        # should hash the password, check username/email doesnt already exist, etc
        if form.is_valid():
            user = form.save(commit=False)
            # required, otherwise password not hashed
            user.set_password(form.cleaned_data["password"])
            user.save()
            # group = Group.objects.get(name='customer') #group now added via signal 'default_account_settings
            # user.groups.add(group)
            # could add message such as 'Account created successfully. You can now log in'
            return redirect('/login')
        else:
            messages.info(request, "Count not create account.")

    context = {'form': form}
    return render(request, 'accounts/create_account.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate user - ensures they're in db etc
        user = authenticate(request, username=username, password=password)

        if user is not None:  # if authenticated successfully
            login(request, user)
            # return redirect('get_accounts')
            return redirect('get_account', str(request.user.id))
        else:
            messages.info(request, "Wrong username or password.")

    context = {}
    return render(request, 'accounts/login.html', context)


# Fn cannot be called logout, otherwise conflicts with default logout name
def logout_user(request):
    logout(request)
    return redirect('login')
