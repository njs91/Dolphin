from django.forms import ModelForm
from .models import Account


class AccountForm(ModelForm):
    class Meta:
        model = Account  # which model we're building a form for
        # form will now show relevant fields from Account model
        fields = ['email', 'username', 'first_name', 'last_name']
        # fields = '__all__'  # form will now show all fields from Account model
