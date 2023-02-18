from django.http import HttpRequest, HttpResponse


def item_list(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<div>Список элементов</div>')


def item_detail(request: HttpRequest, id: int) -> HttpResponse:
    return HttpResponse(f'<div>Подробно элемент id: {id}</div>')
