from django.shortcuts import render
from django.shortcuts import render, redirect
from accounts.models import Account
from messages.models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from core.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def message_create(request, pk):
    account = Account.objects.get(id=pk)
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            new_message = Message.objects.create(
                name=form['name'].value(),
                subject=form['subject'].value(),
                text=form['text'].value(),
                account=account
            )
            new_message.save()
            redirect_url = '/accounts/' + pk + '/messages/'
            return redirect(redirect_url)

    context = {'form': form, 'account': account}
    return render(request, 'messages/message_create.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def message_view(request, pk, message_id):
    account = Account.objects.get(id=pk)  # pk needed? it'll be in the URL
    message = Message.objects.get(id=message_id)
    context = {'account': account, 'message': message}
    return render(request, 'messages/message_view.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def message_edit(request, pk, message_id):
    account = Account.objects.get(id=pk)
    message = Message.objects.get(id=message_id)
    form = MessageForm(instance=message)

    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            redirect_url = '/accounts/' + pk + '/messages/' + message_id
            return redirect(redirect_url)

    context = {'message': message, 'form': form, 'account': account}
    return render(request, 'messages/message_edit.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def message_delete(request, pk, message_id):
    account = Account.objects.get(id=pk)
    message = Message.objects.get(id=message_id)
    if request.method == 'POST':
        message.delete()
        redirect_url = '/account/' + pk + '/messages/'
        return redirect(redirect_url)

    context = {'account': account, 'message': message}
    return render(request, 'messages/message_delete.html', context)
