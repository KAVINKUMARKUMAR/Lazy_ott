from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class CustomLogin(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget= forms.TextInput(attrs={
            'class':'form',
            'placeholder':'enter your username', 
            'style' : 'text-align: center;'
        })
    )

    password = forms.CharField(
        label= '',
        widget= forms.PasswordInput(attrs={
            'class':'form',
            'placeholder':'enter your Password',
            'style' : 'text-align: center;' 
        })
    )

class CustomRegister(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class':'form',
            'placeholder':'enter your username',
            'style' : 'text-align: center;' 
        })
    )
        
    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs={
            'class':'form',
            'placeholder':'enter your Password',
            'style' : 'text-align: center;' 
        })
    )

    password2 = forms.CharField(
        label= '',
        widget= forms.PasswordInput(attrs={
            'class':'form',
            'placeholder':'Confirm Password',
            'style' : 'text-align: center;' 
        })
    )
    class Meta:
        model = User
        fields = ('username','password1','password2')