from django.http import HttpRequest, HttpResponse


def description(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<div>О проекте</div>')
