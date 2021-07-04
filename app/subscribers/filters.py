import django_filters
from .models import *


class SubscriberFilter(django_filters.FilterSet):
    class Meta:
        model = Subscriber  # model we’re building filter for
        fields = '__all__'  # which fields do we wanna allow
