from http import HTTPStatus

from django.http import HttpResponse


def home(request):
    return HttpResponse('<div>Главная страница</div>')


def coffee(request):
    return HttpResponse('<div>Я чайник</div>', status=HTTPStatus.IM_A_TEAPOT)
