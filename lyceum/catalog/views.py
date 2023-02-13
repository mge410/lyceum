from django.http import HttpResponse


def item_list(request):
    return HttpResponse('<div>Список элементов</div>')


def item_detail(request, id):
    return HttpResponse(f'<div>Подробно элемент id: {id}</div>')
