from about import views
from django.urls import path

app_name = 'about'
urlpatterns = [
    path('', views.DescriptionView.as_view(), name='description'),
]
