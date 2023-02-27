from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def description(request: HttpRequest) -> HttpResponse:
    template = 'about/description.html'
    context = {}
    return render(request, template, context)
