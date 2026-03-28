from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'homepage.html')


class ProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'profile.html')
    

class PostsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'posts.html')
    

class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('homepage')
        return render(request, 'login.html')
    
    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(
                request,
                'login.html',
                context={'error': 'Invalid username or password!!'}
            )
    

class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('homepage')
        return render(request, 'register.html')
    
    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # adding validation
        if len(password) < 4:
            return render(
                request,
                'register.html',
                context={'error': 'The password is too short!!'}
            )

        if password != confirm_password:
            return render(
                request,
                'register.html',
                context={'error': "The passwords don't match!!"}
            )
        
        if User.objects.filter(username=username).exists():
            return render(
                request,
                'register.html',
                context={'error': "Username or Email already exists!!"}
            )
        
        if User.objects.filter(email=email).exists():
            return render(
                request,
                'register.html',
                context={'error': "Username or Email already exists!!"}
            )
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('homepage')
    

class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect('homepage')
    

