from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import post
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm


def show_posts(request):
	if request.method == "GET":
		res = post.objects.all()
		context={'posts': res, 'name': '<script>alert("Pirate!")</script>'}

		return render(request, 'post_list.html',context)

def show_shrek(request):
	if request.method == "GET":
		return HttpResponse('<a href="https://www.youtube.com/watch?v=P0BL0gc006w">SHREK</a>')
	#elif request.method == "POST":

def show_one_post(request, post_id):
	_post = get_object_or_404(post, pk=post_id)
	context = {'post':_post}
	return render(request,'one_post.html',context)

def regestar(request):
	err=""
	if request.method=="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user =form.save() 
			login(request, user)
			return redirect("/blog")
		else:
			err=form.errors.as_data()

	form = UserCreationForm
	context = {"form":form, 'error':err}
	return render(request,'regestar.html',context)


# Create your views here.
