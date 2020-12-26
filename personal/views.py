from typing import ContextManager
from django.shortcuts import render
from django.views.generic.base import ContextMixin

def home(request):
    #users = CustomUser.objects.all()    
    return render(request, 'index.html')
