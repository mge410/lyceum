from catalog import converters
from catalog import views
from django.urls import path
from django.urls import re_path
from django.urls import register_converter

register_converter(converters.MyIntegerConverter, 'integer')

app_name = 'catalog'
urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:id>/', views.item_detail, name='detail'),
    re_path(r're/(?P<id>[1-9][0-9]*)/', views.item_detail, name='detail_re'),
    path(
        r'converter/<integer:id>/', views.item_detail, name='detail_converter'
    ),
]
