from datetime import datetime

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def item_list(request: HttpRequest) -> HttpResponse:
    template = 'catalog/item_list.html'
    context = {'date': datetime.now().strftime('%Y %m %d %H:%M')}
    return render(request, template, context)


def item_detail(request: HttpRequest, id: int) -> HttpResponse:
    template = 'catalog/item_detail.html'
    context = {'id': id}
    return render(request, template, context)
