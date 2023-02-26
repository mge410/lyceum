from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<div>Список элементов</div>')


def show(request: HttpRequest, id: int) -> HttpResponse:
    return HttpResponse(f'<div>Подробно элемент id: {id}</div>')
