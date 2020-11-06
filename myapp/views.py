from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import auth
from rest_framework.views import APIView
from myapp.serializers import CropSerializer,RawSerializer,FarmerOrderSerializer,SellerOrderSerializer
#from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib import messages
# Create your views here.
def register(request):
	if request.method == 'POST':
		fname = request.POST['firstname']
		mname = request.POST['middlename']
		lname = request.POST['lastname']
		email = request.POST['email']
		dob = request.POST['dob']
		aadhaar = request.POST['aadhaar']
		pan = request.POST['pan']
		phone = request.POST['phone']
		username = request.POST['username']
		password1 = request.POST['password_reg']
		password2 = request.POST['conf_password_reg']
		state = request.POST['stt']
		city = request.POST['city']
		
		if not User.objects.filter(email=email).exists():
			if password1 == password2:
				user = User.objects.create_user(
					email=email, username=username, password = password1, first_name = fname, last_name = lname, mid_name = mname, dob = dob,
					pan_no = pan, aadhar_no = aadhaar, state = state, city = city
					)
				if request.POST['type_farm']!='None':
					user_type = request.POST['type_farm']
					user.is_farmer = True
					user.save()
					farmer = Farmer.objects.create(user=user, farmer_type = user_type)
					farmer.save()
				elif request.POST['type_cus']!='None':
					user_type = request.POST['type_cus']
					user.is_consumer = True
					user.save()
					consumer = Consumer.objects.create(user=user, consumer_type = user_type)
					consumer.save()
				elif request.POST['type_sel']!='None':
					user_type = request.POST['type_sel']
					user.is_seller = True
					user.save()
					seller = Seller.objects.create(user=user, seller_type = user_type)
					seller.save()
				auth.login(request, user)
				return redirect('home_page')
			else:
				messages.info(request,"Passwords not matching.")
				return redirect('register')
		else:
			messages.info(request,"Email taken")
			return redirect('register')
	else:
		return render(request, 'myapp/home_up.html')

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password_reg']
		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('home_page')
		else:
			messages.info(request,"email or password incorrect")
			return redirect('user_login')
	else:
		return render(request,'myapp/home_up.html')


def user_logout(request):
	auth.logout(request)
	return redirect('user_login')

def home_page(request):
	if request.user.is_authenticated:
		return render(request,'myapp/con_page.html')
	else:
		return HttpResponse("Not logged in.")

class CropListView(APIView):
	def get(self,request):
		crops = Crops.objects.all()
		serializer = CropSerializer(crops, many=True)
		return Response(serializer.data)

def consumer_buy(request,cropid,quant):
	crop = get_object_or_404(Crops, pk = cropid)
	crop.quantity -= quant
	if crop.quantity <=0:
		print("Stock now zero")
	crop.save()
	order = FarmerOrders()
	order.consumer = request.user
	order.farmer = crop.farmer
	order.item_ordered = crop.name
	order.item_quantity = quant
	order.order_total = quant*crop.price
	order.save()
	return HttpResponse("Items Sold Successfully")

class SelectedCrops(APIView):

	def get(self, request):
		crop = request.query_params.get('crop',None)
		state = request.query_params.get('state',None)

		if crop is not None and state is not None:
			crops = Crops.objects.filter(name=crop, state=state)
			serializer = CropSerializer(crops, many=True)
			return Response(serializer.data)

class CropDetail(APIView):

	def get(self,request,id):
		crop = Crops.objects.get(id=id)
		serializer = CropSerializer(crop)
		return Response(serializer.data)

def crop_detail_page(request,id):
	return render(request,'myapp/con_buy_farm.html',{'id':id})
##################################################FARMER VIEWS######################################################################
def create_crop(request):
	ncrop = Crops()
	ncrop.name = request.POST['name']
	ncrop.farmer = request.user
	ncrop.state = request.user.User.state
	ncrop.price = request.user.POST['price']
	ncrop.quantity = request.user.POST['quantity']
	ncrop.save()
	return HttpResponse("New Crop Added successfully")

def add_quantity(request):
	crop = Crops.objects.filter(name = request.POST['name'])
	crop.quantity += request.POST['quantity']
	return HttpResponse("Crops updated successfully")
#######################################################FARMER VIEWS END##################################################################

#######################################################SELLER VIEWS START################################################################
class RawListView(APIView):
	def get(self,request):
		raw = Raw.objects.all()
		serializer = RawSerializer(raw,many=True)
		return Response(serializer.data)

def farmer_buy(request,id,quant):
	item = get_object_or_404(Raw,pk=id)
	item.quantity -= quant
	item.save()
	order = SellerOrders()
	order.seller = item.seller
	order.farmer = request.user
	order.item_ordered = item.name
	order.item_quantity = quant
	order.order_total = quant*item.price
	order.save()
	
# def create_raw(request):

class FarmerOrderView(APIView):
	def get(self,request):
		f_orders = FarmerOrders.objects.all()
		serializer = FarmerOrderSerializer(f_orders,many = True)
		return  Response(serializer.data)

class SellerOrderView(APIView):
	def get(self,request):
		s_orders = SellerOrders.objects.all()
		serializer = SellerOrderSerializer(s_orders,many=True)
		return Response(serializer.data) 
