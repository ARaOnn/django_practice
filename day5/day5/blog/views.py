from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
from django.forms.models import model_to_dict

# Create your views here.
def index(req):
    # return HttpResponse('blog index')
    posts = models.Post.objects.all()
    return HttpResponse(posts)

def api_posts(req):
    if req.method == 'GET':
        posts = models.Post.objects.all()
        return JsonResponse({'results':list(posts.values())})
    elif req.tethod == 'POST':
        # post 생성 로직
        return JsonResponse({'results': 'ok'})
    
def api_post(req, id):
    post = models.Post.objects.get(id=id)
    return JsonResponse({'results' : model_to_dict(post)})