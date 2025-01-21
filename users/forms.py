from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class Registration(UserCreationForm):
    username = forms.CharField(label="Введите ваш логин")
    first_name = forms.CharField(label="Введите ваше имя")
    email = forms.EmailField(label='Введите ваш email',required=True)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('username','first_name', 'email', 'password1', 'password2')

#    def clean_password2(self):
#        cd = self.cleaned_data
#        if cd['password1'] != cd['password2']:
#            raise forms.ValidationError('Пароли не совпадают')
#        return cd['password2']


class Login(forms.Form):
    username = forms.CharField(label='Введите ваш логин')
    password = forms.CharField(label='Введите ваш пароль',widget=forms.PasswordInput)
