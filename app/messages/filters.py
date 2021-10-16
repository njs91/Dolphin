import django_filters
from django_filters import DateFilter
from .models import *


class MessageFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='date_joined', lookup_expr='gte')
    # end_date = DateFilter(field_name='date_joined', lookup_expr='lte')

    class Meta:
        model = Message  # model we’re building filter for
        fields = '__all__'
        # @todo: add automations back and get it to be able to filter by them (it's a select input)
        exclude = ['account', 'date_created', 'text', 'subject', 'automations']
