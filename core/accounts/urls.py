from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomRegistrationView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
]