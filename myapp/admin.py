from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Farmer)
admin.site.register(Seller)
admin.site.register(Consumer)
admin.site.register(Crops)
admin.site.register(Raw)
admin.site.register(SellerOrders)
admin.site.register(FarmerOrders)
