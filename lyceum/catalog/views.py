import django.shortcuts
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Item, Tag


def item_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.catalog_list()
    template = 'catalog/item_list.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def item_detail(request: HttpRequest, id: int) -> HttpResponse:
    item = django.shortcuts.get_object_or_404(
        Item.objects.catalog_detail(),
        pk=id,
    )
    template = 'catalog/item_detail.html'
    context = {'item': item}
    return render(request, template, context)
