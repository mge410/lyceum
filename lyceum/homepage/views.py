from http import HTTPStatus

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Prefetch
from catalog.models import Item, Tag


def home(request: HttpRequest) -> HttpResponse:
    items = (
        Item.objects.select_related('category', 'main_image')
        .prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only('name'))
        )
        .only('name', 'text', 'main_image', 'category__name')
        .filter(
            is_on_main=True,
            is_published=True,
        )
        .order_by('name')
    )
    template = 'homepage/home.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def coffee(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<div>Я чайник</div>', status=HTTPStatus.IM_A_TEAPOT)
