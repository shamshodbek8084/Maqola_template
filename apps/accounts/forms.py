from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'id_password'}))
    password2 = forms.CharField(label = "Parolni tasdiqlang", widget=forms.PasswordInput(attrs={'id' : 'id_password2'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password!=password2:
            self.add_error('password2', "Parollar bir xil emas!!!")

        return cleaned_data
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'icon',
            'user',
            'phone_number',
            'address',
            'country',
            'birth',
        ]

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'password'}))
