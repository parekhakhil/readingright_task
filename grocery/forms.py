from django import forms
from .models import Grocery

class DateInput(forms.DateInput):
    input_type = 'date'

class AddGraceryListForm(forms.ModelForm):
    date = forms.DateField(input_formats= ['%d-%m-%Y'])
    class Meta:
        model = Grocery
        fields = ['product','quantity','status','date']
        widgets = {
            'date': DateInput(),
        }
