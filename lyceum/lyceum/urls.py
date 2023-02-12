from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
]
