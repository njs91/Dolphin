from django.shortcuts import render
from django.shortcuts import render, redirect
from accounts.models import Account
from automations.models import Automation
from messages.models import Message
from .forms import AutomationForm
from .filters import AutomationFilter
from django.contrib.auth.decorators import login_required
from core.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def automation_list(request, pk):
    account = Account.objects.get(id=pk)
    automations = account.automation_set.all()
    filter = AutomationFilter(request.GET, queryset=automations)
    automations = filter.qs
    context = {'account': account,
               'automations': automations, 'filter': filter}
    return render(request, 'automations/automation_list.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def automation_create(request, pk):
    account = Account.objects.get(id=pk)
    form = AutomationForm()

    if request.method == 'POST':
        form = AutomationForm(request.POST)

        if form.is_valid():
            new_automation = Automation.objects.create(
                name=form['name'].value(),
                description=form['description'].value(),
                account=account
            )
            new_automation.save()
            redirect_url = '/accounts/' + pk + '/automations'
            return redirect(redirect_url)

    context = {'form': form, 'account': account}
    return render(request, 'automations/automation_create.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def automation_view(request, pk, automation_id):
    account = Account.objects.get(id=pk)  # pk needed? it'll be in the URL
    automation = Automation.objects.get(id=automation_id)
    messages = Message.objects.filter(automations__account=account)
    context = {'account': account,
               'automation': automation, 'messages': messages}
    return render(request, 'automations/automation_view.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def automation_edit(request, pk, automation_id):
    account = Account.objects.get(id=pk)
    automation = Automation.objects.get(id=automation_id)
    form = AutomationForm(instance=automation)

    if request.method == 'POST':
        form = AutomationForm(request.POST, instance=automation)
        if form.is_valid():
            form.save()
            redirect_url = '/accounts/' + pk + '/automations/' + automation_id
            return redirect(redirect_url)

    context = {'automation': automation, 'form': form, 'account': account}
    return render(request, 'automations/automation_edit.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'], own_account_only=True)
def automation_delete(request, pk, automation_id):
    account = Account.objects.get(id=pk)
    automation = Automation.objects.get(id=automation_id)
    if request.method == 'POST':
        automation.delete()
        redirect_url = '/accounts/' + pk + '/automations'
        return redirect(redirect_url)

    context = {'account': account, 'automation': automation}
    return render(request, 'automations/automation_delete.html', context)
