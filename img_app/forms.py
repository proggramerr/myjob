from django import forms
from .models import UserProfile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

class AuthForm(forms.Form):
    login = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder':'Электронная почта', 'class': 'form-log-in__email'}

        ),
        
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder':'Пароль', 'class': 'form-log-in__password'}
        )
    )

class RegForm(UserCreationForm):
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'applicant__surname', 'placeholder': 'Фамилия'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'applicant__name', 'placeholder': 'Имя'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Почта', 'class': 'applicant__email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'applicant__password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'class': 'applicant__password'}))

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'class': 'applicasnt__password'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с такой почтой уже зарегистрирован')
        return email

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class RegWorkerForm(RegForm):
    inn = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'ИНН', 'class': 'employer__inn'}),required=True)
    CITY_CHOICES = [
        ('', 'Выберите город'),
        ('Уссурийск', 'Уссурийск'),
        ('Владивосток', 'Владивосток'),
        ('Хабаровск', 'Хабаровск'),
        ('Краснодар', 'Краснодар')
    ]
    city = forms.ChoiceField(choices=CITY_CHOICES, widget=forms.Select(attrs={'class': 'employer__select-city'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с такой почтой уже зарегистрирован')
        return email

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user