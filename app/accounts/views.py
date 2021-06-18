from django.shortcuts import render
from django.http import HttpResponse  # delete?

# Create your views here.


def account(request):
    return render(request, 'accounts/account.html')


def edit(request):
    return render(request, 'accounts/edit.html')
