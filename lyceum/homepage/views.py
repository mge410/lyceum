from datetime import datetime
from http import HTTPStatus

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    template = 'homepage/home.html'
    context = {'date': datetime.now().strftime('%Y %m %d %H:%M')}
    return render(request, template, context)


def coffee(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<div>Я чайник</div>', status=HTTPStatus.IM_A_TEAPOT)
