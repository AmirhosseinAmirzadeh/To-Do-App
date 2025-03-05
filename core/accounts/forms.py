from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
from .models import User


class RegisterationForm(UserCreationForm):
    "A form for custom registration"
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
