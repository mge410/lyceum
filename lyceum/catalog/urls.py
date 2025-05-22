from django.urls import path
from django.urls import re_path
from django.urls import register_converter

from catalog import converters
from catalog import views

register_converter(converters.MyIntegerConverter, "integer")

app_name = "catalog"
urlpatterns = [
    path(
        "",
        views.ItemListView.as_view(),
        name="item_list",
    ),
    path(
        "new/",
        views.NewItemListView.as_view(),
        name="new_item_list",
    ),
    path(
        "friday/",
        views.FridayItemListView.as_view(),
        name="friday_item_list",
    ),
    path(
        "unchecked/",
        views.UncheckedItemListView.as_view(),
        name="unchecked_item_list",
    ),
    path(
        "<int:id>/",
        views.ItemDetailView.as_view(),
        name="item_detail",
    ),
    re_path(
        r"re/(?P<id>[1-9][0-9]*)/",
        views.ItemDetailView.as_view(),
        name="detail_re",
    ),
    path(
        r"converter/<integer:id>/",
        views.ItemDetailView.as_view(),
        name="detail_converter",
    ),
]
