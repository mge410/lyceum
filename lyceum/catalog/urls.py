from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.MyIntegerConverter, 'integer')

urlpatterns = [
    path('', views.item_list),
    path('<int:id>', views.item_detail),
    re_path(r're/(?P<id>\d+)', views.item_detail),
    path(r'converter/<integer:id>', views.item_detail),
]
