from django.contrib import admin
from django.urls import path, include
from main import views


urlpatterns = [
    path('posts/comments/<int:postId>/<int:countComments>/', views.comments, name='comments'),
    path('posts/likes/<int:postId>/<int:countLikes>/', views.likes, name='likes'),
    path('access/', views.access, name='access'),
    path('posts/popular/<int:countPosts>/', views.popular, name='posts'),
    path('posts/last/<int:countPosts>/', views.last, name='last posts'),
    path('posts/<int:countPosts>/', views.posts, name='posts'),
    path('user/', views.user, name='user'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('error/', views.error, name='error'),
    path('json/', views.json, name='json'),
    path('set/', views.set, name='set'),
    path('get/', views.get, name='get')
]