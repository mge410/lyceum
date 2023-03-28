from django.views.generic import View
from django.shortcuts import render
from rating.models import Grade


class UserStatsView(View):
    '''View to get information about rating statistics with user_id'''

    template_name = 'stats/userstats.html'

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
