from about import views
from django.urls import path

app_name = 'about'
urlpatterns = [
    path('', views.index, name='index'),
]
