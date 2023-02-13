from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from home.models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                "class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control"}))

    class Meta:
        model = User
        fields = [
            'username', 'password1', 'password2',
        ]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control"}))

    class Meta:
        model = User
        fields = [
            'username', 'password',
        ]

class HouseCreateForm(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            'address', 'image', 'owner', 'floors', 'squareMeters', 'price',
        ]

class UserHouseForm(forms.ModelForm):
    class Meta:
        model = UserHouse
        fields = [
            'house',
        ]