from django.shortcuts import render, redirect
from django.views import View

from main.models import User
import bcrypt

# Create your views here.

"""
FUNCTION:
---------
get -> when user open webs (this is first page when user see)
post -> when user text any data

VARIABLE:
---------
login -> this is user login
password -> this is user password

ERROR:
---------
not login -> when user don't text a login
not password -> when user don't text a password
len(login) -> when user text login less than 5 or more than 25 characters
"""
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login = request.POST.get('login')
        password = request.POST.get('password')

        if not login:
            return render(request, 'login.html', context={'error': "Logi field can't be empty"})
        if not password:
            return render(request, 'login.html', context={'error': "Password field can't be empty"})
        if len(login) > 25 or len(login) < 8:
            return render(request, 'login.html', context={'error': "This is definitely not your login"})

        user_login = User.objects.get(login=login)

        if user_login.login == login:
            if user_login.password == password:
                return render(request, 'login.html', context={'error': "This is your password!!"})

            return render(request, 'login.html',context={'error': 'Valid password'})

        return render(request, 'login.html', context={'error': 'Valid login'})


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username')
        login = request.POST.get('login')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or not login or not password or not email:
            return render(request, 'register.html', context={"error": "Fill in all data"})
        if len(username) < 5 or len(username) > 25:
            return render(request, 'register.html', context={"error": "Username must be between 5 and 25 characters"})
        if len(login) < 8 or len(login) > 25:
            return render(request, 'register.html', context={"error": "Login must be between 8 and 25 characters"})
        if len(password) < 8 or len(password) > 25:
            return render(request, 'register.html', context={"error": "Password must be between 8 and 25 characters"})

        user_login = User.objects.filter(login=login).first()
        if user_login:
            return render(request, 'register.html', context={"error": "This login is busy"})

        user_username = User.objects.filter(username=username).first()
        if user_username:
            return render(request, 'register.html', context={"error": "This username is busy"})

        user_email = User.objects.filter(email=email).first()
        if user_email:
            return render(request, 'register.html', context={"error": "This e-mail is busy"})

        #password_hash = bcrypt.hashpw(password, bcrypt.gensalt())

        User.objects.create(username=username, login=login, password=password, email=email)
        return redirect('login')

