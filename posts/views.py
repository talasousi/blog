from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Post
# Create your views here.

def post_create(request):
	post_list = Post.objects.all()
	content = Post.objects.all().first()
	context = {
		"title": "Post Page",
		"content": content,
		"random_numbers": random.randint(1,1000),
		"user": request.user,
		"list": post_list,
	}
	return render(request, 'create.html', context)

def post_update(request):
	return HttpResponse("<h1> Update <h1>")

def post_delete(request):
	return HttpResponse("<h1> Delete <h1>")

def post_list(request):
	return HttpResponse("<h1> List <h1>")

def post_detail(request):
	return HttpResponse("<h1> Detail <h1>")

def cat(request):
	return HttpResponse("<h1> Cat <h1>")

def dog(request):
	return HttpResponse("<h1> Dog <h1>")

def mouse(request):
	return HttpResponse("<h1> Mouse <h1>")
