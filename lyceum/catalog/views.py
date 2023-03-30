from django.contrib import messages
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
import django.views.generic
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

import catalog.models
from catalog.models import Item
import rating.forms
import rating.models


class ItemListView(django.views.generic.ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    queryset = Item.objects.catalog_list()


class NewItemListView(django.views.generic.ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    queryset = Item.objects.new_item_list()


class FridayItemListView(django.views.generic.ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    queryset = Item.objects.friday_item_list()


class UncheckedItemListView(django.views.generic.ListView):
    template_name = 'catalog/item_list.html'
    context_object_name = 'items'
    queryset = Item.objects.unchecked_item_list()


class ItemDetailView(FormMixin, DetailView):
    model = catalog.models.Item
    form_model = rating.models.Grade
    template_name = 'catalog/item_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'item'
    form_class = rating.forms.GradeForm

    def get_context_data(self, *args, **kwargs) -> dict:
        context = super().get_context_data(*args, **kwargs)

        sum_grades, number = 0, 0
        item_grades = rating.models.Grade.objects.get_item_grades(
            self.kwargs['id']
        )
        min_rating, max_rating = 6, 0
        for grade in item_grades:
            if grade.rating == '':
                continue
            sum_grades += int(grade.rating)
            number += 1
            if int(grade.rating) >= max_rating:
                user_max_rating = grade.user.username
                max_rating = int(grade.rating)
            if int(grade.rating) <= min_rating:
                user_min_rating = grade.user.username
                min_rating = int(grade.rating)
            if self.request.user.id == grade.user.id:
                context['user_grade'] = grade

        context['count_grades'] = number
        if number == 0:
            context['average_rate_value'] = 0
        else:
            context['average_rate_value'] = sum_grades / number
            context['user_max_rating'] = user_max_rating
            context['user_min_rating'] = user_min_rating
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('catalog:item_detail', kwargs={'id': kwargs['id']})

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.form_class(request.POST or None)
        if form.is_valid():
            if form.cleaned_data['rating']:
                self.form_model.objects.update_or_create(
                    user_id=request.user.id,
                    item_id=self.kwargs['id'],
                    defaults=form.cleaned_data,
                )
                messages.success(request, 'Product with a rating')
            else:
                self.form_model.objects.filter(
                    user_id=request.user.id, item_id=self.kwargs['id']
                ).delete()
                messages.success(request, 'Rating removed')
        return redirect(self.get_success_url(**self.kwargs))
