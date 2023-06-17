from django.http import HttpResponse

# def index(request):
#     return HttpResponse('Hello')

def list(request):
    return HttpResponse('List')

def post(request, id):
    return HttpResponse(f'post {id}')

def gugu(req, num):
    # num = int(num)
    gugudan = [f'{num}  * {i} = {num * i}' for i in range(1, 10)]
    return HttpResponse("<br>".join(gugudan))

def daum(req):
    import requests
    res = requests.get("https://www.daum.net")
    return HttpResponse(res.content)

# url에 따라 인자값 다르게 받기
html = """<!doctype html>
<html>
	<head>
		<title>Django</title>
		<meta charset="utf-8">
	</head>
	<body>
		<h1><a href="/">Django</a></h1>
		<ol>
			<li><a href="/chapter/01/">Setting & Deploy</a></li>
			<li><a href="/chapter/02/">Routing & View</a></li>
		</ol>
		<h2>{title}</h2>
		<p>{content}</p>
	</body>
</html>"""

chapters = {
	"01": {"title": "Setting & Deploy" , "content": "Setting & Deploy is ..." },
	"02": {"title": "Routing & View" , "content": "Routing & View is ..." },
}


def index(request):
    d = {'title' : 'django', 
         'content' : 'django is ...'}
    return HttpResponse(html.format(**d))

def chapter(req, id):
    return HttpResponse(html.format(**chapters.get(id)))

