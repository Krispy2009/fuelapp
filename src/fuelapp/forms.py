from django import forms
from prices.models import Station, UserProfile
from django.contrib.auth.models import User


class StationForm(forms.ModelForm):
    
    cities = (
        ('nicosia', 'Nicosia'),
        ('larnaca', 'Larnaca'),
        ('paphos', 'Paphos'),
        ('limassol', 'Limassol'),
        ('famagusta', 'Famagusta')
    )
    
    name    = forms.CharField(max_length=128, help_text="Station name")
    company = forms.CharField(max_length=32,  help_text="Company name")
    city    = forms.ChoiceField(choices=cities,  help_text="City")
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