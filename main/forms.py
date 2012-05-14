from django.contrib.auth.models import User
from django.forms import forms
from django.forms.fields import EmailField, CharField
from django.forms.models import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class ContactForm(forms.Form):
    message = CharField()
    sender = EmailField(required=False)