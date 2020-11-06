from rest_framework import serializers
from . models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'


class FarmerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Farmer
        fields = ['user', 'farmer_type']

class SellerSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Seller
        fields = ['user','seller_type']

class CropSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer()
    class Meta:
        model = Crops
        fields = ['id','name','farmer','state','price','quantity','crop_type']
        #fields = ['name','farmer','state','price','quantity','crop_type']
class RawSerializer(serializers.ModelSerializer):
    seller = SellerSerializer()
    class Meta:
        model = Raw
        fields = ['name','seller','state','price','quantity','raw_type']
class FarmerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerOrders
        fields = ['farmer','consumer','item_orderded','item_quantity','order_total']
class SellerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerOrders
        fields = ['seller','farmer','item_orderded','item_quantity','order_total']
    
