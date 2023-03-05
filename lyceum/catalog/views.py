from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Prefetch
from catalog.models import Item, Tag


def item_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.catalog_list()
    template = 'catalog/item_list.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def item_detail(request: HttpRequest, id: int) -> HttpResponse:
    template = 'catalog/item_detail.html'
    context = {'id': id}
    return render(request, template, context)
