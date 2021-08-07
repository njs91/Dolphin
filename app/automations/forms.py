from django.forms import ModelForm
from .models import Automation


class AutomationForm(ModelForm):
    class Meta:
        model = Automation
        fields = ['name', 'description']
