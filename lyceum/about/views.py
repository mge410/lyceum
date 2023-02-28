from datetime import datetime

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render


def description(request: HttpRequest) -> HttpResponse:
    template = 'about/description.html'
    context = {'date': datetime.now().strftime('%Y %m %d %H:%M')}
    return render(request, template, context)
