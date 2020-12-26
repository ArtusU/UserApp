from typing import ContextManager
from django.shortcuts import render
from django.views.generic.base import ContextMixin
from account.models import CustomUser

def home(request):
    users = CustomUser.objects.all()    
    return render(request, 'index.html', context={'users':users})
