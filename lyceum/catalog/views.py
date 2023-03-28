import django.db.models
import django.shortcuts
import django.urls
import django.views.generic
import rating.forms
import rating.models
from catalog.models import Item
from django.utils.translation import gettext as _


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


class ItemDetailView(
    django.views.generic.DetailView, django.views.generic.edit.ModelFormMixin
):
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    queryset = Item.objects.catalog_detail()
    form_class = rating.forms.GradeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_id = self.kwargs[self.pk_url_kwarg]

        average = rating.models.Grade.objects.get_item_grades(
            item_id
        ).aggregate(
            count=django.db.models.Count('rating'),
            average=django.db.models.Avg('rating'),
        )

        rating_value_choices = {
            choice.value: choice.name for choice in rating.models.Grade.Rating
        }

        if average['average']:
            average_rating_name = rating_value_choices[
                str(round(average['average']))
            ]
        else:
            average_rating_name = _('No rating information')
            average['average'] = ''

        context['average_rating_name'] = average_rating_name
        context['average_rate_value'] = average['average']
        context['count_grades'] = average['count']

        if self.request.user.is_authenticated:
            try:
                grade = rating.models.Grade.objects.get(
                    item__id=self.get_object().id,
                    user__id=self.request.user.id,
                )
                context['form'].fields['rating'].initial = grade.rating
            except rating.models.Grade.DoesNotExist:
                context['form'].fields['rating'].initial = '3'
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        instance, _ = rating.models.Grade.objects.get_or_create(
            item__id=self.get_object().id,
            user__id=self.request.user.id,
            defaults={'item': self.get_object(), 'user': self.request.user},
        )
        self.form_valid(self.form_class(self.request.POST, instance=instance))

        return django.shortcuts.redirect(self.get_success_url())

    def form_valid(self, form):
        if form.is_valid():
            grade = form.save(commit=False)

            rate = form.cleaned_data.get(
                rating.models.Grade.rating.field.name,
            )
            grade.rating = rate
            grade.save()

        return super().form_valid(form)

    def get_success_url(self):
        return django.urls.reverse_lazy(
            'catalog:item_detail',
            kwargs={self.pk_url_kwarg: self.kwargs[self.pk_url_kwarg]},
        )
