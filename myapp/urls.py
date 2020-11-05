from django.contrib import admin
from django.urls import path, include
from .views import register, user_login, user_logout, home_page, CropListView, SelectedCrops, CropDetail, crop_detail_page
urlpatterns = [
    path('register',register,name='register'),
    path('user_login',user_login,name='user_login'),
    path('user_logout',user_logout, name='user_logout'),
    path('home_page',home_page, name='home_page'),
    path('all_crops',CropListView.as_view(), name='all_crops'),
    path('selected_crops',SelectedCrops.as_view(), name='selected_crops'),
    path('crop_detail/<int:id>',CropDetail.as_view(), name='crop_detail'),
    path('crop_detail_page/<int:id>', crop_detail_page, name='crop_detail_page')
]