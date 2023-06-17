from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello')

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