from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from .models import Profile, Department


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']


class UpdateProfileForm(forms.ModelForm):
    father_name = forms.CharField(max_length=40, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all().order_by('name'))

    class Meta:
        model = Profile
        fields = ['father_name', 'department']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Введите логин',
                                   'class': 'form-control',
                               }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Введите пароль',
                                   'class': 'form-control',
                                   'data-toggle': 'password',
                                   'id': 'password',
                                   'name': 'password',
                               }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']