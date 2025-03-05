from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic import FormView
from .forms import RegisterationForm
from django.urls import reverse_lazy

# Create your views here.
class CustomRegistrationView(FormView):
    "A class for custom registration view"
    template_name = 'accounts/register.html'
    form_class = RegisterationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('accounts:login')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegistrationView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('accounts:login')
        return super(CustomRegistrationView, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    "A class for custom login view"
    template_name = 'accounts/login.html'
    fields = 'email', 'password'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('todo:todo-list')
