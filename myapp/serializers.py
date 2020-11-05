from rest_framework import serializers
from . models import Crops, Farmer, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'


class FarmerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Farmer
        fields = ['user', 'farmer_type']


class CropSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer()
    class Meta:
        model = Crops
        fields = ['id','name','farmer','state','price','quantity','crop_type']