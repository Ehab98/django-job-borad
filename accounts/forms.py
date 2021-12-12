from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields =['username','first_name','last_name','email']

class ProfileForm (forms.ModelForm):
    class Meta:
        model=Profile
        fields=['city','phone_number','image']


class SignupForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1','password2']