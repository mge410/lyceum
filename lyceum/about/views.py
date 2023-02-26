from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    template = 'about/index.html'
    context = {}
    return render(request, template, context)
