from http import HTTPStatus

from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import TemplateView

from catalog.models import Item


class HomeView(ListView):
    template_name = 'homepage/home.html'
    context_object_name = 'items'
    queryset = Item.objects.homepage()


class CoffeeView(TemplateView):
    template_name = 'homepage/coffee.html'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=HTTPStatus.IM_A_TEAPOT)
