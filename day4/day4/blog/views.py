from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(req):
    posts = models.Post.objects.all()
    # return HttpResponse('blog page')
    return render(req, 'blog/index.html', {
		'post_list' : posts
	})
    
def detail(req, id):
    # list, 해당값없어도 오류 없음
    # posts = models.Post.objects.filter(id=id)
    try:
        post = models.Post.objects.get(id=id)
    except Exception as e:
        from django.http import HttpResponseNotFound
        return HttpResponseNotFound('그런 글 없어요')
    return render(req, 'blog/detail.html', {
		'post' : post
	})