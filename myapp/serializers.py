from rest_framework import serializers
from . models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'
class ConsumerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Consumer
        fields = ['user','consumer_type']

class FarmerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Farmer
        fields = ['user', 'farmer_type']

class SellerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
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
    farmer = FarmerSerializer()
    consumer = ConsumerSerializer()
    class Meta:
        model = FarmerOrders
        fields = ['farmer','consumer','item_ordered','item_quantity','order_total']
class SellerOrderSerializer(serializers.ModelSerializer):
    seller = SellerSerializer()
    farmer = FarmerSerializer()
    class Meta:
        model = SellerOrders
        fields = ['seller','farmer','item_ordered','item_quantity','order_total']
    
