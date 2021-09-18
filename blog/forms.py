from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import fields
from django.forms import widgets, PasswordInput
from .models import Contact, Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.fields import CharField, ImageField

from django.forms.widgets import EmailInput, FileInput, HiddenInput, NumberInput, PasswordInput, TextInput,TextInput


# class Contactform(forms.Form):
#     name = forms.CharField(max_length=20, widget=TextInput(
#         attrs={"class": "form-control"}))
#     email = forms.EmailField(widget=TextInput(attrs={"class": "form-control"}))
#     contact = forms.IntegerField(
#         widget=NumberInput(attrs={"class": "form-control"}))
#     query = forms.CharField(widget=TextInput(
#         attrs={"class": "form-control"}), label="Write Your Query")

#                        or

class ConttactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields="__all__"
        exclude = ["user"]
        widgets = {"name": TextInput(attrs={"class": "form-control"}), "email": EmailInput(attrs={"class": "form-control"}),
                   "contact": NumberInput(attrs={"class": "form-control"}), "query": TextInput(attrs={"class": "form-control"}), }
        labels = {"query": "Write Your Query"}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude=["p_author"]

        widgets = { "p_title": TextInput(attrs={"class": "form-control"}), "p_body":TextInput(attrs={"class": "form-control  body", }),
                   "p_head1": TextInput(attrs={"class": "form-control"}), "p_chead1":TextInput(attrs={"class": "form-control head1", }), "p_head2": TextInput(attrs={"class": "form-control"}), "p_chead2":TextInput(attrs={"class": "form-control head2", }), "p_thumbnail":FileInput(attrs={"class": "form-control", }),  }
                   
        labels = {"p_title": "Title", "p_body": "Body", "p_head1": "Head", "p_chead1": "Head Content",
                  "p_head2": "Head 2", "p_chead2": "Head 2 Content", "p_thumbnail": "Image"}


class Customusercreation(UserCreationForm):
    password1 = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]
        widgets = {"first_name": TextInput(attrs={"class": "form-control"}), "last_name": TextInput(attrs={"class": "form-control"}),
                   "username": TextInput(attrs={"class": "form-control"}), "email": EmailInput(attrs={"class": "form-control"})}


class Customerlogin(forms.Form):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control"}))
