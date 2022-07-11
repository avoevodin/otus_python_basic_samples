from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)

from .forms import UserCreationForm
from .models import UserModel


class UserCreationView(CreateView):
    model = UserModel
    # success_url = settings.LOGIN_REDIRECT_URL
    success_url = reverse_lazy("animals:list")
    form_class = UserCreationForm
    template_name = "registration/user_register.html"


class LoginView(LoginViewGeneric):
    next_page = reverse_lazy("animals:list")


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("animals:list")
