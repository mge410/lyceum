from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    template = 'catalog/index.html'
    context = {}
    return render(request, template, context)


def show(request: HttpRequest, id: int) -> HttpResponse:
    template = 'catalog/show.html'
    context = {}
    return render(request, template, context)
