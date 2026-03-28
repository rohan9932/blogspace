from django.urls import path
from .views import (
    HomeView,
    ProfileView,
    LoginView,
    LogoutView,
    RegisterView,
    PostsView,
    BlogDetailsView,
    ToggleLikeView
)

urlpatterns = [
    path("", HomeView.as_view(), name='homepage'),
    path("login/", LoginView.as_view(), name='login'),
    path("register/", RegisterView.as_view(), name='register'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path("posts/", PostsView.as_view(), name='posts'),
    path('posts/<int:id>', BlogDetailsView.as_view(), name='blog_details'),
    path('posts/<int:id>/like/', ToggleLikeView.as_view(), name='toggle_like')
]
