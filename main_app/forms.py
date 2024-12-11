from django import forms
from .models import Shoe
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['name', 'brand', 'price', 'style', 'image_url']




class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'form-input'
        })
    )
    password1 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Create a password',
            'class': 'form-input'
        })
    )
    password2 = forms.CharField(
        required=True,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm your password',
            'class': 'form-input'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']