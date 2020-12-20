from django.shortcuts import render
from django.http import HttpResponse

def show_posts(request):
	if request.method == "GET":
		context={"text1": "текст",
				"text2": "текст2"}

		return render(request, 'post_list.html',context)

def show_shrek(request):
	if request.method == "GET":
		return HttpResponse('<a href="https://www.youtube.com/watch?v=P0BL0gc006w">SHREK</a>')
	#elif request.method == "POST":


# Create your views here.
