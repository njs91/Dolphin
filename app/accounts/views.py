from django.shortcuts import render, redirect
from accounts.models import Account
from .forms import AccountForm
# from .models import *


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
            # return redirect('/')  # redirects back to '/'

    context = {'account': account, 'form': form}
    return render(request, 'accounts/edit_account.html', context)


def delete_account(request, pk):
    pass

# example below
# def updateOrder(request, pk):
# 	order = Order.objects.get(id=pk) # gets relevant order
# 	form = OrderForm(instance=order) # store in variable

# 	if request.method == ‘POST’:
# 		form = OrderForm(request.POST, instance=order) # pass instance - without instance=order, it would create a new order
# 		if form.is_valid():
# 			form.save() #saves data to DB
# 			return redirect(‘/‘) #redirects back to ‘/‘

# 	context = {‘form’:form}
# 	return render(request, ‘accounts/order_form.html’, context)
