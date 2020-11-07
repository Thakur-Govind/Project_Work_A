from django.contrib import admin
from django.urls import path, include
from .views import register, user_login, user_logout, home_page, CropListView, SelectedCrops, CropDetail, crop_detail_page,seller_home
from .views import *
urlpatterns = [
    path('register',register,name='register'),
    path('user_login',user_login,name='user_login'),
    path('user_logout',user_logout, name='user_logout'),
    path('home_page',home_page, name='home_page'),
    path('all_crops',CropListView.as_view(), name='all_crops'),
    path('selected_crops',SelectedCrops.as_view(), name='selected_crops'),
    path('crop_detail/<int:id>',CropDetail.as_view(), name='crop_detail'),
    path('crop_detail_page/<int:id>', crop_detail_page, name='crop_detail_page'),
    path('consumer_buy/<int:id>/<int:cropid>/<int:quant>',consumer_buy,name = 'consumer_buy'),
    path('create_crop',create_crop, name = 'create_crop'),
    path('add_crops',add_quantity,name = 'add_crops'),
    path('seller',seller_home, name='seller_home'),
    path('raw_details/<int:id>',RawListView.as_view(),name='raw_details'),
    path('seller_orders/<int:id>',SellerOrderView.as_view(),name= 'seller_orders'),
    path('farmer_orders/<int:id>',FarmerOrderView.as_view(),name= 'farmer_order'),
    path('create_raw',create_raw,name = "new_raw"),
    path('farmer',farmer_home,name = 'farmer_home'),
    path('farmer_crops/<int:id>',FarmerCropView.as_view(), name = 'farmer_crops'),
    path('farmer_shop',farmer_shop,name= 'farmer_shop'),
    path('raw_detail_page/<int:id>',raw_detail,name='raw_detail_page'),
    path('raw_detail/<int:id>',RawDetail.as_view(), name = 'raw_detail'),
    path('all_raw',AllRawView.as_view(), name='all_raws'),
    path('farmer_buy/<int:id>/<int:rawid>/<int:quant>',farmer_buy,name = 'farmer_buy'),

]