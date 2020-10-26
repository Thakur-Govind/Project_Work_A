from django.contrib import admin
from django.urls import path, include
from .views import register, user_login, user_logout, home_page
urlpatterns = [
    path('register',register,name='register'),
    path('user_login',user_login,name='user_login'),
    path('user_logout',user_logout, name='user_logout'),
    path('home_page',home_page, name='home_page')
]