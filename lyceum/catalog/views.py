import django.shortcuts
from catalog.models import Item
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import django.views.generic


def item_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.catalog_list()
    template = 'catalog/item_list.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def new_item_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.new_item_list()
    template = 'catalog/item_list.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def friday_item_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.friday_item_list()
    template = 'catalog/item_list.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def unchecked_item_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.unchecked_item_list()
    template = 'catalog/item_list.html'
    context = {
        'items': items,
    }
    return render(request, template, context)


def item_detail(request: HttpRequest, id: int) -> HttpResponse:
    item = django.shortcuts.get_object_or_404(
        Item.objects.catalog_detail(),
        pk=id,
    )
    template = 'catalog/item_detail.html'
    context = {'item': item}
    return render(request, template, context)


class ItemDetailView(django.views.generic.DetailView,
                     django.views.generic.edit.ModelFormMixin):
    template_name = 'catalog/item_detail.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = django.shortcuts.get_object_or_404(
            Item.objects.catalog_detail(),
            pk=kwargs["id"],
        )
        context["item"] = item

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
