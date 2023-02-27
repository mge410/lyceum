from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def item_list(request: HttpRequest) -> HttpResponse:
    template = 'catalog/item_list.html'
    context = {}
    return render(request, template, context)


def item_detail(request: HttpRequest, id: int) -> HttpResponse:
    template = 'catalog/item_detail.html'
    context = {'id': id}
    return render(request, template, context)
