from django import forms
from prices.models import Station, UserProfile, CITY_CHOICES, COMPANY_CHOICES
from django.contrib.auth.models import User


class StationForm(forms.ModelForm):
    
    
    name    = forms.CharField(max_length=128, help_text="Station name")
    company = forms.ChoiceField(choices=COMPANY_CHOICES, help_text="Company")
    city    = forms.ChoiceField(choices=CITY_CHOICES,  help_text="City")
    slug    = forms.SlugField(widget=forms.HiddenInput(), required=False)
    
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Station
        fields = ('name', 'company', 'city')
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website','picture')