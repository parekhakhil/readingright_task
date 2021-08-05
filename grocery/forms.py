from django import forms
from .models import Grocery

class DateInput(forms.DateInput):
    input_type = 'date'


class AddGraceryListForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Grocery
        fields = ['product','quantity','status','date']
