from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import auth
from rest_framework.views import APIView
from myapp.serializers import CropSerializer,RawSerializer,FarmerOrderSerializer,SellerOrderSerializer
#from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
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
				if 'type_farm' in request.POST:
					user_type = request.POST['type_farm']
					user.is_farmer = True
					user.save()
					farmer = Farmer.objects.create(user=user, farmer_type = user_type)
					farmer.save()
				elif 'type_cus' in request.POST:
					user_type = request.POST['type_cus']
					user.is_consumer = True
					user.save()
					consumer = Consumer.objects.create(user=user, consumer_type = user_type)
					consumer.save()
				elif 'type_sel' in request.POST:
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
#################################################CONSUMER VIEWS###########################################################################
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
@api_view(("GET",))
def consumer_buy(request,id,cropid,quant):
	print(type(id))
	crop = get_object_or_404(Crops, pk = cropid)
	crop.quantity -= quant
	if crop.quantity <=0:
		print("Stock now zero")
		crop.quantity = 0
	crop.save()
	order = FarmerOrders()
	user = get_object_or_404(User,pk=id)
	print(user.mid_name)
	consumer = Consumer.objects.all()[0]
	order.consumer = consumer
	order.farmer = crop.farmer
	order.item_ordered = crop.name
	order.item_quantity = quant
	order.order_total = quant*crop.price
	order.save()
	return JsonResponse({'message':"Items bought successfully!"})

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
#################################################CONSUMER VIEWS END######################################################################
##################################################FARMER VIEWS######################################################################
def farmer_home(request):
	return render(request,'myapp/farm2.html')

def create_crop(request):
	ncrop = Crops()
	ncrop.name = request.POST['crop']
	farmer = Farmer.objects.filter(user = request.user)[0]
	ncrop.farmer = farmer
	ncrop.state = farmer.user.state
	ncrop.price = request.user.POST['crop-price']
	ncrop.quantity = request.user.POST['crop-qty']
	ncrop.save()
	return redirect('all_crops')

def add_quantity(request):
	farmers = Farmer.objects.filter(user = request.user)[0]
	crop = Crops.objects.filter(name = request.POST['crop'], farmer=farmers)
	crop.quantity += request.POST['crop-qty']
	return redirect('all_crops')
class FarmerOrderView(APIView):
	def get(self,request):
		farmers = Farmer.objects.filter(user = request.user)[0]
		f_orders = FarmerOrders.objects.filer(farmer = farmers)
		serializer = FarmerOrderSerializer(f_orders,many = True)
		return  Response(serializer.data)
@api_view(("GET",))
def farmer_buy(request,id,quant):
	item = get_object_or_404(Raw,pk=id)
	item.quantity -= quant
	item.save()
	order = SellerOrders()
	order.seller = item.seller
	farmer = Farmer.objects.filer(user=request.user)[0]
	order.farmer = farmer
	order.item_ordered = item.name
	order.item_quantity = quant
	order.order_total = quant*item.price
	order.save()
	return JsonResponse({'message':"Items bought successfully!"})

class FarmerCropView(APIView):
	def get(self,request,id):
		userr = get_object_or_404(User, pk=id)
		farmers = Farmer.objects.filter(user=userr)[0]
		crop = Crops.objects.filter(seller = sellers)
		serializer = CropSerializer(crop,many=True)
		return Response(serializer.data)


#######################################################FARMER VIEWS END##################################################################

#######################################################SELLER VIEWS START################################################################
class RawListView(APIView): 
	def get(self,request,id):
		userr = get_object_or_404(User, pk=id)
		sellers = Seller.objects.filter(user=userr)[0]
		raw = Raw.objects.filter(seller = sellers)
		serializer = RawSerializer(raw,many=True)
		return Response(serializer.data)

# def create_raw(request):
class SellerOrderView(APIView):
	def get(self,request,id):
		userr = get_object_or_404(User,pk = id)
		sellers = Seller.objects.filter(user = userr)[0]
		s_orders = SellerOrders.objects.filter(seller = sellers)
		serializer = SellerOrderSerializer(s_orders,many=True)
		return Response(serializer.data)
def seller_home(request):
	return render(request,'myapp/seller.html')

def create_raw(request):
	raw = Raw()
	raw.name = request.POST['raw_name']
	seller = Seller.objects.filter(user = request.user)[0]
	raw.seller = seller
	raw.price = request.POST['price_raw']
	raw.state = seller.user.state
	raw.quantity = request.POST['raw_quantity']
	raw.raw_type = request.POST['raw_name'].split()[-1].title()
	raw.save()
	return redirect('seller_home')
###############################################################SELLER VIEWS END###########################################################