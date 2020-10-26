from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth.models import auth
#from django.http import HttpResponse
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
		return render(request, 'myapp/home.html')

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
		return render(request,'myapp/home.html')


def user_logout(request):
	auth.logout(request)
	return redirect('user_login')

def home_page(request):
	if request.user.is_authenticated:
		return HttpResponse("Hello, {}".format(request.user))
	else:
		return HttpResponse("Not logged in.")
