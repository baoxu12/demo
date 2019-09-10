from django.http import HttpResponse
def test(request):
    return HttpResponse('第一个页面hello world')
