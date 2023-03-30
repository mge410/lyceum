from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
import django.views.generic

from catalog.models import Item
from rating.models import Grade


class UserItemListView(LoginRequiredMixin, django.views.generic.ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.user_rated_list(self.request.user.id)


class UserStatisticView(View):
    """View to get information about rating statistics with user_id"""

    template_name = 'statistic/user_statistic.html'

    def get(self, request, id):
        items = Grade.objects.get_filtered_items(user_id=id)

        if len(items) == 0:
            context = {
                'is_successful': 0,
            }
        else:
            sum_of_rates = 0
            for item in items:
                sum_of_rates += int(item.rating)
            average_rate = round(sum_of_rates / len(items), 2)
            context = {
                'is_successful': 1,
                'worst_rated_item': items[0].item,
                'best_rated_item': items[len(items) - 1].item,
                'count_rates': len(items),
                'average_rate': average_rate,
            }
        return render(request, self.template_name, context)
