from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogPost, Comment


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'homepage.html')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'profile.html')


class PostsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        posts = BlogPost.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'posts.html', context=context)
    

class BlogDetailsView(View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        post = get_object_or_404(
            BlogPost.objects.prefetch_related('liked_users'),
            id=id
        )

        comments = post.post_comments.all()
        is_liked = post.liked_users.filter(id=request.user.id).exists()
        like_count = post.liked_users.count()

        post.view_count += 1
        post.save(update_fields=['view_count'])

        context = {
            'post': post,
            'comments': comments,
            'is_liked': is_liked,
            'like_count': like_count,
            'view_count': post.view_count,
        }

        return render(request, 'blog_details.html', context=context)
    
    def post(self, request: HttpRequest, id: int) -> HttpResponse:
        post = get_object_or_404(
            BlogPost.objects.prefetch_related('liked_users'),
            id=id
        )

        comment = request.POST['comment']

        post.view_count -= 1
        post.save(update_fields=['view_count'])

        new_comment = Comment(
            content=comment,
            post=post,
            author=request.user
        )

        new_comment.save()

        return redirect('blog_details', id=post.id)


class ToggleLikeView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        post = get_object_or_404(BlogPost, id=id)

        post.view_count -= 1 # to adjust view counts
        post.save(update_fields=['view_count'])

        if post.liked_users.filter(id=request.user.id).exists():
            post.liked_users.remove(request.user)
        else:
            post.liked_users.add(request.user)

        return redirect('blog_details', id=post.id)


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


class LogoutView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect('homepage')
