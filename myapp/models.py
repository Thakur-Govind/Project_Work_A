from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    mid_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    pan_no = models.CharField(max_length=20)
    aadhar_no = models.CharField(max_length=16)
    is_farmer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_consumer = models.BooleanField(default=False)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='farmer')
    Farmer_choices = (
        ("Food","Food"),
        ("Commercial","Commercial"),
        ("Both","Both")
    )
    farmer_type = models.CharField(max_length=20, choices=Farmer_choices,default="Food")

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='seller')
    seller_choice = (
        ("Pesticide","Pesticide"),
        ("Fertilizer","Fertilizer"),
        ("Seed","Seed")
    )
    seller_type = models.CharField(max_length= 20, choices=seller_choice, default="Pesticide")

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='consumer')
    consumer_choices = (
        ("Consumer","Consumer"),
        ("Retailer","Retailer")
    )
    consumer_type = models.CharField(max_length=20, choices=consumer_choices, default="Consumer")

class Crops(models.Model):
    name = models.CharField(max_length=200)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    state = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    crop_choice = (
        ("Edible","Edible"),
        ("Commercial","Commercial")
    )
    crop_type = models.CharField(max_length=20,choices=crop_choice, default="Edible")

class Raw(models.Model):
    name = models.CharField(max_length=200)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    price = models.IntegerField()
    state = models.CharField(max_length=200)
    quantity = models.IntegerField()
    raw_choice = (
        ("Seeds","Seeds"),
        ("Pesticides","Pesticides"),
        ("Fertilizers", "Fertilizers")
    ) 
    raw_type = models.CharField(max_length=20, choices=raw_choice, default="Seeds")