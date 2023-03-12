from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def feedback(request: HttpRequest) -> HttpResponse:
    template = 'feedback/feedback.html'
    context = {}
    return render(request, template, context)
