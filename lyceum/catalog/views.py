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
        user = self.request.user

        grades = rating.models.Grade.objects.get_item_grades(item_id)

        sum_rating = 0
        count = len(grades)

        user_min_rating, user_max_rating = None, None

        if count != 0:
            user_min_rating = grades[0].user.username
            user_max_rating = grades[len(grades) - 1].user.username
        user_grade = None

        for grade in grades:
            if user.id == grade.user.id:
                user_grade = grade
            sum_rating += int(grade.rating)
        rating_value_choices = {
            choice.value: choice.name for choice in rating.models.Grade.Rating
        }

        if count:
            average = sum_rating / count
            average_rating_name = rating_value_choices[str(round(average))]
        else:
            average_rating_name = _('No rating information')
            average = ''

        context['average_rating_name'] = average_rating_name
        context['average_rate_value'] = average
        context['count_grades'] = count

        context['user_min_rating'] = user_min_rating
        context['user_max_rating'] = user_max_rating

        if user.is_authenticated:
            if user_grade is None:
                context['form'].fields[
                    rating.models.Grade.rating.field.name
                ].initial = '3'
                context['form'].fields['delete_grade'].disabled = True
                context['form'].fields['delete_grade'].widget.attrs[
                    'hidden'
                ] = '1'
            else:
                context['form'].fields[
                    rating.models.Grade.rating.field.name
                ].initial = user_grade.rating

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
            delete_grade = form.cleaned_data.get('delete_grade')
            if delete_grade:
                form.instance.delete()
                return super(
                    django.views.generic.edit.ModelFormMixin, self
                ).form_valid(form)

            grade = form.save(commit=False)
            rate = form.cleaned_data.get(
                rating.models.Grade.rating.field.name,
            )
            grade.rating = rate
            grade.save()

        return super(
            django.views.generic.edit.ModelFormMixin, self
        ).form_valid(form)

    def get_success_url(self):
        return django.urls.reverse_lazy(
            'catalog:item_detail',
            kwargs={self.pk_url_kwarg: self.kwargs[self.pk_url_kwarg]},
        )
