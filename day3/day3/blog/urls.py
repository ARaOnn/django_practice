from django.urls import path
from django.shortcuts import render
from . import views

app_name = 'blog'
urlpatterns = [
	# path('', views.home),
	# path('<id>/', views.post_list),
	path('', views.post_list, name= 'post_list'),
    path('<int:id>/' , views.post_detail, name='post_detail'),
]
