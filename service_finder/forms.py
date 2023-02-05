from django import forms
from django.contrib.auth .forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class CustomrRegistrationForm(UserCreationForm):
    password1 = forms.CharField(lable='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email= forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
class Meta:
    model=User
    fields = ['username','email','password1','password2']
    lable ={'email':'Email'}
    widgets ={'username': forms.TextInput(attrs={'class','form-control'})}