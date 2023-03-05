from http import HTTPStatus

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Item, Tag


def home(request: HttpRequest) -> HttpResponse:
    items = Item.objects.homepage()
    template = 'homepage/home.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def coffee(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<div>Я чайник</div>', status=HTTPStatus.IM_A_TEAPOT)
