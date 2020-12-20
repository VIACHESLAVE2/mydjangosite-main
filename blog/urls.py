from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
			path('',views.show_posts),
			path('/shrek',views.show_shrek )
]