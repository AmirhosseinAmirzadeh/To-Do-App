from django import forms
from .models import User

class RegisterationForm(forms.Form):
    "A form for custom registration"
    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        
        
class LoginForm(forms.Form):
    "A form for custom login"
    class Meta:
        model = User
        fields = ['email', 'password']