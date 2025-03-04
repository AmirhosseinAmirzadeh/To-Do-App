from django.shortcuts import render
from django.views.generic import FormView
from .forms import RegisterationForm, LoginForm

# Create your views here.
class RegistrationView(FormView):
    "A class for custom registration view"
    template_name = 'register.html'
    form_class = RegisterationForm
    fields = '__all__'
    success_url = 'login.html'


class LoginView(FormView):
    "A class for custom login view"
    template_name = 'login.html'
    form_class = LoginForm
    fields = '__all__'
    success_url = 'index.html'