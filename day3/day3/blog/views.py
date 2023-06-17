from django.shortcuts import render
from . import models

# Create your views here.
# posts = {
# 		'01' : {'title' : 'Template', 'content' : 'Template is ...'},
# 		'02' : {'title' : 'orm' , 'content' : 'orm is ...'}
# }

def home(req):   
    posts = models.Post.objects.all() 
    return render(req, 'blog/index.html', {
        'post_list' : posts,
        'post' : {'title' : 'Django', 
        'content' : 'Django is ...'}
        })
    
def post_list(req, id):
    posts = models.Post.objects.all()
    post = models.Post.objects.get(id=id)
    return render(req, 'blog/index.html', {
        'post_list': posts, 
        'post': post})
