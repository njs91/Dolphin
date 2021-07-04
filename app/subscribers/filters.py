import django_filters
from django_filters import DateFilter
from .models import *


class SubscriberFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_joined', lookup_expr='gte')
    end_date = DateFilter(field_name='date_joined', lookup_expr='lte')

    class Meta:
        model = Subscriber  # model we’re building filter for
        fields = '__all__'  # which fields do we wanna allow
        exclude = ['account', 'date_joined']  # exclude these fields
