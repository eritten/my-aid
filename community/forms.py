from django import forms
from . models import Profile
from django.contrib.auth.models import User

class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'sex', 'date_of_birth', 'occupation', 'profile_picture', 'about', 'city', 'country', 'telephone_number', 'status']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {"password": forms.PasswordInput()}
