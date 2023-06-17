"""
URL configuration for day2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.http import FileResponse
from django.shortcuts import render
# from blog import views as blogView

# 동적 이미지 로드
def load_img(req, name):
	img = open(f'static/{name}.jpg', 'rb')
	return FileResponse(img, content_type= 'image/jpeg' )

# templates에서 가져오기
def hello(req):
    return render(req, 'index.html')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index),
    path('hello/', hello),
    path('chapter/<id>/', views.chapter),
    path('images/<name>/' , load_img),
    path('control/', views.control),
    path('child/', views.child),
    # path('blog/', blogView.post_list),   
    path('blog/', include('blog.urls')), # blog폴더 뒤의 url을 blog.urls.py에 위임
]
