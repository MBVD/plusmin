from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from phonenumber_field.modelfields import PhoneNumberField
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import BaseModelFormSet

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form_input', 'placeholder': "Имя пользователя"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form_input', 'placeholder': "Email"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_input', 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form_input', 'placeholder': "Подтверждение пароля"}))

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form_login_input form_input', 'placeholder': 'Имя'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form_password_input form_input', 'placeholder': 'Пароль'}))


class UserProfileChangeForm(forms.ModelForm):
    avatar = forms.ImageField(label='Новая аватарка пользователя', widget=forms.FileInput())
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'birth_date', 'avatar', 'status', 'about_me', 'country']
        widgets = {
            'birth_date': AdminDateWidget(attrs={'type': 'date'}),
        }

class UserSolutionForm(forms.ModelForm):
    image_solution = forms.ImageField(label='Решение в виде фотографии', widget=forms.FileInput(), required = False)
    class Meta:
        model = UserSolution
        fields= ['text_solution', 'image_solution']


class SolutionVerification(forms.ModelForm):
    class Meta:
        model = UserSolution
        fields = ['mark']
