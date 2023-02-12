from django.http import HttpResponse


def home(request):
    return HttpResponse('<div><h1>Главная страница</h1></div>')


def coffee(request):
    return HttpResponse('Я чайник', status=418)
