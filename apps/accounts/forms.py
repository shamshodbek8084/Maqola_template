from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


# Ro‘yxatdan o‘tish formasi
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'id_password'}),
        label="Parol"
    )
    password2 = forms.CharField(
        label="Parolni tasdiqlang",
        widget=forms.PasswordInput(attrs={'id': 'id_password2'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            self.add_error('password2', "Parollar bir xil emas!!!")

        return cleaned_data


# Profil uchun forma
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


# Login uchun forma
class LoginForm(forms.Form):
    username = forms.CharField(label="Foydalanuvchi nomi")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'id_password'}), label="Parol")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Foydalanuvchi nomi yoki parol noto‘g‘ri!")
        self.user = user
        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)
