from catalog.models import Item
from django.views.generic import ListView, DetailView


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


class ItemDetailView(DetailView):
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    queryset = Item.objects.catalog_detail()
