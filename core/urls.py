from django.urls import path
from .views import (
    HomeView,
    ProfileView,
    LoginView,
    LogoutView,
    RegisterView,
    PostsView,
    BlogDetailsView,
    ToggleLikeView,
    CreateBlogPostView,
    EditBlogPostView,
    DeleteBlogPostView
)

urlpatterns = [
    path("", HomeView.as_view(), name='homepage'),
    path("login/", LoginView.as_view(), name='login'),
    path("register/", RegisterView.as_view(), name='register'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("profile/", ProfileView.as_view(), name='profile'),
    path("posts/", PostsView.as_view(), name='posts'),
    path('posts/<int:id>', BlogDetailsView.as_view(), name='blog_details'),
    path('posts/<int:id>/like/', ToggleLikeView.as_view(), name='toggle_like'),
    path('create/', CreateBlogPostView.as_view(), name='add_post'),
    path('edit/<int:id>', EditBlogPostView.as_view(), name='edit_post'),
    path('delete/<int:id>', DeleteBlogPostView.as_view(), name='delete_post')
]
