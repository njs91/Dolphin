import django_filters
from django_filters import DateFilter
from .models import *


class AutomationFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='date_joined', lookup_expr='gte')
    # end_date = DateFilter(field_name='date_joined', lookup_expr='lte')

    class Meta:
        model = Automation  # model we’re building filter for
        fields = '__all__'
        exclude = ['account', 'date_created', 'description', 'messages']
