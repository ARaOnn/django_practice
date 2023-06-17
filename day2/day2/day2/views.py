from django.http import HttpResponse

# python 파일안에 있는 html코드를 다른 곳에 보내 유지보수,재사용용이하게
# html = """
# 		<h1><a href="/">Django</a></h1>
# 		<ol>
# 			<li><a href="/chapter/01/">Setting & Deploy</a></li>
# 			<li><a href="/chapter/02/">Routing & View</a></li>
# 		</ol>
# 		<h2>{title}</h2>
# 		<p>{content}</p>
# 		<img src='/static/sun.jpg' width='300'>
# 	"""
from django.shortcuts import render

def index(req):
    # return HttpResponse(html.format(
	# 	title='Django',
	# 	content = "Django is ..."
	# ))
	return render(req, 'index.html')

def chapter(req, id):
    chapters = {
	"01": {"title": "Setting & Deploy" , "content": "Setting & Deploy is ..." },
	"02": {"title": "Routing & View" , "content": "Routing & View is ..." },
	}
    # return HttpResponse(html.format(**chapters.get(id)))
    return render(req, 'index.html')