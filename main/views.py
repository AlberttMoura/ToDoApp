from django.shortcuts import render
import requests
from . import models

def home(request):
    user = request.POST

    password = None
    if user['password1'] == user['password2']:
        password = user['password1']

    user_data = {
        'name': user['name'],
        'email': user['email'],
        'password': password,
    }
    print(user_data)
    return render(request, 'index.html', user_data)

def signup(request):
    return render(request, 'signup.html')

