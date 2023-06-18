from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms

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
    
def create(req):
    if req.method == 'POST':
        # print(req.POST.get('title'))
        # print(req.POST.get('content'))
        new_post = models.Post(
			title = req.POST.get('title'),
			content = req.POST.get('content')
		)
        new_post.save()
        return redirect('/blog/')
    return render(req, 'blog/create.html')

def create_form(req):
    if req.method == 'POST':
        form = forms.PostForm(req.POST)
        # 유효성 검사
        if form.is_valid():
            new_post = models.Post(
				title=form.cleaned_data['title'],
				content=form.cleaned_data['content'],
				published_at = form.cleaned_data['published']
				)
            new_post.save()
            return redirect('/blog/')
    else:
        form = forms.PostForm()
    return render(req, 'blog/create_form.html',{'form' : form})

def create_form2(req):
    if req.method == 'POST':
        form = forms.PostModelForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = forms.PostModelForm()

    return render(req, "blog/create_form.html", {'form': form})