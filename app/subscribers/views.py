from django.shortcuts import render
from .models import *


def subscribers(request):
    subscribers = Subscriber.objects.all()

    return render(request, 'subscribers/subscribers.html', {'subscribers': subscribers})
