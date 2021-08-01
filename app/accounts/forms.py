from django.forms import ModelForm
from .models import Account


class AccountForm(ModelForm):  # replace ModelForm with UserCreationForm?
    class Meta:
        model = Account  # which model we're building a form for
        # password not hashed and requires username even if username omitted from fields
        fields = ['email', 'password', 'first_name',
                  'last_name', 'username', 'plan']
        # fields = ['email', 'password1', 'password2',
        #   'first_name', 'last_name', 'username']
        # fields = '__all__'  # form will now show all fields from Account model
