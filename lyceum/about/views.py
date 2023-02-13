from django.http import HttpResponse


def description(request):
    return HttpResponse('<div>О проекте</div>')
