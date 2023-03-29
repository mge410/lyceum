import django.views.generic
from catalog.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin


class UserItemListView(django.views.generic.ListView, LoginRequiredMixin):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.user_rated_list(self.request.user.id)
