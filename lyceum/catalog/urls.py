from catalog import converters, views
from django.urls import path, re_path, register_converter

register_converter(converters.MyIntegerConverter, 'integer')

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.show, name='detail'),
    re_path(r're/(?P<id>[1-9][0-9]*)/', views.show, name='detail_re'),
    path(
        r'converter/<integer:id>/', views.show, name='detail_converter'
    ),
]
