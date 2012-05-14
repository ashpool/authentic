from django.forms import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.PasswordInput(max_length=100)

