from django.shortcuts import render
from django.http import JsonResponse
import requests

def text_search(request):
	api_key = 'AIzaSyD74plURlNJbj45Q3lZAcDHAHn1UjYRoKI'
	query = request.GET.get("query", '')
	next_page_token = request.GET.get("next_page_token")
	url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s'%(query, api_key)

	if next_page_token is not None:
		url+="&pagetoken=%s"%(next_page_token)

	response = requests.get(url)

	# return JsonResponse(response.json(), safe=False)

	return render(request, 'text.html', {'response': response.json()})

def place_detail(request):
	api_key = 'AIzaSyD74plURlNJbj45Q3lZAcDHAHn1UjYRoKI'
	key = 'AIzaSyBEvWXgxlD_928Z_mnD6QLstI648swdgi8'
	reference = request.GET.get("reference", '')
	next_page_token = request.GET.get("next_page_token")
	url = 'https://maps.googleapis.com/maps/api/place/details/json?reference=%s&key=%s'%(reference, api_key)

	response = requests.get(url)

	# return JsonResponse(response.json(), safe=False)

	return render(request, 'detail.html', {'response': response.json(), 'key': key})


def radius_search(request):
	api_key = 'AIzaSyCLsBEq2BEOReQ77h3eGBe44ewoNL6tnps'
	radius = request.GET.get('radius', '')
	location = request.GET.get('location')
	# next_page = request.GET.get("next_page_token")
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%s&radius=%s&key=%s'%(location, radius, api_key)

	# if next_page is not None:
	# 	url+="&pagetoken=%s"%(next_page)

	response = requests.get(url)

	# return JsonResponse(response.json(), safe=False)

	return render(request, 'radius.html', {'response': response.json()})