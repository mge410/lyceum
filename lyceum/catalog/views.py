from catalog.models import Item
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import django.views.generic
import catalog.forms
import rating.models
import django.db.models
import django.urls


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


def item_detail(request: HttpRequest, id: int) -> HttpResponse:
    item = django.shortcuts.get_object_or_404(
        Item.objects.catalog_detail(),
        pk=id,
    )
    template = 'catalog/item_detail.html'
    context = {'item': item}
    return render(request, template, context)


class ItemDetailView(
    django.views.generic.DetailView, django.views.generic.edit.ModelFormMixin
):
    template_name = 'catalog/item_detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    queryset = Item.objects.catalog_detail()
    form_class = catalog.forms.GradeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_id = self.kwargs[self.pk_url_kwarg]
        item_grades = (
            rating.models.Grade.objects.select_related(
                "item",
            )
                .filter(item__id=item_id)
                .only("rating", "item__id", "user__id")
        )

        # print(rating.models.Grade.objects.get(user__id=58)) 58
        average = item_grades.aggregate(
            count=django.db.models.Count("rating"),
            average=django.db.models.Avg("rating"),
        )

        num2word = {i.value: i.name for i in rating.models.Grade.Rating}
        beautiful_rate = num2word[str(round(average["average"]))]

        context["beautiful_rate"] = beautiful_rate
        context["average_rate"] = average["average"]
        context["count_grades"] = average["count"]

        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form_valid(self.form_class(self.request.POST))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            try:
                grade = form.save(commit=False)
                print(grade, "!!!!!!!!!!!!!!!!!!!!!!!")
                grade.user = self.request.user
                grade.item = self.get_object()
                grade.save()
            except django.db.utils.IntegrityError:

                grade = rating.models.Grade.objects.get(
                    item__id=self.get_object().id,
                    user__id=self.request.user.id,
                )
                print(grade, "!OOOOOOOOOOOOOOOOOOOOOOOOO")
                rate = form.cleaned_data.get(
                    rating.models.Grade.rating.field.name, )
                grade.rating = rate
                grade.save()

        return super().form_valid(form)

    def get_success_url(self):
        return django.urls.reverse_lazy(
            'catalog:item_detail',
            kwargs={self.pk_url_kwarg: self.kwargs[self.pk_url_kwarg]},
        )


"""        try:
            print("!!!!!!!!!!!!!!!!!!!!!!!")
            grade = form.save(commit=False)
            grade.user = self.request.user
            grade.item = self.get_object()
            grade.save()
        except django.db.utils.IntegrityError:
            print("!OOOOOOOOOOOOOOOOOOOOOOOOO")
            grade = rating.models.Grade.objects.get(
                item__id=self.get_object().id,
                user__id=self.request.user.id,
            )
            grade.user = self.request.user
            grade.item = self.get_object()
            rate = form.cleaned_data.get(rating.models.Grade.rating.field.name)
            grade.rating = rate
            grade.save()"""
