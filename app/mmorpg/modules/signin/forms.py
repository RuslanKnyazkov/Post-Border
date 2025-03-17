from django import forms
from django.contrib.auth.models import User
from .utils import validate_unique_email


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50,
                               label="Имя пользователя",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-input'
                               }))
    password1 = forms.CharField(max_length=30,
                                label="Пароль",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input'
                                }))
    password2 = forms.CharField(max_length=30,
                                label="Повтор пароля",
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input'
                                }))

    email = forms.EmailField(validators=[validate_unique_email])
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
