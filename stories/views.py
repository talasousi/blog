from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def morning(request):
	return render(request, 'morning.html', {})

def afternoon(request):
	return HttpResponse("<h1> Afternoon <h1>")

def night(request):
	return HttpResponse("<h1> Night <h1>")
# Create your views here.
