from django.shortcuts import render
import requests
from . import models

def home(request):
    user_data = {}
    
    if request.POST:
        user = request.POST
        password = None

        if models.User.objects.filter(user_email=user['email'].upper()).exists():
            print("Esse e-mail já foi cadastrado")
        else:
            if user['password1'] == user['password2']:
                password = user['password1']

            user_data = {
                'name': user['name'],
                'email': user['email'].upper(),
                'password': password,
            }
            print(f"nome:{user_data['name']}\ne-mail:{user_data['email']}\nsenha:{user_data['password']}")
            models.User.objects.create(user_name=user_data['name'], user_email=user_data['email'], user_password=user_data['password'])




    return render(request, 'index.html', user_data)

def signup(request):
    return render(request, 'signup.html')
