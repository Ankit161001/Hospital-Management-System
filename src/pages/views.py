from django.shortcuts import render

#from .forms import ProductForm

from .models import Doctor

from .models import Ambulance

# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def appoint_view(request, *args, **kwargs):
	return render(request, "appointment.html", {})

def lab_view(request, *args, **kwargs):
	return render(request, "labtest.html", {})

def bed_view(request, *args, **kwargs):
	return render(request, "bookbed.html", {})

def doctor_view(request, *args, **kwargs):
	queryset = Doctor.objects.all()
	context = {
		"object_list" : queryset
	}
	return render(request, "docdetails.html", context)

def contactus_view(request, *args, **kwargs):
	return render(request, "contactus.html", {})

def login_view(request, *args, **kwargs):
	return render(request, "login.html", {})

def register_view(request, *args, **kwargs):
	return render(request, "register.html", {})

def ambulance_view(request, *args, **kwargs):
	queryset = Ambulance.objects.all()
	context = {
		"object_list" : queryset
	}
	return render(request, "ambulance_book.html", context)

def aboutus_view(request, *args, **kwargs):
	return render(request, "aboutus.html", {})