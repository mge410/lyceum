from catalog.models import Item
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import django.views.generic
from django.views.generic import DetailView, ListView


class ItemListView(ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    queryset = Item.objects.catalog_list()


class NewItemListView(ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    queryset = Item.objects.new_item_list()


class FridayItemListView(ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    queryset = Item.objects.friday_item_list()


class UncheckedItemListView(ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    queryset = Item.objects.unchecked_item_list()


def item_detail(request: HttpRequest, id: int) -> HttpResponse:
    item = django.shortcuts.get_object_or_404(
        Item.objects.catalog_detail(),
        pk=id,
    )
    template = 'catalog/item_detail.html'
    context = {'item': item}
    return render(request, template, context)
class ItemDetailView(DetailView):
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    queryset = Item.objects.catalog_detail()


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
