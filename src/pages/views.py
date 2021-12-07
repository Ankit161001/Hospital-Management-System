from django.shortcuts import render

#from .forms import ProductForm

from .models import Doctor

# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def appoint_view(request, *args, **kwargs):
	return render(request, "appoint.html", {})

def lab_view(request, *args, **kwargs):
	return render(request, "labtest.html", {})

def bed_view(request, *args, **kwargs):
	obj = Doctor.objects.get(id = 1)
	context = {
		'object' : obj
	}
	return render(request, "bookbed.html", context)

def doctor_view(request, *args, **kwargs):
	queryset = Doctor.objects.all()
	context = {
		"object_list" : queryset
	}
	return render(request, "docdetails.html", context)