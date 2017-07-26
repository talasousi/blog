from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib	import messages
# Create your views here.

#def post_create(request):
#	content = Post.objects.all().first()
#	context = {
#		"title": "Post Page",
#		"content": content,
##		"list": post_list,
#	}
#	return render(request, 'create.html', context)

def post_update(request, post_id):
	post_object = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None, instance=post_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Post updated")
		return redirect("posts:list")
	context = {
		"form": form,
		"post_object": post_object,
	}

	return render(request, 'post_update.html', context)

def post_delete(request, post_id):
	Post.objects.get(id=post_id).delete()
	messages.warning(request, "message deleted")
	return redirect("posts:list")

def post_list(request):
	obj_list = Post.objects.all()#.order_by("-timestamp", "-updated")
	context = {
		"post_list": obj_list,
	}

	return render(request, 'post_list.html', context)

def post_detail(request, post_id):
	obj = get_object_or_404(Post, id=post_id)
	context = {
		"instance": obj,
	}
	return render(request, 'post_detail.html', context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Post created")
		return redirect("posts:list")
	context = {
		"form": form,
	}

	return render(request, 'post_create.html', context)