from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput
from .choice import YEARS, GENDER_CHOICE
from .models import Customer


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, widget=TextInput(attrs={'class': 'form-control col-md-7', }))
    last_name = forms.CharField(max_length=150, widget=TextInput(attrs={'class': 'form-control col-md-7', }))
    username = forms.CharField(max_length=150, widget=TextInput(attrs={'class': 'form-control col-md-7', }))
    email = forms.EmailField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-7', }))
    phone = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control col-md-7', }))
    dob = forms.DateField(widget=forms.SelectDateWidget(years=YEARS, attrs={'class': "d-inline col-md-2 "
                                                                                     "form-control"}))
    gender = forms.CharField(max_length=20, widget=forms.Select(choices=GENDER_CHOICE,
                                                                attrs={'class': 'form-control col-md-7'}))

    password1 = forms.CharField(max_length=500, widget=PasswordInput(attrs={'class': 'form-control col-md-7'}))
    password2 = forms.CharField(max_length=500, widget=PasswordInput(attrs={'class': 'form-control col-md-7'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'dob', 'gender', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_customer = True
    #     if commit:
    #         user.save()
    #     return user
