from django.shortcuts import render

# Create your views here.
posts = {
		'01' : {'title' : 'Template', 'content' : 'Template is ...'},
		'02' : {'title' : 'orm' , 'content' : 'orm is ...'}
}

def home(req):    
    return render(req, 'blog/index.html', {
        'post_list' : posts,
        'title' : 'Django', 
        'content' : 'Django is ...'})
    
def post_list(req, id):
    
    return render(req, 'blog/index.html', {
        'post_list' : posts, 
        **posts.get(id) })
