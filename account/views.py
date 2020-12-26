from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/accounts/login'
    template_name = 'account/signup.html'
