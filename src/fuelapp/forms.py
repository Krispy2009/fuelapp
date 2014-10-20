from django import forms
from prices.models import Station


class StationForm(forms.ModelForm):
    name    = forms.CharField(max_length=128, help_text="Station name")
    company = forms.CharField(max_length=32,  help_text="Company name")
    city    = forms.CharField(max_length=16,  help_text="City")
    slug    = forms.SlugField(widget=forms.HiddenInput(), required=False)
    
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Station
        fields = ('name',)