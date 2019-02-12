from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


def test(request):
    """view written to check operations on base.html -> to be removed later"""
    return render(request, "base.html")


class MainView(View):
    def get(self, request):
        return render(request, "index.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            try:
                user_details = User.objects.get(email=email)
            except:
                alert = "Niepoprawny użytkownik lub hasło"
                return render(request, "login.html", {"alert": alert})

            user = authenticate(request, username=user_details.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                alert = "Niepoprawny użytkownik lub hasło"
                return render(request, "login.html", {"alert": alert})

        else:
            return render(request, "login.html")


def log_out(request):
    logout(request)
    return redirect('main')
