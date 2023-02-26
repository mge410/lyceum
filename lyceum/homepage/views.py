from http import HTTPStatus

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    template = 'homepage/index.html'
    context = {}
    return render(request, template, context)


def coffee(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<div>Я чайник</div>', status=HTTPStatus.IM_A_TEAPOT)
