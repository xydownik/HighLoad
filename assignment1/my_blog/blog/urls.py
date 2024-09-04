from django.urls import path
from . import views
from accounts.views import register, login, logout

urlpatterns = [
    path('', views.post_list_view, name='post_list'),
    path('hello/', views.hello_blog, name='hello_blog'),
    path('blog/posts/', views.post_list, name='post_list'),
    path('blog/posts/<int:id>', views.post_detail, name='post_detail'),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/<int:id>', views.post_detail_view, name='post_detail'),
    path('posts/new/', views.create_post, name='create_post'),
    path('posts/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]